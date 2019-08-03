import random
import time

from yaspin import yaspin
from yaspin.compat import iteritems
from yaspin.constants import COLOR_MAP
from yaspin.spinners import Spinners


COLORS = (k for k, v in iteritems(COLOR_MAP) if v == "color")
HIGHLIGHTS = (k for k, v in iteritems(COLOR_MAP) if v == "on_color")


def any_spinner_you_like(message):
    
    params = [("simpleDotsScrolling", 5)]

    # Setup printing
    max_len = 45
    msg = message

    for name, period in params:
        spinner = getattr(Spinners, name)

        spaces_qty = max_len - len(name) - len(msg) - len(spinner.frames[0])
        text = "{0}{1}".format(" " * spaces_qty,msg)

        with yaspin(spinner, text=text, color="white",side="right"):
            time.sleep(period)


def colors_simple(sleep=0.7):
    # Setup printing
    max_len = 25
    msg = "[Colors]"

    with yaspin(Spinners.dots12) as sp:
        for color in COLORS:
            spaces_qty = max_len - len(color) - len(msg)
            text = "{0}{1}{2}".format(color, " " * spaces_qty, msg)

            sp.color = color
            sp.text = text
            time.sleep(sleep)


def color_highlights(sleep=0.5):
    # Setup printing
    max_len = 40
    msg = "[Color Highlights]"

    with yaspin(Spinners.bouncingBall) as sp:
        for highlight in HIGHLIGHTS:
            name = "On {0} color".format(highlight.split("_")[1])
            spaces_qty = max_len - len(name) - len(msg)
            text = "{0}{1}{2}".format(name, " " * spaces_qty, msg)

            sp.on_color = highlight
            sp.text = text

            time.sleep(sleep)


def color_attributes(sleep=0.8):
    descriptions = [
        "Bold white color",
        "Dark red color",
        "Underline green color",
        "Blink yellow color",
        "Reverse blue color",
        "Concealed magenta color",
    ]
    # Setup printing
    max_len = 42
    msg = "[Color Attributes]"

    with yaspin(Spinners.bouncingBall) as sp:
        for descr in descriptions:
            spaces_qty = max_len - len(descr) - len(msg)
            text = "{0}{1}{2}".format(descr, " " * spaces_qty, msg)

            attr, color, _ = descr.split()
            sp.attrs, sp.color = [attr.lower()], color
            sp.text = text

            time.sleep(sleep)


def color_craziness(sleep=1.3):
    descriptions = [
        "Bold underline reverse cyan color",
        "Dark blink concealed white color",
        "Underline red on_grey color",
        "Reversed green on_red color",
    ]

    def parse_attrs(description):
        """Parse attributes from text description."""
        attrs = []
        for word in description.split():
            attr = word.lower()
            sp = yaspin()
            try:
                getattr(sp, attr)
            except AttributeError:
                continue
            else:
                attrs.append(attr)
        return attrs

    # Setup printing
    max_len = 58
    msg = "[Color Craziness  ]"

    # New spinner instance should be created every iteration since
    # multiple simultaneous color attributes are supported. Hence,
    # updating attribute of the instance will add new attribute to
    # the existing list of previous attributes.
    for descr in descriptions:
        spaces_qty = max_len - len(descr) - len(msg)
        text = "{0}{1}{2}".format(descr, " " * spaces_qty, msg)

        with yaspin(Spinners.pong, text=text) as sp:
            # Apply all color attributes from description
            for attr in parse_attrs(descr):
                getattr(sp, attr)

            time.sleep(sleep)


def right_spinner(sleep=2):
    with yaspin(text="Right spinner", side="right", color="cyan") as sp:
        time.sleep(sleep)

        # Switch to left spinner
        sp.side = "left"
        sp.text = "Left spinner"

        time.sleep(sleep)


def reversed_spinner(sleep=1):
    with yaspin(text="Reversed spinner", reversal=True, color="cyan") as sp:
        time.sleep(sleep)

        sp.spinner = Spinners.line

        time.sleep(sleep)

        sp.text = "Enjoy!"
        sp.ok("*")


# def main():
#     any_spinner_you_like()
#     colors_simple()
#     color_highlights()
#     color_attributes()
#     color_craziness()
#     right_spinner()
#     reversed_spinner()


# if __name__ == "__main__":
#     main()


# any_spinner_you_like()