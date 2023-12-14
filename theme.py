import shutil

# ... Center
def centerText(text, border_char2='_'):
    """Center text"""
    screen_width2, _ = shutil.get_terminal_size()
    border2 = border_char2 * screen_width2
    centerTxt = f"{text.center(screen_width2)}\n"
    return centerTxt
# ... Center_with_Border
def center_text_with_border(text, border_char='*'):
    """Centers the text and adds a border based on screen size."""
    screen_width, _ = shutil.get_terminal_size()
    border = border_char * screen_width
    centered_text_wB = f"{border}\n{text.center(screen_width)}\n{border}"
    return centered_text_wB

# ... Center With Bottom Border
def centerText_Bottom_border(text, border_char2='_'):
    """Center text"""
    screen_width2, _ = shutil.get_terminal_size()
    border2 = border_char2 * screen_width2
    centerTxt_bB = f"\n{text.center(screen_width2)}\n{border2}"
    return centerTxt_bB