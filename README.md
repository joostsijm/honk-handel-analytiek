# Housetrack
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
Requires Python (^3.10), Poetry, and Selenium installed onto the installation target system.
Futhermore, the housing platform, and Airtable API, credentials are requisites.

## Installation steps
Poetry dependency installation:

```
poetry install
```

Copy the example environment configuration:

```
cp example.env .env
```

Then edit the `.env` file accordingly with the credentials.

## Running the application
Start the application With the following commandt

```
poetry run python housetrack
```
