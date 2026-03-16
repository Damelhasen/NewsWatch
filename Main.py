import requests 
import time
import json 
import os
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (posix)
    else:
        _ = os.system('clear')

def data_grabber(query:str):
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {"query": query,
        "mode": "artlist",
        "format": "json",
        "timespan": "7d",
        "maxrecords": 10}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        for article in data["articles"]:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Date: {article['seendate']}")
            print("-" * 40)
        return data

    elif response.status_code == 429:
        print(f"Error: {response.status_code}")
        print("Rate limit exceeded. Waiting before retrying...")  # Wait for 60 seconds before retrying
        time.sleep(60)
        print("Retrying...")
        return data_grabber(query)
    else:
        print(f"Error: {response.status_code}")
        return None
   
def main():
    lookup_query = str(input("Enter a search query: "))
    clear_screen()
    data_grabber(lookup_query)


if __name__ == "__main__":
    main()
