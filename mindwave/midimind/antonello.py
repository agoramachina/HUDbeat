from oscpy.server import OSCThreadServer
from time import sleep

def eeg_callback(*values):
	print("got values: {}".format(values))

osc = OSCThreadServer()  # See sources for all the arguments
sock = osc.listen(address='127.0.0.1', port=7000, default=True)
osc.bind(b'/muse/eeg', eeg_callback)

sleep(1000)

osc.stop()  # Stop the default socket
 
osc.stop_all()  # Stop all sockets
 
# Here the server is still alive, one might call osc.listen() again
 
osc.terminate_server()  # Request the handler thread to stop looping
 
osc.join_server()  # Wait for the handler thread to finish pending tasks and exit