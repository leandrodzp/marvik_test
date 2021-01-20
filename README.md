# Marvik API

## Description

This implements an API with an only enpoint in `/date` route accepting a `verbose` param **in the request body** and returning the actual date with format depending on `verbose` value.

- If `verbose` is false or missing the format will be `aaaa-mm-dd hh:ii:ss`.

- If `verbose` is true `aaaa-dd-mm` is the expected format.

## Instructions

1. To run the server export the FLASK_APP environment variable as follows: `export FLASK_APP=api`

2. Create your virtual env and install dependencies in `requirements.txt`

3. Run `flask run` to start the server
