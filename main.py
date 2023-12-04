import inquirer
import requests
from bs4 import BeautifulSoup
import time
import datetime
import sys
import signal

banner = '''


   ___   __        ___  __  _____  ___   ___     ___      _            _____                _
  / __\ /__\/\_/\ / _ \/__\/__   \/ __\ /___\   / _ \_ __(_) ___ ___  /__   \_ __ __ _  ___| | _____ _ __
 / /   /_\  \_ _// /_)/_\    / /\/ /   //  //  / /_)/ '__| |/ __/ _ \   / /\/ '__/ _` |/ __| |/ / _ \ '__|
/ /___//__   / \/ ___//__   / / / /___/ \_//  / ___/| |  | | (_|  __/  / /  | | | (_| | (__|   <  __/ |
\____/\__/   \_/\/   \__/   \/  \____/\___/   \/    |_|  |_|\___\___|  \/   |_|  \__,_|\___|_|\_\___|_|


'''
banner1 = '''


 ____ _  _,      ___,____,_____,  __, _,_, _____,  _____,
(-|__(-\_/      (-/_(-(__(-/_(-|\ (-|  (-|(-/_(-|\ (-(__
 _|__) _|,      _((_/_____/  |_| \|_|____|_/  |_| \|____)
(     (        (    (   (    (    (   (  (    (    (


'''

url = 'https://ceypetco.gov.lk/marketing-sales/'

question1 = [
  inquirer.List('oil_type',
                message="What oil type do you need to keep track of?",
                choices=['Petrol 92 Octane', 'Petrol 95 Octane', 'Auto Diesel', 'Super Diesel 4', 'Kerosene', 'Industrial Kerosene'],
                ),
            ]
question2 = [
  inquirer.Text('date_line',
                message="Enter Full Line Here"),
            ]

fuel_number_mapping = {
    "Petrol 92 Octane": 0,
    "Petrol 95 Octane": 1,
    "Auto Diesel": 2,
    "Super Diesel 4": 3,
    "Kerosene": 4,
    "Industrial Kerosene": 5
}


def get_user_input(question1, question2, url):
    answers = inquirer.prompt(question1)
    oil_type = answers["oil_type"]

    print(f"Go to {url} and Enter full line of Effect date")
    answers = inquirer.prompt(question2)
    date_line = answers["date_line"]

    print("Gathering Data.....")
    print(f"Currently -", date_line)
    print("Starting.....")

    return oil_type, date_line

def create_timestamp():
    current_time = datetime.datetime.now()
    timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")

    return timestamp

def get_html(url):
    # Gets the HTML of a URL and returns it.

    response = requests.get(url)
    html = response.content
    return html

def get_link_parts(html):
    soup = BeautifulSoup(html, 'html.parser')

    date_parts = []
    price_parts = []
    for row in soup.find_all('div', {'class': 'card'}):
        link_tags = row.find_all('p')
        date_tag = link_tags[1]
        price_tag = link_tags[0]

        if date_tag is not None:
            date_parts.append(date_tag)
        else:
            continue

        if price_tag is not None:
            price_parts.append(price_tag)
        else:
            continue

    return date_parts, price_parts

def print_status(date_parts, price_parts, oil_type, date_line, timestamp):
    numeric_value = fuel_number_mapping.get(oil_type)
    date = date_parts[numeric_value].text
    price = price_parts[numeric_value].text
    if date == date_line:
        print(f"{timestamp}: Status- Not Changed")
    else:
        print(f"{timestamp}: Status- Changed")
        print(date)
        print(price)
        print("\a")  # This rings the terminal bell
        """
        Change below code accordingly to include function of sending message to telegram when price changed.
        res = requests.post(f'https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/sendMessage?chat_id={ID}&text=Price+Changed\n{date}\n{price}')
        """

def interrupt_handler(signum, frame):
  print("\nProgram interrupted by user. Exiting...")
  # Perform any necessary cleanup tasks before exiting
  sys.exit(1)

signal.signal(signal.SIGINT, interrupt_handler)

if __name__ == '__main__':
    print(banner)
    print(banner1)
    oil_type, date_line = get_user_input(question1, question2, url)
    while True:
        timestamp = create_timestamp()
        html = get_html(url)
        date_parts, price_parts = get_link_parts(html)
        print_status(date_parts, price_parts, oil_type, date_line, timestamp)
        time.sleep(300)  # Sleeps for - 60 * 5 = 300 (5 minutes)
