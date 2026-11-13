
import json
import os
import urllib.request
import urllib.parse
import urllib.error
from dotenv import load_dotenv

load_dotenv()


def get_news(query):
    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        print("Error: API key not found. Check your .env file.")
        return

    params = {
        "q": query,
        "lang": "en",
        "country": "us",
        "max": 10,
        "apikey": api_key
    }

    url = "https://gnews.io/api/v4/search?" + urllib.parse.urlencode(params)

    try:
        with urllib.request.urlopen(url, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        articles = data.get("articles", [])

        if not articles:
            print("No news articles found for this search.")
            return

        print(f"\nNews results for: {query}\n")

        for i, article in enumerate(articles, start=1):
            print(f"\nArticle {i}")
            print("Title:", article.get("title", "No title"))
            print("Description:", article.get("description") or "No description")
            print("URL:", article.get("url", "No link"))
            print("-" * 50)

    except urllib.error.HTTPError as e:
        if e.code == 403:
            print("API access denied. Check your API plan and key.")
        elif e.code == 400:
            print("Invalid search request. Please try another keyword.")
        else:
            print("API error:", e.code)

    except urllib.error.URLError:
        print("Network error. Please check your internet connection.")

    except TimeoutError:
        print("Request timed out. Please try again.")

    except (ValueError, KeyError):
        print("Unable to process the news data.")


query = input("Enter a news topic: ").strip()

if query:
    get_news(query)
else:
    print("Search topic cannot be empty.")
