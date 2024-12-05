import requests

def fetch_bills_by_date(date):
    api_key = "J0jKbtfI0cbPa6tbAwlnW7gmcYGealzZRhY48hQH"
    url = f"https://api.congress.gov/v3/bills?introduced_date={date}&api_key={api_key}"
    
    response = requests.get(url)
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        return []

    bills_data = response.json().get('bills', [])
    bills = []
    
    for bill in bills_data:
        bill_details = {
            "bill_number": bill.get("bill_number"),
            "title": bill.get("title"),
            "sponsor": bill.get("sponsor", {}).get("name"),
            "bill_type": bill.get("bill_type"),
            "committees": [committee['name'] for committee in bill.get("committees", [])],
            "summary": bill.get("summary", {}).get("text"),
            "latest_action": bill.get("latest_action", {}).get("description"),
        }
        bills.append(bill_details)
    
    return bills

# Example usage
date = "2024-10-31"  # Example date in YYYY-MM-DD format
bills = fetch_bills_by_date(date)
for bill in bills:
    print(f"Bill Number: {bill['bill_number']}")
    print(f"Title: {bill['title']}")
    print(f"Sponsor: {bill['sponsor']}")
    print(f"Bill Type: {bill['bill_type']}")
    print(f"Committees: {', '.join(bill['committees'])}")
    print(f"Summary: {bill['summary']}")
    print(f"Latest Action: {bill['latest_action']}")
    print("-" * 40)
