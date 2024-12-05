import requests
import json
from datetime import datetime

def get_bill_summary(api_key, congress_number, bill_type, bill_number):
    # Build the URL to get the bill summary
    url = f"https://api.congress.gov/v3/bill/{congress_number}/{bill_type}/{bill_number}/summaries"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key
    }
    
    # Make the request to get the bill summary
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        summaries = response.json().get('summaries', [])
        # Return the first summary (if available)
        return summaries[0].get('text', 'No summary available') if summaries else 'No summary available'
    else:
        raise Exception(f"Error: Unable to retrieve summary (status code: {response.status_code})")

def get_bill_committees(api_key, congress_number, bill_type, bill_number):
    # Build the URL to get the bill summary
    url = f"https://api.congress.gov/v3/bill/{congress_number}/{bill_type}/{bill_number}/committees"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key
    }
    
    # Make the request to get the bill committees
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        committees = response.json().get('committees', [])
        # Return the first summary (if available)
        return committees[0].get('name', 'No committee information available') if committees else 'No committee information available'
    else:
        raise Exception(f"Error: Unable to retrieve committee information (status code: {response.status_code})")

def get_bill_actions(api_key, congress_number, bill_type, bill_number):
    # Build the URL to get the bill summary
    url = f"https://api.congress.gov/v3/bill/{congress_number}/{bill_type}/{bill_number}/actions"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key
    }
    
    # Make the request to get the bill committees
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        actions = response.json().get('actions', [])
        # Return the first action (if available)
        return actions[0].get('text', 'No latest action available') if actions else 'No latest action available'
    else:
        raise Exception(f"Error: Unable to retrieve latest action information (status code: {response.status_code})")


def get_bills_from_date(api_key, date):
    # Format the date to make sure it's in the right format (YYYY-MM-DD)
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Incorrect date format. Please use YYYY-MM-DD.")

    url = f"https://api.congress.gov/v3/bill"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key
    }

    params = {
        "fromDate": date,
        "toDate": date,
        "format": "json",
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        bills = response.json()
        return bills
    else:
        raise Exception(f"Error: Unable to retrieve bills (status code: {response.status_code})")
    
def get_bill_sponsor(api_key, congress_number, bill_type, bill_number):
    # Build the URL to get the bill sponsor
    url = f"https://api.congress.gov/v3/bill/{congress_number}/{bill_type}/{bill_number}"
    headers = {
        "Accept": "application/json",
        "x-api-key": api_key
    }
    
    # Make the request to get the bill committees
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        sponsors = response.json().get('bill', {}).get('sponsors', [])
        # Return the first summary (if available)
        return sponsors[0].get('fullName', 'No sponsor available') if sponsors else 'No sponsor available'
    else:
        raise Exception(f"Error: Unable to retrieve sponsor information (status code: {response.status_code})")
    
def get_bills_details(api_key, date):
    bills_data = []
    
    # Get the list of bills for the specified date
    bills = get_bills_from_date(api_key, date)
    
    # Iterate through each bill to gather additional details
    for bill in bills.get('bills', []):
        congress_number = bill.get('congress')
        bill_type = bill.get('type').lower()
        bill_type_upper = bill_type.upper()
        bill_number = bill.get('number')
        title = bill.get('title', 'No title available')
        url = bill.get('url')

        # Get latest bill action
        latest_action = get_bill_actions(api_key, congress_number, bill_type, bill_number)

        # Get the bill sponsor
        sponsor = get_bill_sponsor(api_key, congress_number, bill_type, bill_number)

        # Fetch committee and summary details
        try:
            committee = get_bill_committees(api_key, congress_number, bill_type, bill_number)
            summary = get_bill_summary(api_key, congress_number, bill_type, bill_number)
        except Exception as e:
            committee = f"Error: {e}"
            summary = f"Error: {e}"

        # Append details to the list as a dictionary
        bills_data.append({
            "bill_number": bill_number,
            "title": title,
            "sponsor": sponsor,
            "bill_type": bill_type,
            "bill_type_upper": bill_type_upper,
            "committee": committee,
            "summary": summary,
            "url": url,
            "latest_action": latest_action
        })
    
    return bills_data

print(json.dumps(get_bills_details('J0jKbtfI0cbPa6tbAwlnW7gmcYGealzZRhY48hQH', '2024-09-25'), indent = 4))


