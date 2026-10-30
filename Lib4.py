try:
    from colorama import Fore, Style
    COLOR = True
except ImportError:
    COLOR = False

print(Fore.GREEN + "ok" + Style.RESET_ALL if COLOR else "ok")