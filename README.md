# wikipedia-scraper
# 
[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


## 🏢 Description

Scraping data is often the first coding step of a data science project (meaning, the data collection) and you will likely come back to it in the future.

![scraping](https://media4.giphy.com/media/Xe02toxlUsztG7iQgb/giphy.gif?cid=ecf05e47lixeo6qe5y4ooabkh0hfdz0t1pio4h0qgbngjq0n&ep=v1_gifs_search&rid=giphy.gif&ct=g)


## 📦 Repo structure

Create a virtual environment using [venv](https://docs.python.org/3/library/venv.html)

```
.
├── src/
│   ├── scraper.py
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## 🛎️ Usage

1. Clone the repository to your local machine.


2.  First MVP (Notebook) `wikipedia_scraper.ipynb` notebook.
 This notebook contains hints on calling the API endpoint, handling cookies, and extracting text with `BeautifulSoup`.

Once ready, move on to the next step and integrate your code into functions, put it inside a `scraper.py` module.

To run the script, you can execute the `main.py` file from your command line:

    ```
    python main.py
    ```


3.  A `scraper.py` module contains: Wrapping all the codes into functions.

The object should contain at least these six attributes: 
- `base_url: str` containing the base url of the API (https://country-leaders.onrender.com)
- `country_endpoint: str` → `/countries` endpoint to get the list of supported countries
- `leaders_endpoint: str` → `/leaders` endpoint to get the list of leaders for a specific country
- `cookies_endpoint: str` → `/cookie` endpoint to get a valid cookie to query the API
- `leaders_data: dict` is a dictionary where you store the data you retrieve before saving it into the JSON file
- `cookie: object` is the cookie object used for the API calls

The object should contain at least these five methods:
- `refresh_cookie() -> object` returns a new cookie if the cookie has expired
- `get_countries() -> list` returns a list of the supported countries from the API
- `get_leaders(country: str) -> None` populates the `leader_data` object with the leaders of a country retrieved from the API
- `get_first_paragraph(wikipedia_url: str) -> str` returns the first paragraph (defined by the HTML tag `<p>`) with details about the leader
- `to_json_file(filepath: str) -> None` stores the data structure into a JSON file

## ⏱️ Timeline

This project took three days for completion.

## 📌 Personal Situation
This project was done as part of the AI Boocamp at BeCode.org. 



