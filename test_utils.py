## Some utilities for testing script
# Chen Wang, Feb. 18, 2014
# chenw@andrew.cmu.edu
## test_utils.py

import random
import time
import math
import urllib2
from attach_cache_agent import *

## ======================================================================== 
# Wait for a random period of time
# @input : minPeriod ---- The minimum time period to wait
#		   maxPeriod ---- The maximum time period to wait
## ======================================================================== 
def waitRandom(minPeriod, maxPeriod):
	## Sleeping a random interval before starting the client agent
	waitingTime = random.randint(minPeriod, maxPeriod)
	print "Before running DASH on the client agent, sleep %d seconds!" % waitingTime
	time.sleep(waitingTime)

## ======================================================================== 
# Generate the cumulative Distribution Function for Zipf's distribution
# @input : N ---- The number of videos
#		   p ---- The parameter to compute Zipf distribution
# @return : the cumulative distribution function of Zipf
## ======================================================================== 
def getZipfCDF(N, p):
	zipf_cdf = []
	sum_p = 0
	for i in range(N):
		p = math.pow(i + 1, -p)
		sum_p = sum_p + p
		zipf_cdf.append(sum_p)


	zipf_cdf = [x/sum_p for x in zipf_cdf]
	return zipf_cdf

## ======================================================================== 
# Weighted choice a number from zero to the length of dist_cdf
# @input : dist_cdf ---- The cumulative distribution for the weighted choice
# @return : the number choiced from 0 to len(dist_cdf)
## ======================================================================== 
def weighted_choice(dist_pdf):
	rnd = random.random()
	for i, total in enumerate(dist_pdf, start=1):
		if rnd < total:
			return i

## ======================================================================== 
# Update the client's cache agent to cmu-agens
# @input : client ---- The client name
#		   cache_agent ---- The cache agent the client is connecting to
## ========================================================================
def update_cache_agent(client, cache_agent):
	update_url = "http://104.197.6.6:8000/cacheagent/add?client=%s&cache_agent=%s" % (client, cache_agent)
	try:
		rsp = urllib2.urlopen(update_url)
		print "Update cache agent for client :", client, " and its cache agent is ", cache_agent, " successfully!"
	except:
		print "Failed to update cache agent for client ", client, " to cmu-agens server!"

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