from dora import Node
import pyarrow as pa

node = Node()
for event in node:
    if event["type"] == "INPUT":
        # pylint: disable=fixme
        # TODO: Remove this after https://github.com/dora-rs/dora/pull/652
        while True:
            next_event = node.next(timeout=1)
            if next_event is not None and next_event["type"] == "INPUT":
                event = next_event
            else:
                break
# while True:
#     event = node.next(timeout=1)
#     node.send_output("data", pa.array([1, 2, 3, 4, 5]))
