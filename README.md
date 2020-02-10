# airbnb-scraper

Small project to scrape Airbnb listings.

Specification

```
Please write some code that scrapes property name, property type (e.g Apartment), number of bedrooms, bathrooms and list of the amenities for the following 3 properties:

https://www.airbnb.co.uk/rooms/14531512?s=51
https://www.airbnb.co.uk/rooms/19278160?s=51
https://www.airbnb.co.uk/rooms/1939240?s=51
```

## Dependencies

The scraper uses Selenium to start a headless browser. On MacOS, ensure `geckodriver` is installed
```
brew install geckodriver
```

All other dependencies are in python, and the project uses Pipenv - https://pipenv.kennethreitz.org/en/latest/
Simply run `make install`


## How to run

`make run`


## Progress / Completion

:white_check_mark: Property Name

:grey_question: Property Type

:white_check_mark: No of Bedrooms

:white_check_mark: No of Bathrooms

:white_check_mark: List of Amenities



Two of the provided links had expired, so other links were chosen.
