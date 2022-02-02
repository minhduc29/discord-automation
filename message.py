from datetime import datetime
from pyautogui import write, press


def send_message(msg):
    """Send messages to text channel"""
    write(msg)
    press('enter')
    log(msg)


def log(msg):
    """Msg log"""
    t = datetime.now().strftime('%H:%M:%S')
    print(f'[{t}] MESSAGE: {msg}')
