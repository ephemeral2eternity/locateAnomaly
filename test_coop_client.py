## Testing the cooperative client in CFD System
# test_coop_client.py
# Chen Wang, Feb. 18, 2015
# chenw@andrew.cmu.edu
import random
import sys
import logging
import shutil
from coop_client import *
from test_utils import *
from attach_cache_agent import *

### Get client name and attache to the closest cache agent
client_name = getMyName()
cache_agent = attach_cache_agent()

if not cache_agent:
	reportErrorQoE(client_name)
	sys.exit()

## Config logging level
logging.basicConfig(filename='agens_' + client_name + '.log', level=logging.INFO)

## Try several times to confirm the lose connection of client agent
# cache_agent = attach_cache_agent(client_name)

print "Client ", client_name, " is connecting to cache agent : ", cache_agent['name']
cache_agent_ip = cache_agent['ip']

## Report cache agent to the centralized controller cmu-agens
update_cache_agent(client_name, cache_agent['name'])

## Get the CDF of Zipf distribution
N = 10
p = 0.1
zipf_cdf = getZipfCDF(N, p)

### Get the server to start streaming
for i in range(1):
	# Randomly select a video to stream
	vidNum = 1000
	video_id = weighted_choice(zipf_cdf)

	## Testing rtt based server selection
	method = 'nocoop'
	waitRandom(1, 100)
	coop_agent(cache_agent, video_id, method)
