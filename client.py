#   OSU CS361 Assignment 7 by John Kim
#   ZeroMQ per https://zeromq.org/get-started/
#   Client(sender) in Python
#   Connects REQ socket to tcp://localhost:5555
#   Sends message to server, expects confirmation reply back

import zmq

context = zmq.Context()

# Socket to talk to server
print("Connecting to server(receiver) …")
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

# send a message
input = 12 # Integer from my partner <------------------- User Input
data = str(input) # change intger into string
socket.send_string(data)
print("[***] Sent integer to server(receiver): ", data)

# Get the reply with output
message = socket.recv()

# Change string into array
string = str(message)[2:-1]
output = string.split(',')
for i in range(input):
    output[i] = int(output[i]) # Array <------------------- Output from Server
print("[***] Received random array back from server(receiver): ", output)