# evernote-example
A set of scripts for working with the Evernote service via the API.

## How to install
Cloning project in your local computer:
```bash
git clone https://github.com/clownkill/evernote-example
```
Python 2.7 should be installed. Then use pip to install dependencies:
```bash
pip install -r requirements.txt
```

## Environment variables
Create `.env` file and put variables:
```
EVERNOTE_CONSUMER_KEY=[KEY]
EVERNOTE_CONSUMER_SECRET=[SECRET]
EVERNOTE_PERSONAL_TOKEN=[TOKEN]
JOURNAL_TEMPLATE_NOTE_GUID=[GUID]
JOURNAL_NOTEBOOK_GUID=[GUID]
INBOX_NOTEBOOK_GUID=[GUID]
```
Where:
* EVERNOTE_CONSUMER_KEY - your consumer key, you need to get it when registering on [dev.evernote.com](https://dev.evernote.com/#apikey)
* EVERNOTE_CONSUMER_SECRET - your consumer secret, you need to get it when registering on [dev.evernote.com](https://dev.evernote.com/#apikey)
* EVERNOTE_PERSONAL_TOKEN - your developer key, you need to get it on the evernote website [evernote.com](https://www.evernote.com/api/DeveloperToken.action)
* JOURNAL_TEMPLATE_NOTE_GUID - The GUID of the note, which will be used as a template in the future.
* JOURNAL_NOTEBOOK_GUID - Notepad GUID for notes that are generated automatically.
* INBOX_NOTEBOOK_GUID - The GUID of the notepad that is the inbox.

## Script description
### list_notebooks.py
The script makes a request to the Evernote API and outputs to the console a 
list of all notebooks (GUID and title) stored in the account.

### dump_inbox.py
Displays a list of notes that are stored in a notepad - inbox. The notepad GUID `INBOX_NOTEBOOK_GUID` is stored in `.env`.
By default, the console displays the last 10 notes. 
When running the script, it can be passed the number of notes required for output using the argument:
```python dump_inbox.py [number of notes]```

### add_note2journal.py
Creates an entry using the `JOURNAL_TEMPLATE_NAME_GUID` template and saves it in the notebook specified in `JOURNAL_NOTEBOOK_GUIDE`.

The template header should contain places to insert the date and day of the week, for example `{date}--{dow}`. 
By default, the current system date and time are inserted into the header. 
If it is necessary to set other date and time, they must be transmitted 
in ISO format (YYYY-MM-DD) as an argument when calling the script:  
`python add_note2journal.py [YYYY-MM-DD]`