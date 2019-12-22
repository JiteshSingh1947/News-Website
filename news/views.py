from django.http import HttpResponse
from django.shortcuts import render



from django.shortcuts import render 
from newsapi import NewsApiClient 

# Create your views here. 
def index(request): 
	
	newsapi = NewsApiClient(api_key ='e54654e4a5324069bbcb602b1ffd01ea') 
	top = newsapi.get_top_headlines(sources ='techcrunch,bbc-news,the-verge') 

	l = top['articles'] 
	desc =[] 
	news =[] 
	img =[] 
	url=[]
	for i in range(len(l)): 
		f = l[i] 
		news.append(f['title']) 
		desc.append(f['description']) 
		img.append(f['urlToImage']) 
		url.append(f['url'])
	mylist = zip(news, desc, img,url) 

	return render(request, 'index.html', context ={"mylist":mylist}) 
