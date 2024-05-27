import sys
import os
from colorama import Fore, Style

# clear console screen
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')

# info
print(Fore.BLUE)
print("Hell Let Loose Artillery Calculator")
print("Ctrl-C to exit")
print("Loader bearing needs to be -50˚ for gunner to be centered")
print(Fore.CYAN)
print("A good guide to HLL Arty (made not by me): https://www.hell-let-loose-calculator.com/#/help")
print()

try:
    arg = input(
        Fore.WHITE + "Press \"s\" for Soviet Artillery (122mm Howitzer)" + "\nOr \"b\" for British Artillery (QF 25-Pounder): ")
except KeyboardInterrupt:
    print(Fore.MAGENTA + "\nExiting")
    sys.exit()

# calculate constants:
# x = meters (input), y = MIL (output)
# slope: m = y / x  ->  (y1 - y2) / (x1 - x2)
# intercept: y = mx + b  ->  y - mx = b
if arg == "s":  # soviet
    m = (800 - 1120) / (1600 - 100)  # using (1600, 800) and (100, 1120)
    b = 800 - m * 1600  # using (1600, 800)
    print(Fore.YELLOW + "Calculating for Soviet Artillery (122mm Howitzer)")
elif arg == "b":  # british
    m = (267 - 533) / (1600 - 100)  # using (1600, 267) and (100, 533)
    b = 267 - m * 1600 # using (1600, 267)
    print(Fore.YELLOW + "Calculating for British Artillery (QF 25-Pounder)")
else:  # germany & US
    m = (622 - 978) / (1600 - 100)  # using (1600, 622) and (100, 978)
    b = 622 - m * 1600  # using (1600, 622)
    print(Fore.YELLOW + "Calculating for US/Germany Artillery (150mm Howitzer)")

while True:
    try:
        x = int(input(Fore.WHITE + "Meters: "))
    except ValueError:
        print(Fore.RED + "Invalid input")
        sys.tracebacklimit = None  # Disable error messages
        continue
    except KeyboardInterrupt:
        print(Fore.MAGENTA + "\nExiting")
        sys.exit()

    if x < 100 or x > 1600:
        print(Fore.RED + "Target out of range")
        print(Fore.CYAN + "The artillery can only hit target between 100m and 1600m")
    else:
        y = int(m * x + b)
        print(Fore.GREEN + str(x) + " m = " + str(y) + " MIL")
