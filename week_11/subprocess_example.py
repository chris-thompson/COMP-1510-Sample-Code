"""
The subprocess module lets us start other programs.

That's right. We can use our Python program to run other programs now. WOW!
"""

import subprocess
import time


def main():
    status = subprocess.Popen("/System/Applications/Chess.app/Contents/MacOS/Chess")
    print(status)
    time.sleep(3)
    status = subprocess.run(['/usr/local/bin/python3', 'webbrowser_example.py'])
    print(status)
    time.sleep(3)
    status = subprocess.run('/System/Applications/Calculator.app/Contents/MacOS/Calculator')
    print(status)
    status = subprocess.run("/System/Applications/Chess.app/Contents/MacOS/Chess")
    print(status)


if __name__ == "__main__":
    main()
