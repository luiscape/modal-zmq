from dataclasses import dataclass

import modal
import cloudpickle

image = (
    modal.Image.debian_slim()
    .pip_install("zmq", "cloudpickle")
    .add_local_python_source("common")
)
app = modal.App(image=image)


@dataclass
class Message:
    data: str
    processed: bool = False

    def serialize(self):
        return cloudpickle.dumps(self)

    @staticmethod
    def deserialize(data: bytes) -> "Message":
        return cloudpickle.loads(data)
