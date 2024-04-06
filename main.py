import requests
from bs4 import BeautifulSoup
import smtplib

# Define the URL of the product page
url = 'https://www.amazon.com/dp/B081WQY69Y'

with open('password.txt', 'r') as f:
    password = f.read()


def find_price():
    page = requests.get(url)

    soup = BeautifulSoup(page.content, 'html.parser')

    price_whole = soup.find(attrs={"class": "a-price-whole"}).get_text()
    price_decimal = soup.find(attrs={"class": "a-price-fraction"}).get_text()

    price_total = float(price_whole + price_decimal)

    return price_total


def send_mail(subject, body):
    smtp_server = 'smtp.gmail.com'
    port = 587
    sender_email = 'devthekar@gmail.com'
    receiver_email = 'devthekar@gmail.com'

    # Create email message
    message = f"Subject: {subject}\n\n{body}"

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def main():

    price = find_price()

    if price < 25:
        subject = "Price Lowered!"
        body = "Your price is now $" + str(price)
        send_mail(subject, body)


if __name__ == "__main__":
    main()