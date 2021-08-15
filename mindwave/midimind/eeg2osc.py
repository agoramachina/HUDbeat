from oscpy.server import OSCThreadServer
from time import sleep

osc = OSCThreadServer()
sock = osc.listen(address='127.0.0.1'), port=7000, default=True))
#osc.bind(b'/muse/eeg'. eeg_callback)

sleep(1000)

osc.stop  # stop the default socket

