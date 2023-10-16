# Move.nl House Listing Tracker
This repository contains a Python application, which consists of multiple data pipelines.
These pipelines following the extract, transform, and load designed principle.
An online housing platform functions as source information, as housing details are normalized, they are loaded into Airtable.

# Overview
The pipelines data resolves around house listenings.
It features pipelines to fullfill the following purpose:

## Overview extract 
A page is opened, containing an overview of house listings.
The listing platform accounts search criteria are applied.
During extraction, loading as many available listings as possible is attempted.
The little detail information of the listing is then loaded to Airtable.

## Details extract
Following the overview extract process, more details of the listing are gathered.
The listing details of unsold houses are updated if older then one week.
Common described detail from the listing page are extracted.
The detailed information is then added to the existing record in Airtable

# Set-up
Requires [https://www.python.org/](https://www.python.org/) (^3.10), [Poetry](https://python-poetry.org/), and [Selenium](https://www.selenium.dev/) installed onto the target installation system.
Futhermore credentials for the [Move.nl](https://move.nl/) housing platform, and [Airtable API](https://airtable.com/developers/web/api/introduction), are requisites.

## Installation
With Python installed on the target system, futher installation of Python dependencies are required.
Use the [Poetry](https://python-poetry.org/) Python dependency manager to install them
Execute the following snippet on a command line interface (CLI) after navigating to the repository base directory (the  folder this file is located in):

```
poetry install
```

Simple environment variable configuration is needed to interact with external systems.
Copy, or rename, the example environment configuration `example.env` to `.env`.
Execute the following snippet in the CLI while in the base repository (or use your prefered file explorer):

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

See `Makefile` for additional parameters
