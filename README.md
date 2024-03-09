
# ASCII Art Generator

## Description

This project is a simple Python application that generates ASCII art from text using the `pyfiglet` library. It also incorporates colorization using the `colorama` library to make the output more visually appealing. The application supports customization of the font and color of the ASCII art.

## Installation

To install the required libraries, run the following commands:

```
pip install pyfiglet
pip install colorama
```

## Usage

Here's a basic example of how to use the application:

```
from pyfiglet import Figlet
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Create a Figlet object with a specific font
f = Figlet(font='slant')

# Generate ASCII art with color
ascii_banner = f.renderText("Hello, World!")
print(Fore.GREEN + ascii_banner + Style.RESET_ALL)
```

## Customization

You can customize the font and color of the ASCII art by modifying the `Figlet` object and the `Fore` color in the `print` statement.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Output

```
    __  __     ____           _       __           __    ____
   / / / /__  / / /___       | |     / /___  _____/ /___/ / /
  / /_/ / _ \/ / / __ \      | | /| / / __ \/ ___/ / __  / /
 / __  /  __/ / / /_/ /      | |/ |/ / /_/ / /  / / /_/ /_/
/_/ /_/\___/_/_/\____( )     |__/|__/\____/_/  /_/\__,_(_)b
```