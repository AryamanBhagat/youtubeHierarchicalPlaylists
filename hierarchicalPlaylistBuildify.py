#run this file once to 
import networkx as nx
import matplotlib.pyplot as plt
from ytmusicapi import YTMusic
import json
#read playlistsGraph.csv and build a directed graph of playlists
g = nx.read_edgelist('playlistsGraph.csv', create_using=nx.DiGraph(), nodetype=str)
#print(nx.info(g))
#nx.draw(g)
#plt.show()

# TODO check if all playlists exist, if not then create new playlists


ytmusic = YTMusic('headers_auth.json')
library = ytmusic.get_library_playlists(limit = 100)

titles = [data['title'] for data in library]
#print(titles)

playlistDict ={titles[i]:library[i]['playlistId'] for i in range(len(library))}

#print(playlistDict)

def augmentPlaylist(node):
    #find list of IDs of songs on youtube
    #print(g.in_edges(node))
    #find get a list of songs from the bottom
    for x in [edges[0] for edges in g.in_edges(node)]:
        augmentPlaylist(x)
        ytmusic.edit_playlist(playlistDict[node], addPlaylistId=playlistDict[x])
    #add to original list
    #return the list       
#run hierarchify on playlists that do not have a parent.

roots = [node for node in g.nodes if g.out_degree(node) == 0]

for root in roots:
    print(root)
    augmentPlaylist(root)
