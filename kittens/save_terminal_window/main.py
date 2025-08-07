#!/usr/bin/env python3

"""
save_terminal_window kitten is made just for learning purposes.
It takes all the things on the current terminal window and paste them into a txt file.
The user can select where to save the file.
"""
import inspect
import os
from pathlib import Path

from kitty.boss import Boss


def main(args: list[str]) -> str:
    current = Path.home()
    while True:
        # 1) list children of 'current'
        visible_dirs = [
            p for p in current.iterdir() if p.is_dir() and not p.name.startswith(".")
        ]
        print(f"\n📂 {current}")
        for d in visible_dirs:
            print("📁", d.name)
        print("Type a subdirectory name to enter it, or 'q' to finish.")

        # 2) get the raw input
        choice = input("> ").strip()
        if choice == "q":
            break

        # 3) find the matching Path
        selected = next((p for p in visible_dirs if p.name == choice), None)
        if not selected:
            print(f"❌ No such directory: {choice}")
            continue

        # 4) descend
        current = selected

    filename = input("Enter the file name: ")
    print(f"{current}/{filename}")
    return f"{current}/{filename}"


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
    # Paste the text into the file
    with open(path, "w") as file:
        file.write(buf)
