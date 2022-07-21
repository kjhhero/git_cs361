#   OSU CS361 Assignment 7 by John Kim
#   ZeroMQ per https://zeromq.org/get-started/
#   Server(receiver) in Python
#   Binds REP socket to tcp://*:5555
#   Expects expect from sender(client), replies for confirmation

import time
import zmq
import random

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

# Microservice
def ran_num_gen(int):
    int_str = ''
    int_str = int_str + ','.join(str(random.randint(0, int)) for i in range(int))
    return int_str

# Communication piping
while True:
    #  Wait for next request from client
    print('Waiting for messages. To exit press CTRL+C')
    message = socket.recv()

    message_int = int(message) # change string to integer
    print("[***] Received integer: ", message_int)
    random_num = ran_num_gen(message_int)
    print("[***] Generated random numbers : ", random_num)

    #  Do some 'work'
    time.sleep(1)

    #  Send reply back to client as string
    socket.send_string(random_num)