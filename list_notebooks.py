#!/usr/bin/env python 
from evernote.api.client import EvernoteClient

from config import Settings


if __name__ == '__main__':
    config = Settings()
    client = EvernoteClient(
        token=config.EVERNOTE_PERSONAL_TOKEN,
        sandbox=False
    )
    note_store = client.get_note_store()

    notebooks = note_store.listNotebooks()
    for notebook in notebooks:
        print(f'{notebook.guid} - {notebook.name}')
