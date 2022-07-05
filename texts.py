import colorama
from colorama import *

colorama.init(autoreset=True)

start_message = f"Hi there, what do you {Fore.RED}need{Style.RESET_ALL}?"
width_text = f"""
    {Fore.RED + "⬛ ⬛ ⬛"}{Style.RESET_ALL}
    ▭▭▭▭
    ⬛ ⬛ ⬛
    ▭▭▭▭
    ⬛ ⬛ ⬛
    ▭▭▭▭
    ⬛ ⬛ ⬛
    ▭▭▭▭
    ⬛ ⬛ ⬛
    ▭▭▭▭
    ⬛ ⬛ ⬛
    """

height_text = f"""
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    {Fore.RED + "▭"}{Style.RESET_ALL}▭▭▭
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    {Fore.RED + "▭"}{Style.RESET_ALL}▭▭▭
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    {Fore.RED + "▭"}{Style.RESET_ALL}▭▭▭
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    {Fore.RED + "▭"}{Style.RESET_ALL}▭▭▭
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    {Fore.RED + "▭"}{Style.RESET_ALL}▭▭▭
    {Fore.RED + "⬛ "}{Style.RESET_ALL}⬛ ⬛
    """

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
           'H', 'I', 'J', 'K', 'L', 'M', 'N',
           'O', 'P', 'Q', 'R', 'S', 'T', 'U',
           'V', 'W', 'X', 'Y', 'Z']

numbers = ["❶","❷","❸","❹","❺","❻","❼","❽",
           "❾","❿","⓫","⓬","⓭","⓮","⓯","⓰",
           "⓱","⓲","⓳","⓴"]