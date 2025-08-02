#!/usr/bin/env python3

import sys
from kitty.boss import Boss
def main(args: list[str]) -> str:
    ans = input("Enter some text: ")

    # whatever this function returns will be available inside handle_result
    return ans

def handle_result(args: list[str], ans: str, target_window_id: int, boss: Boss) -> None:
    # get the kitty window into which to paste the text
    w = boss.window_id_map.get(target_window_id)
    if w is not None:
        w.paste_text(ans)
