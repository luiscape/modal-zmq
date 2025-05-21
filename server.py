import os
import zmq
from common import Message, app

import modal


@app.function()
def start_server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    region = os.getenv("MODAL_REGION")
    print(f"Server is running on {region=}...")

    with modal.forward(5555, unencrypted=True) as tunnel:
        origin, port = tunnel.tcp_socket
        print(f"Tunnel endpoint -> {origin}:{port}")
        while True:
            # Wait for next request from client.
            data = socket.recv()
            message = Message.deserialize(data)
            print(f"received message: {message}")

            # Update and send back to client.
            message = process_message.local(message)
            socket.send(message.serialize())


@app.function()
def process_message(message: Message) -> Message:
    message.processed = True
    return message


@app.local_entrypoint()
def main():
    start_server.remote()
