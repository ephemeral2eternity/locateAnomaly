## cfds_logger_utils.py
# All communications with cfds-logger for fault detection
# Chen Wang, chenw@andrew.cmu.edu, July, 23, 2015
import urllib2

## ======================================================================== 
# Update the client's hostname and ip address to the centralized cfds-logger
# @input : client ---- The client name
## ========================================================================
def update_cfds_logger(client):
	update_url = "http://173.255.112.124:8000/monitor/add?%s" % client
	try:
		rsp = urllib2.urlopen(update_url)
		print "Successfully update the client name: ", client, " to the centralized cfds-logger!"
	except:
		print "Failed to update client ", client, " to the centralized cfds-logger server!"