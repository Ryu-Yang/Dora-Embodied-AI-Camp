from dora import Node
import pyarrow as pa
from enum import Enum


PID_X = 0.0004
PID_Y = -0.0003

class Action(Enum):
    Xp      = ("arm Xp", "movec", [0.01, 0, 0, 0, 0, 0, 0.1])
    Xn      = ("arm Xn", "movec", [-0.01, 0, 0, 0, 0, 0, 0.1])
    Yp      = ("arm Yp", "movec", [0, 0.01, 0, 0, 0, 0, 0.1])
    Yn      = ("arm Yn", "movec", [0, -0.01, 0, 0, 0, 0, 0.1])
    Zp      = ("arm Zp", "movec", [0, 0, 0.01, 0, 0, 0, 0.1])
    Zn      = ("arm Zn", "movec", [0, 0, -0.01, 0, 0, 0, 0.1])
    take    = ("arm take", "claw", [0])
    put     = ("arm put", "claw", [100])

    save    = ("save", "save", [0])
    clear   = ("clear", "clear", [0])

    begin   = ("begin", "begin", [0])
    stop    = ("stop", "stop", [0])
    goto    = ("goto", "goto", [0])


node = Node()

for event in node:
    if event["type"] == "INPUT":
        if event["id"] == "text":
            text = event["value"][0].as_py()
            text = text.replace(".", "")
            text = text.replace(".", "")

                
            for action in Action:
                if action.value[0] in text:
                    node.send_output(action.value[1], pa.array(action.value[2]))
                    print(f"""recieved:{action.value[0]}""")

        if event["id"] == "error":
            [error_x, error_y] =  event["value"].tolist()
            move_error = [
                PID_Y*error_y,
                PID_X*error_x,
                0,
                0,
                0,
                0,
                0
            ]
            print(f"""move_error:{move_error}""")
            node.send_output("movec", pa.array(move_error))
