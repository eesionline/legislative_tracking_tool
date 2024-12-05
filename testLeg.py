import requests

def get_bills_by_date(date):
    # LegiScan API endpoint and parameters
    api_key = "69655a3d92bf217d493339b996112205"
    base_url = "https://api.legiscan.com/"
    
    # Initial parameters for getMasterList operation
    params_masterlist = {
        "key": api_key,
        "op": "getMasterList",
        "state": "US"  # Specifies Congress
    }
    
    # Send request to the LegiScan API to get the master list of bills
    response = requests.get(base_url, params=params_masterlist)
    data = response.json()
    
    # Check for successful response
    if data.get("status") != "OK":
        print("Error:", data.get("alert", "Failed to retrieve data"))
        return []

    # Retrieve and filter bill information based on the specified date
    bills_info = []
    bills = data["masterlist"]
    
    for bill_id, bill_data in bills.items():
        if isinstance(bill_data, dict) and bill_data.get("last_action_date") == date:
            # Parameters for getBill operation to retrieve detailed information for each bill
            params_getbill = {
                "key": api_key,
                "op": "getBill",
                "id": bill_data.get("bill_id")
            }
            
            # Send request to the LegiScan API to get detailed bill information
            detailed_response = requests.get(base_url, params=params_getbill)
            detailed_data = detailed_response.json()
            
            # Check for successful response in the detailed call
            if detailed_data.get("status") != "OK":
                print("Error:", detailed_data.get("alert", "Failed to retrieve detailed data"))
                continue
            
            # Extracting information including categorized sponsors and committee details
            bill_detail = detailed_data.get("bill", {})
            sponsors = bill_detail.get("sponsors", [])
            
            # Categorize sponsors based on sponsor_order
            primary_sponsors = [sponsor.get("name") for sponsor in sponsors if sponsor.get("sponsor_order") == 1]
            cosponsors = [sponsor.get("name") for sponsor in sponsors if sponsor.get("sponsor_order") == 2]
            generic_sponsors = [sponsor.get("name") for sponsor in sponsors if sponsor.get("sponsor_order") == 0]
            
            # Handle missing last_action and last_action_date
            last_action = bill_detail.get("last_action", "No action available")
            last_action_date = bill_detail.get("last_action_date", "Date not available")

            bill_info = {
                "bill_number": bill_detail.get("bill_number"),
                "title": bill_detail.get("title"),
                "primary_sponsors": primary_sponsors,
                "cosponsors": cosponsors,
                "generic_sponsors": generic_sponsors,
                "committee": bill_detail.get("committee", {}).get("name", "N/A"),
                "summary": bill_detail.get("description", "No summary available"),
                "latest_action": last_action,
                "latest_action_date": last_action_date
            }
            bills_info.append(bill_info)
    
    return bills_info

# Example usage
date = "2024-11-08"  # Specify date here in YYYY-MM-DD format
bills_info = get_bills_by_date(date)

# Print retrieved bill information
for bill in bills_info:
    print("Bill Number:", bill["bill_number"])
    print("Title:", bill["title"])
    print("Primary Sponsors:", ", ".join(bill["primary_sponsors"]) if bill["primary_sponsors"] else "N/A")
    print("Cosponsors:", ", ".join(bill["cosponsors"]) if bill["cosponsors"] else "N/A")
    print("Generic Sponsors:", ", ".join(bill["generic_sponsors"]) if bill["generic_sponsors"] else "N/A")
    print("Committee:", bill["committee"])
    print("Summary:", bill["summary"])
    print("Latest Action:", bill["latest_action"])
    print("Latest Action Date:", bill["latest_action_date"])
    print("-" * 50)
