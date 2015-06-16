#!/usr/bin/python
# Cooperative Client Agent in QoE based Anomaly Localization System
# coop_agent.py
# Chen Wang, chenw@cmu.edu
# Jun. 16, 2015
from attach_cache_agent import *
from test_utils import *

PORT = 8717

#==========================================================================================
# Get the route info to all servers
#==========================================================================================


#==========================================================================================
# Main Function of A Cooperative Agent
#==========================================================================================
def main(argv):
	### Get client name and attache to the closest cache agent
	client_name = getMyName()
	cache_agent = attach_cache_agent()

	## Connect client to its cache agent and update centralized manager
	print "Client ", client_name, " is connecting to cache agent : ", cache_agent['name']
	connect_cache_agent(client_name, cache_agent['name'], cache_agent['ip'])
	update_cache_agent(client_name, cache_agent['name'])

    #server = HTTPServer(('', PORT), MyHandler)
    #print 'started httpserver on port : ', str(PORT), ' .... '
    #server.serve_forever()

if __name__ == '__main__':
    main(sys.argv)
