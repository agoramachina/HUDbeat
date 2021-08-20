from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

IP = "127.0.0.1"
PORT = 5000

def muse_handler(address, *args):
    """handle all muse data"""
    print(f"{address}: {args}")

def eeg_handler(address, *args):
    """handle raw eeg data"""
    print(f"{address}: {args}")

def battery_handler(address, *args):
    """handle battery data"""
    level, batt_voltage, adc_voltage, temp = args
    print(f"Battery level: {level}")

def blink_handler(address, *args):
    """handle blink data"""

    # Note: when the jaw stays clenched blink message is spammed

    # it seems to only send a 1 when a blink is detected
    # so no reason to do much to process the data
    print("Blink detected")

def jaw_handler(address, *args):
    """handle jaw clench data"""

    # it seems to only send a 1 when a clench is detected
    # so no reason to do much to process the data
    print("Jaw Clench detected")

def marker_handler(address, *args):
    """handle marker data"""

    # this didn't do anything for me.  Might be because I have
    # the S model
    print(f"{address}: {args}")

def default_handler(address, *args):
    print(f"DEFAULT {address}: {args}")

def get_dispatcher():
    dispatcher = Dispatcher()
    # dispatcher.map("/muse/batt", battery_handler)
    dispatcher.map("/muse/elements/blink", blink_handler)
    dispatcher.map("/muse/elements/jaw_clench", jaw_handler)
    # dispatcher.map("/Marker/*", marker_handler)
    
    # this will handle any unidentified messages if you would like
    # dispatcher.set_default_handler(default_handler)

    # use this dispatched to handle anythin muse
    # dispatcher.map("/muse/*", muse_handler)

    return dispatcher

    # TODO
    # dispatcher.map("/muse/*", muse_handler)
    # dispatcher.map("/muse/eeg", eeg_handler)
    # dispatcher.map("/muse/elements/delta_absolute", delta_absolute_handler)
    # dispatcher.map("/muse/elements/theta_absolute", theta_absolute_handler)
    # dispatcher.map("/muse/elements/alpha_absolute", alpha_absolute_handler)
    # dispatcher.map("/muse/elements/beta_absolute", beta_absolute_handler)
    # dispatcher.map("/muse/elements/gamma_absolute", gamma_absolute_handler)
    # dispatcher.map("/muse/elements/horseshoe", horseshoe_handler)
    # dispatcher.map("/muse/elements/touching_forehead", touching_forehead_handler)
    # dispatcher.map("/muse/gyro", gyro_handler)
    # dispatcher.map("/muse/acc", accel_handler)
    # dispatcher.set_default_handler(default_handler)


def start_blocking_server(ip, port):
    server = BlockingOSCUDPServer((ip, port), dispatcher)
    server.serve_forever()  # Blocks forever

if __name__ == '__main__':
    dispatcher = get_dispatcher()
    start_blocking_server(IP, PORT)
