#run this file once to 
import networkx as nx
import matplotlib.pyplot as plt
#read playlistsGraph.csv and build a directed graph of playlists
g = nx.read_edgelist('playlistsGraph.csv', create_using=nx.DiGraph(), nodetype=str)
#print(nx.info(g))
nx.draw(g)
plt.show()

# TODO check if all playlists exist, if not then create new playlists

#run hierarchify on playlists that do not have a parent.

