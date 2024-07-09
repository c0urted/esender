# Esender

### Esender aims to be an AIO spamming toolkit. The script provides a simple command-line menu interface that is easy to navigate.


![image](https://github.com/c0urted/esender/assets/65371714/a015feed-142a-4c08-a8b7-0a42ac349a5a)


## Features
Email Sendouts: Send emails to multiple recipients using a specified SMTP server.

email2SMS Sendouts: Send SMS messages to multiple recipients using a specified SMTP server.

Email Letter Support: Choose to send emails with a pre-defined HTML letter or simple text content.

Email Validation (TODO): Validate email addresses to check if they are valid and active.

UTF-8 Encoding: Include special characters and Unicode symbols in emails to avoid spam filters or enhance content appearance.


## Requirements
Python 3.6 or higher

## Setup


Install the required Python packages:


pip install -r requirements.txt


Create a recipients.txt file and list the email or phone numbers of targets, each on a separate line.


Change the config.json to include your smtp information:


{
    "SMTP_USERNAME": "your_smtp_username",
    "SMTP_PASSWORD": "your_smtp_password",
    "SMTP_SERVER": "your_smtp_server",
    "SMTP_PORT": 587
}

Note: The SMTP_PORT value may vary depending on your SMTP server's configuration.

Usage
Run the esender.py script to start the command-line interface:

python esender.py

Follow the on-screen instructions to choose between email and SMS sendouts and provide the required information when prompted.

## Disclaimer
This script is intended for ethical and legal use only. Do not use it for spamming or any malicious activities. The author is not responsible for any misuse of this script.

## Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve the script.

[list of sms gateways for mobile spamming](https://en.wikipedia.org/wiki/SMS_gateway)
