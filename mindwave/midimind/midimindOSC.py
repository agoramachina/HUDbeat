from pythonosc import udp_client
from pythonosc import osc_message_builder
from pythonosc.udp_client import SimpleUDPClient


ip = '127.0.0.1'
port = 57121


sender = udp_client.SimpleUDPClient(ip, port)
sender.send_message('/trigger/prophet', [70, 100, 8])

#client = SimpleUDPClient(ip, port) # Create client
#client.send_message(ip, 123) # Send float message
#client.send_message(1p, [1, 2., "hello"]) # Send message with int, float and string
