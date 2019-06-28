COWSAY_TEMPLATE = r"""
##{speech_bubble_border}##
# {msg} #
##{speech_bubble_border}##
       \
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||"""


def cowsay(msg: str, print_end="\n\n") -> None:
    """
    Print ASCII picture of a cow saying something provided by the user.

    Refers to the true and original: https://en.wikipedia.org/wiki/Cowsay
    """
    speech_bubble_border = len(msg) * "#"
    formatted_cowsay_str = COWSAY_TEMPLATE.format(
        msg=msg, speech_bubble_border=speech_bubble_border
    )
    print(formatted_cowsay_str, end=print_end)


INTERVALS = (("minutes", 60), ("seconds", 1))


def humanize_seconds(seconds: float) -> str:
    """Seconds formatted for humans."""
    result = []
    seconds_rounded = int(round(seconds))

    if seconds_rounded == 0:
        return "less than or equal 0.5 seconds"

    for name, count in INTERVALS:
        value = seconds_rounded // count
        if value:
            seconds_rounded -= value * count
            if value == 1:
                name = name.rstrip("s")
            result.append(f"{value} {name}")

    return ", ".join(result)
