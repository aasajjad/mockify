import pandas as pd

def spongebob_text(text):
    """
    Converts text to alternating capitalization to emulate a mocking tone.
    """
    return ''.join(char.upper() if i % 2 else char.lower() for i, char in enumerate(text))

def top_bottom_text(top_text="TOP TEXT", bottom_text="BOTTOM TEXT"):
    """
    Generates a meme text in upper case with top and bottom text.
    """
    return f"{top_text.upper()}\n\n{bottom_text.upper()}"

