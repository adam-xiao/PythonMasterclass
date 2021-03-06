# Some ANSI escape sequences for colours and effects
# Text on right of bracket are special commands
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'

# print(RED,"This will be in red")
# print("So will this")


def color_print(text: str, *effects: str) -> None:
    """
    Print `text using the ANSI sequences to change color, etc
    :param text: The text to print.
    :param effects: The effect we want. One of the constants defined
        at the stat of this module.
    """
    effect_string = "".join(effects)
    output_string = "{0}{1}{2}".format(effect_string, text, RESET)
    print(output_string)


color_print("Hello Yellow Bold", YELLOW, BOLD)
color_print("Hello Yellow Reversed", YELLOW, REVERSE)


print("hello")