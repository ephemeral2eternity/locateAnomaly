## Some utilities for cooperative agents
# Chen Wang, Jun. 17, 2015
# chenw@andrew.cmu.edu
## coop_utils.py
import random
import time
import math
import os
import urllib2
from attach_cache_agent import *
from traceroute import *

## ======================================================================== 
# Connect the client to its closest cache agent
# @input : client ---- The client name
#		   cache_agent ---- The cache agent the client is connecting to
## ========================================================================
def connect_cache_agent(client, cache_agent, cache_agent_ip):
	update_url = "http://%s:8615/client/add?%s" % (cache_agent_ip, client)
	try:
		rsp = urllib2.urlopen(update_url)
		print rsp
		print "Connect client :", client, " to its cache agent ", cache_agent, " successfully!"
	except:
		print "Failed to connect client ", client, " to its cache_agent", cache_agent, "!"

#==========================================================================================
# Get Traceroutes to all available servers
#==========================================================================================
def get_all_routes():
	## Try several times before exit
	all_cache_agents = get_cache_agents()
	trial_num = 0
	while not all_cache_agents and trial_num < 10:
		all_cache_agents = get_cache_agents()
		trial_num = trial_num + 1

	all_srv_hops = dict()
	for srv in all_cache_agents.keys():
		srv_hops = traceroute(all_cache_agents[srv])
		all_srv_hops[all_cache_agents[srv]] = srv_hops

	return all_srv_hops

#==========================================================================================
# Read the client's latest QoE and streaming server address from temporary file
# Filename: ./dat/info
#==========================================================================================
def get_info():
	full_path = os.path.realpath(__file__)
	path, fn = os.path.split(full_path)

	## Read the server address and the video ID.
	filename = path + "/dat/info"
	fo = open(filename, "r")
	lines = fo.read().splitlines()
	srv = lines[0]
	video = lines[1]

	## Read the recent monitored QoE
	qoeFileName = path + "/dat/qoe"
	qoeFile = open(qoeFileName, "r")
	lines = qoeFile.read().splitlines()
	qoe = lines[0]

	info = dict()
	info['srv'] = srv
	info['qoe'] = float(qoe)
	info['video'] = video

	return info

#==========================================================================================
# Get the string of route info from all routes
# @input: srv ---- the server the client is streaming from
#         all_routes ---- all traceroute info from client to the streaming server, srv
# @return : the string of all hops in the route from the client to the streaming server
#==========================================================================================
def get_route_str(srv, all_routes):
	cur_route = all_routes[srv]

	cur_route_list = []
	for hop_id in cur_route.keys():
		cur_route_list.append(cur_route[hop_id]['Name'])

	cur_route_str = ', '.join(cur_route_list)
	return cur_route_str
