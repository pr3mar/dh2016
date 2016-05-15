# -*- coding: utf-8 -*-
"""
Created on Sat May 14 14:27:38 2016

@author: Angelina
"""

from instagram.client import InstagramAPI
import httplib2
import json
import sys

access_token = "2zU3V9W4OKaOgAbipKaoCw"
client_id = "a76df195ba2740b19e05d52d877fbe2b"
client_secret = "	ed0bbc17c42a4e3885d8da4afe26d903"

client_id_kokan = "1ff34d3853d14d02a197b23e6f7e85f1"
client_secret_kokan = "0065e78f50374f8caf04a3397fc4b4d1"

#api = InstagramAPI(client_id, client_secret)
#api = InstagramAPI(client_id_kokan, client_secret_kokan)

#popular_media, x = api.media_popular()
#print popular_media
#print x
#for media in popular_media:
#    print media.images['standard_resolution'].url

#userid = "1137702452"    
api = InstagramAPI(client_id = client_id, client_secret = client_secret)
api_comm = api.media_comments
print api_comm

#user_id = api.user_search('angelinatemelkovska')[0].id
#print user_id
    
#recent_media, next = api.user_recent_media(user_id="userid", count=10)

#for media in recent_media:
   #print media.text    
#    
#popular_media = api.media_popular(count=1)
#for media in popular_media:
#    print media.images['standard_resolution'].url
    


    
#https://api.instagram.com/oauth/authorize/?client_id=a76df195ba2740b19e05d52d877fbe2b&redirect_uri=http://www.google.com&response_type=code
    
#https://www.google.si/?gws_rd=cr,ssl&ei=2zU3V9W4OKaOgAbipKaoCw    