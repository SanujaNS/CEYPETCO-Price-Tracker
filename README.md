# CEYPETCO-Price-Tracker

![Screenshot_20231205_002718](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/c7d7613d-496d-4be1-bfe3-e82271d877f7)


This is a Python code to keep track of the price of oil of your choice distributed by CEYPETCO.

## Features

* Can use with any type of oil - ['Petrol 92 Octane', 'Petrol 95 Octane', 'Auto Diesel', 'Super Diesel 4', 'Kerosene', 'Industrial Kerosene']
* Can change interval time
* Sends notification messages of price changes via Telegram

## Requirements

> * requests
> * beautifulsoup4
> * inquirer

### 1. Get Code
```bash
git clone https://github.com/SanujaNS/CEYPETCO-Price-Tracker.git
cd CEYPETCO-Price-Tracker/
```

### 2. Install requirements
```python
python -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install -r requirements.txt
```

### 3. Run Code
```python
python main.py
```

### 4. Select oil type
![Screenshot_20231205_003937](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/f91b54c0-393d-4342-862f-44b0e9aaf846)

### 5. Enter Current "Effect date"
1. Go to the website [https://ceypetco.gov.lk/marketing-sales/](https://ceypetco.gov.lk/marketing-sales/)
2. Copy whole line of your choice
![Screenshot_20231205_004231](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/1762a35c-ca62-4857-823d-a3a60262e6d2)
4. Paste it in the terminal

![Screenshot_20231205_004508](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/dfbcd026-5c5d-45bb-b2e0-9e9faa502b5a)

## Setup Telegram Notifications

For telegram notifications,
![Screenshot_20231205_005153-1](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/d39b73a1-9d67-4c51-bcd6-ce9f3c7bc52b)
remove comment shown in above picture and fill values(bot_token, chat_id) accordingly.
If you don't know how to get those values, just a simple google search will do. There are lot of tutorials for that.
So I'm not explainig them here.

If everything is configured correctly, you will get a notification like this when the price changes.
![Screenshot_20231205_001035](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/f3651230-c967-4d83-a3a0-408ada67dd2b)


## Screenshots

### 1. Status: Not Changed
![Screenshot_20231205_000656](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/ad0cbd43-06fa-40a0-910a-9b9903433fa2)

### 2. Status: Changed
![Screenshot_20231205_000938](https://github.com/SanujaNS/CEYPETCO-Price-Tracker/assets/66342986/0c2bb79e-7469-4890-b8e7-df5345f88c81)

# Donation

|**[Buy me a coffee ☕](https://bmc.link/sanujans)**|
|---------------------------------------------------|
|![](assets/bmc_sanujans.jpg)                       |
|                                                   |

# License

GNU General Public License v3.0
