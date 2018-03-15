# A script to return and update meta data for youtube videos from Youtube API
"""
Created: Jan 2017
@author: shuang

"""
import urllib,json,codecs,sys
f = open('YT_list.txt','r')
f1 = codecs.open('yt_results_test3.tsv',encoding='utf-8',mode='w+')
key = 'xxxxxx'  #hide my API key
for line in f:
	list = line.rstrip('\r\n').split('\t')
	# part == snippet contains channelTitle and categoryID
	a = urllib.urlopen('https://www.googleapis.com/youtube/v3/videos?id='+line+'&part=snippet&key='+key)
	b = json.loads(a.read())
	try:
		list.append(b['items'][0]['snippet']['channelTitle'])
	except:
		list.append('')
	try:		
		list.append(b['items'][0]['snippet']['categoryId'])
	except:
		list.append('')	
	# part == statistics for likes
	a = urllib.urlopen('https://www.googleapis.com/youtube/v3/videos?id='+line+'&part=statistics&key='+key)
	b = json.loads(a.read())
	try:
		list.append(b['items'][0]['statistics']['likeCount'])
	except:
		list.append('')
	# part == contentDetails for duration		
	a = urllib.urlopen('https://www.googleapis.com/youtube/v3/videos?id='+line+'&part=contentDetails&key'+key)
	b = json.loads(a.read())
	try:
		list.append(b['items'][0]['contentDetails']['duration'])
	except:
		list.append('')		
	f1.write('\t'.join(list)+'\n')
f1.close()
f.close()