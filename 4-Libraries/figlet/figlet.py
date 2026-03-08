import sys
from pyfiglet import Figlet
import random

figlet = Figlet()

if len(sys.argv) - 1 == 2:
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        if sys.argv[2] in figlet.getFonts():
            figlet.setFont(font=sys.argv[2])
            print(
                figlet.renderText(
                    input("Input text to be shown in your font of choice:\n")
                )
            )
        else:
            sys.exit()
else:
    figlet.setFont(font=random.choice(figlet.getFonts()))
    print(figlet.renderText(input("Input text to be shown in a random font\n")))
