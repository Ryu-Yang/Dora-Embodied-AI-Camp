from dora import Node
import pyarrow as pa

node = Node()
for event in node:
    if event["type"] == "INPUT":
        while True:
            next_event = node.next(timeout=0.1)
            if next_event is not None and next_event["type"] == "INPUT":
                event = next_event
            else:
                break

