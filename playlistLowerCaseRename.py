from ytmusicapi import YTMusic
import json


ytmusic = YTMusic('headers_auth.json')
library = ytmusic.get_library_playlists(limit = 100)



def replace(s, ch):
    new_str = []
    l = len(s)
      
    for i in range(len(s)):
        if (s[i] == ch and i != (l-1) and
           i != 0 and s[i + 1] != ch and s[i-1] != ch):
            new_str.append(s[i])
              
        elif s[i] == ch:
            if ((i != (l-1) and s[i + 1] == ch) and
               (i != 0 and s[i-1] != ch)):
                new_str.append(s[i])
                  
        else:
            new_str.append(s[i])
          
    return ("".join(i for i in new_str))
  
  
char = '_'
#print(replace(s, char))

def fixTitle(title):
    title = title.lower()
    title = title.replace('-', '_')
    title = title.replace(' ', '_')
    title = title.replace('/', '_')
    title = title.replace('\'', '_')
    title = title.replace('|', '_')
    title = title.replace('(', '_')
    title = title.replace(')', '_')
    
    if(title[0:2] != "x_"):
        title = "x_"+title
    return title


import json
userInfoFile = open("personalDetails.json","r")
userInfo = json.load(userInfoFile)

whiteListFile = open('/home/aryaman/youtubeHierchialPlaylists/whiteList.txt', 'r')
whiteList = whiteListFile.readlines()

for playlist in library:
    newTitle = replace(fixTitle(playlist["title"]), char)
    #print(newTitle)
    #print(playlist["playlistId"])
    playlist_complete_info = ytmusic.get_playlist(playlist['playlistId'])
    if playlist["playlistId"] not in whiteList:
        if(playlist_complete_info['author']['id'] == userInfo['author']['id']):
            print(newTitle)
            ytmusic.edit_playlist(playlist["playlistId"], title=newTitle)
    