#!/usr/bin/env python3
import sys
from kitty.boss import Boss
from kitty.fast_data_types import Screen

def main(args):
    answer = input("Enter something: ")
    return answer

def handle_result(args, answer, target_window_id, boss: Boss):
    w = boss.window_id_map[target_window_id]
    w.paste_text(f"You said: {answer}\n")

