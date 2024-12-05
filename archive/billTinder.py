import json
import html
import experimental.getBills as getBills
import htmlTest
import re

def filter_relevant_bills(bills):
    relevant_bills = []

    # Iterate through each bill
    for bill in bills.get('bills', []):  # Assuming 'bills' is the key in the API response (so pls don't change this)
        
        # Display a summary of the bill to the user (title, bill number, etc...)
        bill_type = bill.get('type', 'N/A').lower()
        bill_number = bill.get('number', 'N/A')
        congress_number = bill.get('congress', 'N/A')
        bill_title = bill.get('title', 'No Title Available')

        # Get the summary for each bill using an additional API call
        summary_html = getBills.get_bill_summary(api_key, congress_number, bill_type, bill_number)

        # Ditto for committees
        bill_committees = getBills.get_bill_committees(api_key, congress_number, bill_type, bill_number)

        summary = summary_html #do something about ugly html display eventually...

        re.sub('<[^<]+?>', '', summary)
  

        print(f"\nBill Number: {bill_type.upper()}{bill_number}")
        print(f"Title: {bill_title}")
        print(f"Committees: {bill_committees}")
        print(f"Summary: {summary}")

        # Ask the user if the bill is relevant
        user_input = input("Is this bill relevant? (y/n): ").lower()

        summary_html = f"""
        <p><b>{bill_title}</b></p>
        <p>{summary}</p>
        """

        htmlTest.display_html_in_browser(summary_html)

        # If the user says 'y', collect the bill
        if user_input == 'y':
            relevant_bills.append(bill)

    return relevant_bills

def print_relevant_bills(relevant_bills):
    # print the relevant bills
    print("\nRelevant Bills:\n")
    print(json.dumps(relevant_bills, indent=4))

# Input: API Key and the date to retrieving bills from
api_key_file = open('apikey.txt','r')
api_key = api_key_file.read()
date = "2024-11-01"  # Input date here!! Will be replaced with user input when we work on the UI :D

bills = getBills.get_bills_from_date(api_key, date)

# Step 1: Filter relevant bills
relevant_bills = filter_relevant_bills(bills)

# Step 2: Pretty print the relevant bills
print_relevant_bills(relevant_bills)
