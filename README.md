# git_cs361

by John Kim for CS361 2022 Summer

Steps on how to request data from the microservice I implemented using ZeroMQ for my partner’s individual project which is flashcards for SAT vocabulary.
- STEP 0: Install ZeroMQ. follow these steps (https://pypi.org/project/pyzmq/), but in short there are only two commnad line excutions you need (Mac OS terminal)
  First command: brew install zeromq
  Secnid command: python -m pip install pyzmq
- STEP 1: My partner and I communicate for a time-window for me to keep my server.py running in my computer.
- STEP 2: During an agreed time-window, I will keep running server.py in my computer.
- STEP 3: My partner downloads client.py from this GitHub into his computer.
- STEP 4: My partner puts his desired integer number into the integer variable (for example: 12) called “input” in the client.py and save the client.py.
- STEP 5: My partner run client.py in command window such as “python client.py”
- STEP 6: My partner will see messages in command window like “Sent integer to server” and “Received random array (with total 12 random numbers) back from server” for communication confirmation.
- STEP 7: My partner will use the received an array of random numbers which is stored in a variable called “output” for his individual project which is flashcards for SAT vocabulary.

UML Sequence Diagram showing how to request and receive data from the microservice I implemented.

![cs361](https://user-images.githubusercontent.com/62677086/180116616-e8d5c70b-387d-47ce-b0cd-4d6fc9ee85f9.png)

