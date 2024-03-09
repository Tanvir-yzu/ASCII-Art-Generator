from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create a Figlet object with a specific font
f = Figlet(font='slant')

# Generate ASCII art with color
ascii_banner = f.renderText("Hello, World!")
print(Fore.GREEN + ascii_banner + Style.RESET_ALL)
