# Move.nl House Listing Tracker
This repository contains a Python application that consists of multiple data pipelines.
These pipelines follow the extract, transform, and load design principle.
An online housing platform functions as a source of information, as housing details are normalized, they are loaded into Airtable.

# Overview
The pipelines' data resolves around house listening.
It features pipelines to fulfill the following purposes:

## Overview extract 
A page is opened, containing an overview of house listings.
The listing platform account search criteria are applied.
During extraction, loading as many available listings as possible is attempted.
The little details of the listing are then loaded into Airtable.

## Details extract
Following the overview extraction process, more details about the listing are gathered.
The listing details of unsold houses are updated if they are older than one week.
Commonly described details from the listing page are extracted.
The detailed information is then added to the existing record in Airtable.

# Set-up
Requires [https://www.python.org/](https://www.python.org/) (^3.10), [Poetry](https://python-poetry.org/), and [Selenium](https://www.selenium.dev/) installed onto the target installation system.
Furthermore credentials for the [Move.nl](https://move.nl/) housing platform and [Airtable API](https://airtable.com/developers/web/api/introduction) are requisites.

## Installation
With Python installed on the target system, further installation of Python dependencies is required.
Use the [Poetry](https://python-poetry.org/) Python dependency manager to install them.
Execute the following snippet on a command-line interface (CLI) after navigating to the repository base directory (the  folder this file is located in):

```
poetry install
```

A aimple environment variable configuration is needed for the application to connect to external systems.
Copy, or rename, the example environment configuration `example.env` to `.env`.
Execute the following snippet in the CLI while in the base repository (or use your preferred file explorer):

```
cp example.env .env
```

Then edit the `.env` file accordingly with the credentials.

```
# Username of move.nl account
MOVE_USERNAME=PLACEHOLDER
# Password of move.nl account
MOVE_PASSWORD=PLACEHOLDER

# Personal access token of Airtable API
AIRTABLE_TOKEN=PLACEHOLDER
# The Airtable base identicator where the data will be loaded
AIRTABLE_BASE=PLACEHOLDER
# Airtable table identicator in the base to hold loaded data
AIRTABLE_TABLE=PLACEHOLDER
```

## Running the application
After installation and configuration, run the application with the following command:

```
poetry run python housetrack
```

See `Makefile` for additional parameters.
