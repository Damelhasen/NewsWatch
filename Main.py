import requests 
import time
import json 
import os

#######################Country->cordianates########################
COUNTRY_COORDS = {
    "Afghanistan": (33.9391, 67.7100), "Albania": (41.1533, 20.1683), "Algeria": (28.0339, 1.6596),
    "Andorra": (42.5063, 1.5218), "Angola": (-11.2027, 17.8739), "Argentina": (-38.4161, -63.6167),
    "Armenia": (40.0691, 45.0382), "Australia": (-25.2744, 133.7751), "Austria": (47.5162, 14.5501),
    "Azerbaijan": (40.1431, 47.5769), "Bahrain": (26.0275, 50.5500), "Bangladesh": (23.6850, 90.3563),
    "Belarus": (53.7098, 27.9534), "Belgium": (50.5039, 4.4699), "Belize": (17.1899, -88.4976),
    "Benin": (9.3077, 2.3158), "Bolivia": (-16.2902, -63.5887), "Bosnia and Herzegovina": (43.9159, 17.6791),
    "Brazil": (-14.2350, -51.9253), "Bulgaria": (42.7339, 25.4858), "Burkina Faso": (12.3641, -1.5275),
    "Burundi": (-3.3731, 29.9189), "Cambodia": (12.5657, 104.9910), "Cameroon": (3.8480, 11.5021),
    "Canada": (56.1304, -106.3468), "Chad": (15.4542, 18.7322), "Chile": (-35.6751, -71.5430),
    "China": (35.8617, 104.1954), "Colombia": (4.5709, -74.2973), "Croatia": (45.1000, 15.2000),
    "Cuba": (21.5218, -77.7812), "Cyprus": (35.1264, 33.4299), "Czech Republic": (49.8175, 15.4730),
    "Denmark": (56.2639, 9.5018), "Djibouti": (11.8251, 42.5903), "DR Congo": (-4.0383, 21.7587),
    "Ecuador": (-1.8312, -78.1834), "Egypt": (26.8206, 30.8025), "El Salvador": (13.7942, -88.8965),
    "Eritrea": (15.1794, 39.7823), "Estonia": (58.5953, 25.0136), "Ethiopia": (9.1450, 40.4897),
    "Finland": (61.9241, 25.7482), "France": (46.2276, 2.2137), "Gabon": (-0.8037, 11.6094),
    "Georgia": (42.3154, 43.3569), "Germany": (51.1657, 10.4515), "Ghana": (7.9465, -1.0232),
    "Greece": (39.0742, 21.8243), "Guatemala": (15.7835, -90.2308), "Guinea": (9.9456, -11.3247),
    "Haiti": (18.9712, -72.2852), "Honduras": (15.1999, -86.2419), "Hungary": (47.1625, 19.5033),
    "Iceland": (64.9631, -19.0208), "India": (20.5937, 78.9629), "Indonesia": (-0.7893, 113.9213),
    "Iran": (32.4279, 53.6880), "Iraq": (33.2232, 43.6793), "Ireland": (53.1424, -7.6921),
    "Israel": (31.0461, 34.8516), "Italy": (41.8719, 12.5674), "Ivory Coast": (7.5399, -5.5471),
    "Japan": (36.2048, 138.2529), "Jordan": (30.5852, 36.2384), "Kazakhstan": (48.0196, 66.9237),
    "Kenya": (-0.0236, 37.9062), "Kosovo": (42.6026, 20.9030), "Kuwait": (29.3117, 47.4818),
    "Kyrgyzstan": (41.2044, 74.7661), "Laos": (19.8563, 102.4955), "Latvia": (56.8796, 24.6032),
    "Lebanon": (33.8547, 35.8623), "Libya": (26.3351, 17.2283), "Lithuania": (55.1694, 23.8813),
    "Madagascar": (-18.7669, 46.8691), "Malawi": (-13.2543, 34.3015), "Malaysia": (4.2105, 101.9758),
    "Mali": (17.5707, -3.9962), "Malta": (35.9375, 14.3754), "Mauritania": (21.0079, -10.9408),
    "Mexico": (23.6345, -102.5528), "Moldova": (47.4116, 28.3699), "Mongolia": (46.8625, 103.8467),
    "Montenegro": (42.7087, 19.3744), "Morocco": (31.7917, -7.0926), "Mozambique": (-18.6657, 35.5296),
    "Myanmar": (21.9162, 95.9560), "Namibia": (-22.9576, 18.4904), "Nepal": (28.3949, 84.1240),
    "Netherlands": (52.1326, 5.2913), "New Zealand": (-40.9006, 174.8860), "Nicaragua": (12.8654, -85.2072),
    "Niger": (17.6078, 8.0817), "Nigeria": (9.0820, 8.6753), "North Korea": (40.3399, 127.5101),
    "Norway": (60.4720, 8.4689), "Oman": (21.4735, 55.9754), "Pakistan": (30.3753, 69.3451),
    "Palestine": (31.9522, 35.2332), "Panama": (8.5380, -80.7821), "Paraguay": (-23.4425, -58.4438),
    "Peru": (-9.1900, -75.0152), "Philippines": (12.8797, 121.7740), "Poland": (51.9194, 19.1451),
    "Portugal": (39.3999, -8.2245), "Qatar": (25.3548, 51.1839), "Romania": (45.9432, 24.9668),
    "Russia": (61.5240, 105.3188), "Rwanda": (-1.9403, 29.8739), "Saudi Arabia": (23.8859, 45.0792),
    "Senegal": (14.4974, -14.4524), "Serbia": (44.0165, 21.0059), "Sierra Leone": (8.4606, -11.7799),
    "Singapore": (1.3521, 103.8198), "Slovakia": (48.6690, 19.6990), "Slovenia": (46.1512, 14.9955),
    "Somalia": (5.1521, 46.1996), "South Africa": (-30.5595, 22.9375), "South Korea": (35.9078, 127.7669),
    "South Sudan": (6.8770, 31.3070), "Spain": (40.4637, -3.7492), "Sri Lanka": (7.8731, 80.7718),
    "Sudan": (12.8628, 30.2176), "Sweden": (60.1282, 18.6435), "Switzerland": (46.8182, 8.2275),
    "Syria": (34.8021, 38.9968), "Taiwan": (23.6978, 120.9605), "Tajikistan": (38.8610, 71.2761),
    "Tanzania": (-6.3690, 34.8888), "Thailand": (15.8700, 100.9925), "Tunisia": (33.8869, 9.5375),
    "Turkey": (38.9637, 35.2433), "Turkmenistan": (38.9697, 59.5563), "Uganda": (1.3733, 32.2903),
    "Ukraine": (48.3794, 31.1656), "United Arab Emirates": (23.4241, 53.8478), "United Kingdom": (55.3781, -3.4360),
    "United States": (37.0902, -95.7129), "Uruguay": (-32.5228, -55.7658), "Uzbekistan": (41.3775, 64.5853),
    "Venezuela": (6.4238, -66.5897), "Vietnam": (14.0583, 108.2772), "Yemen": (15.5527, 48.5164),
    "Zambia": (-13.1339, 27.8493), "Zimbabwe": (-19.0154, 29.1549),
}
#######################################################################
def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux (posix)
    else:
        _ = os.system('clear')

source_countries = {}

def data_grabber(query:str):
    url = "https://api.gdeltproject.org/api/v2/doc/doc"
    params = {"query": query,
        "mode": "artlist",
        "format": "json",
        "timespan": "7d",
        "maxrecords": 100}
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
       
       
        source_countries = {}
        data = response.json()
        for article in data["articles"]:
            print(f"Title: {article['title']}")
            print(f"URL: {article['url']}")
            print(f"Date: {article['seendate']}")
            print(article["sourcecountry"])
            if article["sourcecountry"] in source_countries:
                source_countries[article["sourcecountry"]] += 1
            else:
                source_countries[article["sourcecountry"]] = 1
            print("-" * 40)
        print(source_countries)
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
