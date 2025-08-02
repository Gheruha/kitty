#!/usr/bin/env python3

'''
save_terminal_window kitten is made just for learning purposes.
It takes all the things on the current terminal window and paste them into a txt file.
The user must provide the absolute path - ex(~/Documents/buf.txt)
'''
import os
from kitty.boss import Boss


def main(args: list[str]) -> str:
    answer = input("Where to save: ")
    return answer


def handle_result(
    args: list[str], answer: str, target_window_id: int, boss: Boss
) -> None:
    w = boss.window_id_map.get(target_window_id)
    if not w:
        return

    # Getting all the text from the parent window
    resp = boss.call_remote_control(
        None, ("get-text", "--match", "state:parent_active", "--extent", "all")
    )
    buf = resp if isinstance(resp, str) else ""

    # Getting the path
    path = os.path.expanduser(answer)
    # Ensure that it ends with .txt
    if not path.lower().endswith(".txt"):
        path += ".txt"
    with open(path, "w") as file:
        file.write(buf)
