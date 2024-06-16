# Email Archiver

This project is a simple email archiving script using the Gmail API to remove specific emails from the inbox.

## Description

The Email Archiver script leverages the Gmail API to find and archive emails from specific senders. This script is useful for managing and organizing your Gmail inbox by programmatically moving selected emails out of the inbox.

## Getting Started

### Dependencies

- Python 3.x

Required libraries:

- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client

These can be installed using the following command:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```
## Installing
Clone the repository:
```bash
git clone https://github.com/yourusername/email-archiver.git
cd email-archiver
```
## Set up Google Cloud project:
Go to the Google Cloud Console.
Create a new project.
Enable the Gmail API for your project.
Create OAuth 2.0 credentials and download the credentials.json file.
Place the credentials.json file in the project directory.
## Prepare the environment:
Ensure all dependencies are installed as mentioned above.
Make sure Python 3.x is installed on your machine.
## Executing program
## Run the script:
Ensure you have the credentials.json file in the project directory.
Execute the script:
```bash
python email_archiver.py
```
## Help
#If you encounter issues, ensure:
You have an active internet connection.
Your credentials.json is correctly placed and valid.
The required libraries are installed.

## Authors
[Sathariels][nithilan.dev]

## License
This project is licensed under the MIT License - see the LICENSE.md file for details.




