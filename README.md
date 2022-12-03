# Secret Santas

Assigns Secret Santas to a group of people and notifies them via email.

## Usage

`USER` and `PASSWORD` environment variables must be set to access a Gmail account.

Make `santas.py` executable:

```sh
chmod u+x santas.py
```

Participants must be listed in the following format:

```json
{
    "participant_name": {
        "email": "participant@example.com",
        "excludes": ["other_participant_name"]
    }
}
```

The excludes list allows spouses/partners to be excluded from the candidate pool.

Email template can use [Python Template strings](https://docs.python.org/3/library/string.html#template-strings).

Run script:

```sh
./santas.py participants.json template.txt
```

