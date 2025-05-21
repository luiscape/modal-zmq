import sys
import time

import zmq
from common import Message


def zmq_query(address: str, n_messages: int = 10):
    context = zmq.Context()

    print(f"connecting to {address=}")
    soc = context.socket(zmq.REQ)
    soc.connect(f"tcp://{address}")

    soc.RCVTIMEO = 12 * 1000  # Timeout interval (in milliseconds)

    for i in range(n_messages):
        message = Message(data=f"message {i}")
        soc.send(message.serialize())

        # Handle timeout errors.
        start = time.perf_counter()
        try:
            response = soc.recv()
            message = Message.deserialize(response)
        except zmq.error.Again:
            print("Failed to receive message.")
            break

        print(f"got response in {(time.perf_counter() - start) * 1000:.2f}ms")
        print(message)


if __name__ == "__main__":
    n_messages = 10

    start = time.perf_counter()
    zmq_query(sys.argv[1], n_messages=n_messages)
    print(f"zmq_query total time: {time.perf_counter() - start:.3f}s")
