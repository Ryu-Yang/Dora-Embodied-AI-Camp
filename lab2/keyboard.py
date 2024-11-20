import pyarrow as pa
from dora import Node
import time
import cv2


node = Node()

for event in node:
    if event["type"] == "INPUT":
        key = cv2.waitKey(1)
        if key == 27:       #按Esc键退出
            break


# with keyboard.Events() as events:
#     while True:
#         event = events.get(1.0)
#         if event is not None and isinstance(event, Events.Press):
#             if hasattr(event.key, "char"):
#                 if event.key.char == "p":
#                     break
#                 if event.key.char == "z":
#                     while True:
#                         node.send_output("char", pa.array(["b"]))
#                         time.sleep(5)
#                 if event.key.char is not None:
#                     node.send_output("char", pa.array([event.key.char]))


# with keyboard.Events() as events:
#     while True:
#         event = events.get(1.0)
#         if event is not None and isinstance(event, Events.Press):
#             if hasattr(event.key, "char"):
#                 if event.key.char == "p":
#                     break
#                 if event.key.char == "z":
#                     while True:
#                         node.send_output("char", pa.array(["b"]))
#                         time.sleep(5)
#                 if event.key.char is not None:
#                     node.send_output("char", pa.array([event.key.char]))
