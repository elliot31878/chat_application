"""
---- this class created at (Sunday , May , 5/6/2020) by MR.ROBOT 

---- this class for create  color in consol  (0 - 0)
"""

from colorama import (
    Fore, Back, init as colorma_init
)


class Colors:
    colorma_init(autoreset=True)

    FORE_GREEN = Fore.GREEN
    FORE_RED = Fore.RED
    FORE_YELLOW = Fore.YELLOW
    FORE_CYAN = Fore.CYAN
    FROE_MAGENTA = Fore.MAGENTA
    FORE_BLUE = Fore.BLUE
    FORE_WHITE = Fore.WHITE

    BACK_GREEN = Back.GREEN
    BACK_YELLOW = Back.YELLOW
    BACK_CYAN = Back.CYAN
    BACK_BLUE = Back.BLUE
