from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create a Figlet object with a specific font
f = Figlet(font='slant')

# Generate ASCII art
ascii_banner = f.renderText("Hello, World!")

# Add color to the ASCII art and print
colored_ascii_banner = Fore.GREEN + ascii_banner + Style.RESET_ALL
print(colored_ascii_banner)
