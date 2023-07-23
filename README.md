Esender
Esender is a Python script that allows you to send out emails and SMS messages to multiple recipients using a specified SMTP server. The script provides a simple command-line menu interface that lets you choose between email and SMS sendouts.

Esender Logo

Features
Email Sendouts: Send emails to multiple recipients using a specified SMTP server.
SMS Sendouts: Send SMS messages to multiple recipients using a specified SMTP server.
Email Letter Support: Choose to send emails with a pre-defined HTML letter or simple text content.
Email Validation (TODO): Validate email addresses to check if they are valid and active.
SMTP Configuration: Read SMTP configuration from a config.json file for easy setup.
UTF-8 Encoding (TODO): Include special characters and Unicode symbols in emails to avoid spam filters or enhance content appearance.

Requirements
Python 3.6 or higher
Setup
Clone the repository to your local machine:

bash
Copy code
git clone https://github.com/your-username/esender.git

Install the required Python packages:

Copy code
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

Copy code
python esender.py
Follow the on-screen instructions to choose between email and SMS sendouts and provide the required information when prompted.

Disclaimer
This script is intended for ethical and legal use only. Do not use it for spamming or any malicious activities. The author is not responsible for any misuse of this script.

Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to help improve the script.

Contact
If you have any questions or need assistance, feel free to contact the author:

Email: courted@xmpp.jp


Replace the placeholders like your-username, your_smtp_username, your_smtp_password, etc., with actual values and customize the content as needed. The README provides basic information about the script, how to set it up, use it, and gives appropriate credits to the author. Make sure to include appropriate links, logos, and contact details based on your preference.

[list of sms gateways for mobile spamming](https://en.wikipedia.org/wiki/SMS_gateway)
