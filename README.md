# Low-latency communications with ZMQ in Modal

This repository demonstrates how to achieve low-latency communications
between a client and a server running in Modal. This uses ZMQ as a communication
mechanism and unencrypted [Modal Tunnels](https://modal.com/docs/guide/tunnels).
Messages are also serialized using [cloudpickle](https://github.com/cloudpipe/cloudpickle),
allowing for arbitrary data types to be pased between client and server. 

# Usage

Start server with:

```shell
$ modal run server.py
Server is running on region='us-phoenix-1'...
Tunnel endpoint -> r29.modal.host:46669
```

Copy the tunnel endpoint and then run client with:

```shell
$ python client.py r29.modal.host:46669
connecting to address='r22.modal.host:44579'
got response in 13.42ms
Message(data='message 0', processed=True)
got response in 1.11ms
Message(data='message 1', processed=True)
got response in 0.97ms
Message(data='message 2', processed=True)
got response in 0.92ms
Message(data='message 3', processed=True)
got response in 1.04ms
Message(data='message 4', processed=True)
got response in 0.98ms
Message(data='message 5', processed=True)
got response in 0.94ms
Message(data='message 6', processed=True)
got response in 0.94ms
Message(data='message 7', processed=True)
got response in 0.93ms
Message(data='message 8', processed=True)
got response in 0.92ms
Message(data='message 9', processed=True)
zmq_query total time: 0.023s
```

You can pin the region of the server to match where you're running your client
in order to get more predictable latency. 
