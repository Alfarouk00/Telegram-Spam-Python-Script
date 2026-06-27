
## Overview

This Python script demonstrates how to connect to Telegram using the Telethon library and send scheduled messages to a Telegram group or channel that you own or are authorized to manage.

## Features

* Connects to your Telegram account.
* Lists available groups and channels.
* Allows you to select a destination.
* Sends a predefined message at a fixed time interval.
* Automatically retries if a temporary error occurs.

## Requirements

* Python 3.8 or later
* Telethon library

Install Telethon:

```
pip install telethon
```

## Configuration

Open the Python script and edit the following values:

API_ID
Your Telegram API ID.

API_HASH
Your Telegram API Hash.

MESSAGE
The message you want to send.

INTERVAL
Number of seconds between scheduled messages.

Example:

```
API_ID = 12345678
API_HASH = "your_api_hash"
MESSAGE = "Hello everyone!"
INTERVAL = 60
```

## Getting API Credentials

1. Sign in to Telegram.
2. Visit https://my.telegram.org
3. Create an API application.
4. Copy your API ID and API Hash into the script.

## Running the Script

Run:

```
python your_script.py
```

The first time you run it:

* Enter your phone number.
* Enter the verification code sent by Telegram.
* Complete two-factor authentication if enabled.

A session file will be created so you won't need to log in every time.

## How It Works

1. Connects to Telegram.
2. Retrieves your groups and channels.
3. Displays a numbered list.
4. Lets you choose one.
5. Sends the configured message at the specified interval until you stop the program.

## Stopping the Script

Press:
Ctrl + C
     to stop the program safely.

## Notes

* Only use this script in groups or channels where you have permission to send scheduled announcements.
* Sending unsolicited or excessive messages may violate Telegram's Terms of Service and can result in account restrictions.
* Keep your API ID and API Hash private.
