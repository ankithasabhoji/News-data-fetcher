# News Fetcher 

A simple Python application that fetches news articles based on user search keywords using the GNews API.

## Features
- Search news by keyword.
- Display article titles and descriptions.
- Show article links.
- Fetch multiple news articles.
- Handle API and network errors.

## Technologies
- Python
- GNews API
- urllib
- python-dotenv

## Setup
1. Install dependencies:
   `pip install -r requirements.txt`
2. Add your API key to a `.env` file:
   `GNEWS_API_KEY=your_api_key`
3. Run:
   `python news.py`

**Note:** A GNews API key is required.