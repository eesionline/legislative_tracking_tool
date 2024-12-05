# Legislative Tracking Tool

This project uses the Congress.gov API to retrieve detailed information about congressional bills, including sponsors, committees, summaries, and actions. It is designed to be a tool for tracking legislative activity on specific dates.

## Features

- Retrieve a list of bills introduced on a specific date.
- Fetch detailed information for each bill, including:
  - Bill title
  - Sponsor
  - Committees involved
  - Latest action
  - Summary
  - URL linking to the full bill details (TODO)
- Formats the output as static webpage for ease of selection.

## Technologies Used

- **Python 3.x**
- Libraries:
  - `requests`: For making HTTP requests to the Congress.gov API.
  - `json`: For parsing and formatting API responses.
  - `datetime`: For validating and handling date inputs.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/legislative_tracking_tool.git
   cd legislative_tracking_tool
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Obtain an API key from [Congress.gov API](https://api.congress.gov/) and replace the placeholder in the script with your API key.

## Usage

1. Set your API key in the script:
   Replace `'your-api-key-here'` in the function calls with your actual Congress.gov API key.

2. Call the main function:
   ```python
   from main import get_bills_details

   # Example: Fetch bills from September 25, 2024
   api_key = 'your-api-key-here'
   date = '2024-09-25'
   bills = get_bills_details(api_key, date)

   print(json.dumps(bills, indent=4))
   ```

3. The script will return a JSON object containing details about each bill from the specified date.

### Example JSON Output

```json
[
    {
        "bill_number": "1234",
        "title": "Example Bill Title",
        "sponsor": "John Doe",
        "bill_type": "hr",
        "committee": "House Committee on Transportation",
        "summary": "This is a summary of the bill.",
        "url": "https://www.congress.gov/bill/1234",
        "latest_action": "Referred to the Committee on Rules"
    }
]
```

## Error Handling

- Invalid dates: The script will raise an error if the date format is incorrect (must be `YYYY-MM-DD`).
- Missing data: If certain fields (e.g., summary or committee information) are unavailable, the output will display appropriate error messages.
- API errors: The script will notify the user of API-related issues, such as rate limits or authentication errors.

## Limitations

- The Congress.gov API might return incomplete or limited data depending on the bill's status.
- The script assumes a working internet connection and valid API access.

## Contributions

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request with a detailed description of your changes.

## Contact

For questions or suggestions, contact Josh Cohen as joshuacohen179@gmail.com.
