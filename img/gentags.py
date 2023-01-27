#!/usr/bin/env python3
import os

def main():
    for e in os.listdir("."):
        if e == "gentags.py":
            continue

        print(f"""<li class="splide__slide">
<img src="./img/{e}" width="70%">
</li>""")

if __name__ == "__main__":
    main()
