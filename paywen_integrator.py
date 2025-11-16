import requests
import json
import os
from datetime import datetime

# NOTE: In a real-world scenario, the API key would be required for authenticated requests.
# The documentation does not explicitly show the API key in the request, suggesting
# it might be handled via a pre-authenticated session or a separate setup step.
# For this autonomous agent, we will assume a simple POST request is sufficient
# for a basic paywall creation, as shown in the documentation example.
# If an API key is required, the user would need to provide it as an environment variable.

PAYWEN_API_URL = "https://api.paywen.dev/v1/paywalls"
REPORT_DIR = "reports"
REPORT_BASE_URL = "https://your-public-hosting-service.com/reports/" # Placeholder for user's public URL

def create_paywall(report_filename, price=2.99, currency="USDC"):
    """
    Creates a paywall for the given report file using the Paywen API.
    
    NOTE: This function assumes the report is already uploaded to a public URL.
    In a real-world scenario, the user would need to upload the file and provide
    the base URL for their hosting service (e.g., S3, IPFS, GitHub Pages).
    """
    
    # 1. Construct the full public URL for the report
    report_public_url = REPORT_BASE_URL + report_filename
    
    # 2. Define the payload for the Paywen API
    report_date = datetime.now().strftime("%Y-%m-%d")
    payload = {
        "url": report_public_url,
        "price": price,
        "currency": currency,
        "title": f"Premium AI Research Briefing: {report_date}",
        "description": "Autonomous, AI-curated summary of the latest AI Model Updates and Benchmarks. Powered by the x402 protocol."
        # Additional fields like API key would go here if required by Paywen
    }
    
    headers = {
        "Content-Type": "application/json",
        # "Authorization": f"Bearer {os.environ.get('PAYWEN_API_KEY')}" # Uncomment if API key is needed
    }
    
    print(f"Attempting to create paywall for URL: {report_public_url}")
    
    try:
        response = requests.post(PAYWEN_API_URL, headers=headers, data=json.dumps(payload))
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        paywall_data = response.json()
        
        # The API response should contain the final paywall URL
        paywall_url = paywall_data.get("paywall_url")
        
        if paywall_url:
            print(f"Successfully created Paywen Paywall!")
            print(f"Paywall URL: {paywall_url}")
            return paywall_url
        else:
            print(f"Paywall creation successful, but 'paywall_url' not found in response.")
            print(f"Full response: {paywall_data}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"Error creating paywall: {e}")
        print(f"Response status code: {response.status_code if 'response' in locals() else 'N/A'}")
        print(f"Response text: {response.text if 'response' in locals() else 'N/A'}")
        return None

def main(report_filename):
    # This is a placeholder for testing the function independently
    # In the final script, this will be called by the main automation script.
    
    # NOTE: The user MUST replace REPORT_BASE_URL with their actual public hosting service.
    if REPORT_BASE_URL == "https://your-public-hosting-service.com/reports/":
        print("CRITICAL ERROR: Please update 'REPORT_BASE_URL' in paywen_integrator.py with your actual public hosting service URL.")
        return

    paywall_link = create_paywall(report_filename)
    
    if paywall_link:
        print(f"\nFinal Paywall Link: {paywall_link}")
    else:
        print("\nFailed to generate paywall link.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Error: Report filename argument missing.")
