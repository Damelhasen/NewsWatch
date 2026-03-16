import requests 
import time
import json 
def clear_screen():
    print("\033[H\033[J", end="")

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

    elif response.status_code == 429:
        print(f"Error: {response.status_code}")
        print("Rate limit exceeded. Waiting before retrying...")  # Wait for 60 seconds before retrying
        time.sleep(60)
        print("Retrying...")
        return data_grabber(query)
    else:
        print(f"Error: {response.status_code}")
        return None
   
print(data_grabber("Iran"))
