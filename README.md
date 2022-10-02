# Python Test App

A simple Python app that does something.

Handy for testing CI pipelines.

## Requirements

Python 3.6+

## Setup

```bash
$ python -m venv venv
$ . venv/bin/activate
$ python -m pip install -r requirements.txt
```

## Run

```bash
$ flask run

$ curl http://localhost:5000/api/v1/hello
{"Hello":"World"}

$ curl -X POST http://localhost:5000/api/v1/hello \
-H 'Content-Type: application/json' -d '{\"Good\": \"Morning\"}'
{
  "Good": "Morning"
}
```
