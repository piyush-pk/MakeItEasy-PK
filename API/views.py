import requests, json, base64
from django.shortcuts import render, HttpResponse



# views here.
def home(request):
    if request.method == "POST":
        id = dict(request.POST)['yt-link'][0].split("=")[1]
        url = "https://ytstream-download-youtube-videos.p.rapidapi.com/dl"
        querystring = {"id": id[:11]}
        headers = {
            'x-rapidapi-host': "ytstream-download-youtube-videos.p.rapidapi.com",
            'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
            }
        response = requests.request("GET", url, headers=headers, params=querystring).json()
        items = []
        # Mp3 APi
        url2 = "https://youtube-mp36.p.rapidapi.com/dl"
        querystring2 = {"id":id}
        headers2 = {
            'x-rapidapi-host': "youtube-mp36.p.rapidapi.com",
            'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
            }
        mp3 = requests.request("GET", url2, headers=headers2, params=querystring2).json()

        for name in response['link']:
            # print(name)
            for val in response['link'][name]:
                # if val.find("video/mp4") != -1:
                if val.find('video/mp4;') != -1 :
                   items.append(response['link'][name])
        return render(request, "index.html",{'response': response, 'items': items, 'mp3':mp3})
    return render(request, "index.html")

def yt_ss(request):
    if request.method == "POST":
        id = dict(request.POST)['ytlink'][0].split("=")[1]
        seconds = dict(request.POST)['seconds'][0]
        url = "https://youtube-screenshot1.p.rapidapi.com/frames/"

        querystring = {"seconds":seconds,"youtube_id": id[:11]}

        headers = {
            'x-rapidapi-host': "youtube-screenshot1.p.rapidapi.com",
            'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).content
        # print(response)
        # file = base64.b64encode(response)
        file = open("static/img/temp.png", "wb").write(response)
        return render(request, "yt_screenshot.html")
    return render(request, "yt_screenshot.html")

# def ip(request):
#     return render(request, "ip.html")

# def seo(request):
#     if request.method == "POST":
#         name = request.POST['seo']
#         url = "https://canssens-seo-extraction-v1.p.rapidapi.com/seo/api/"
#         payload = f"url={name}"
#         headers = {
#         'content-type': "application/x-www-form-urlencoded",
#         'x-rapidapi-host': "canssens-seo-extraction-v1.p.rapidapi.com",
#         'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
#         }
#         response = requests.request("POST", url, data=payload, headers=headers).json()
#         return render(request, "seo.html", {'response': response})
#     return render(request, "seo.html")

def movie(request):
    if request.method == "POST":
        name = dict(request.POST)['movie'][0]
        url = f"http://www.omdbapi.com/?s={name}&apikey=a2a7bdb5"
        response = requests.get(url = url).json()
        # print(response)
        return render(request, "movie.html", {'response': response})
    return render(request, "movie.html")

# def web_ss(request):
#     if request.method == "POST":
#         web = request.POST['web']
#         url = "https://zmokhtar-thum-io-website-screenshot-generator-v1.p.rapidapi.com/get/width/320/http://www.facebook.com/"

#         headers = {
#             'x-rapidapi-host': "zmokhtar-thum-io-website-screenshot-generator-v1.p.rapidapi.com",
#             'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
#             }
#         response = requests.get(url = url, headers=headers).content
#         print(response)
#         # print(web)
#     return render(request, "web_ss.html")

def media(request):
    if request.method == "POST":
        link = dict(request.POST)['link'][0]
        url = "https://all-social-media-video-downloader.p.rapidapi.com/"

        payload = f"url={link}"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-host': "all-social-media-video-downloader.p.rapidapi.com",
            'x-rapidapi-key': "02e975b74bmsh1a59df51080dfcep16358ejsnfe01fab1ec6a"
            }
        response = requests.request("POST", url, data=payload, headers=headers).json()
        return render(request, "media_downloader.html", {'response': response})
    return render(request, "media_downloader.html")

# def call(request):
#     # if request.method == "POST":
#     #     # print(dict(request.POST)['yt-link'][0])
#     return render(request, "call.html")



