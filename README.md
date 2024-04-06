# Amazon Price Tracker

This Python script monitors the price of a product on Amazon and sends an email notification if the price drops below a certain threshold.

## Dependencies
- requests
- BeautifulSoup4
- smtplib

## Installation
1. Install the required dependencies:
   ```bash
   pip install requests beautifulsoup4


## Usage
Define the URL of the product page in the item variable.
Run the script using Python:
```python main.py```

## Features
- Scrapes the product page to extract the current price.
- Sends an email notification if the price drops below a specified threshold.
- Uses BeautifulSoup for web scraping and smtplib for email notifications.

## Configuration
- Update the item variable with the URL of the product you want to track.
- Customize the email sender and receiver addresses in the send_mail function.
- Adjust the price threshold in the main function to trigger notifications at your desired price point. 
- Store your email password securely in a password.txt file in the same directory as the script.

## Disclaimer
This script is provided for educational purposes only. Use it responsibly and ensure compliance with Amazon's terms of service and any applicable laws and regulations.