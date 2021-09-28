requests

url = "https://youtube-screenshot1.p.rapidapi.com/frames/"

querystring = {"seconds":"80","youtube_id":"yVBO6FJSYjs"}

headers = {
    'x-rapidapi-host': "youtube-screenshot1.p.rapidapi.com",
    'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)