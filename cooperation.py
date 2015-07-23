## Fault Detection and Fault Tolerance via Client Cooperation
# Chen Wang, Jun. 17, 2015
# chenw@andrew.cmu.edu
## cooperation.py
import json
import urllib2

## ======================================================================== 
# Get a peer's latest QoE for cooperation
# @input: peer_ip ---- a peer client's ip
# @return: peer_latest_info --- the latest QoE info from the peer client
## ========================================================================
def get_peer_latest(peer_ip):
	peer_url = "http://%s:8717/latest" % peer_ip
	peer_latest_info = {}
	
	try:
		rsp = urllib2.urlopen(url)
		rsp_headers = rsp.info()
		peer_latest_info = json.loads(rsp_headers['Params'])
	except:
		print "Failed to connect to peer client", peer_ip
		pass

	return peer_latest_info

## ======================================================================== 
# Detect Faults in the VoD system
# @input: cur_qtype ---- the QoE value of current client.
# @return: peer_latest_info --- the latest QoE info from the peer client
## ========================================================================
def coop_fault_detection(qoe, pclient, vclient):
	fault_events = {}
	vclient_latest = get_peer_latest(vclient['ip'])
	pclient_latest = get_peer_latest(pclient['ip'])
	# common_router = get_closest_router()
	if qoe < 0:
		# Go through


	else if qoe < 2:

	else:

