import requests
import json

API_KEY = "df0f5e4fa1b5d08996524e8014aaae19"
url = "https://www.understandingwar.org/backgrounder/russia-cautiously-optimistic-following-zelensky-trump-meeting"  # Підставте потрібну URL-адресу

response = requests.get("http://api.scraperapi.com", params={
    "api_key": API_KEY,
    "url": url,
})

if response.status_code == 200:
    print("successful page load!")


    result = {
        "url": url,
        "status_code": response.status_code,
        "content": response.text
    }

    with open("page2.json", "w", encoding="utf-8") as file:
        json.dump(result, file, ensure_ascii=False, indent=4)

    print("successful saving to file")
else:
    print(f" Error: {response.status_code}")
