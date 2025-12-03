# Program: language_switcher (Language Fixer app)
# written in Python
# Windows progran to convert gibberish text type in Hebrew to the corresponding English characters, and vice versa
# Default Hotkey to convert marked text: F9
# Version: 1.0
# Release date: 03-Dec-2025
# Powered by: NApps

import time
import sys
import pyperclip
import winsound # Required for the beep sound
from pynput import keyboard
from pynput.keyboard import Key, Controller

# --- Configuration ---
TRIGGER_KEY = Key.f9 

# --- Mapping Logic ---
ENG_TO_HEB = {
    'q': '/', 'w': "'", 'e': 'ק', 'r': 'ר', 't': 'א', 'y': 'ט', 'u': 'ו', 'i': 'ן', 'o': 'ם', 'p': 'פ', '[': ']', ']': '[',
    'a': 'ש', 's': 'ד', 'd': 'ג', 'f': 'כ', 'g': 'ע', 'h': 'י', 'j': 'ח', 'k': 'ל', 'l': 'ך', ';': 'ף', "'": ',',
    'z': 'ז', 'x': 'ס', 'c': 'ב', 'v': 'ה', 'b': 'נ', 'n': 'מ', 'm': 'צ', ',': 'ת', '.': 'ץ', '/': '.',
    'Q': '/', 'W': "'", 'E': 'ק', 'R': 'ר', 'T': 'א', 'Y': 'ט', 'U': 'ו', 'I': 'ן', 'O': 'ם', 'P': 'פ',
    'A': 'ש', 'S': 'ד', 'D': 'ג', 'F': 'כ', 'G': 'ע', 'H': 'י', 'J': 'ח', 'K': 'ל', 'L': 'ך',
    'Z': 'ז', 'X': 'ס', 'C': 'ב', 'V': 'ה', 'B': 'נ', 'N': 'מ', 'M': 'צ'
}

HEB_TO_ENG = {v: k for k, v in ENG_TO_HEB.items()}

def convert_text(text):
    if not text: return text
    heb_chars_count = sum(1 for char in text if char in HEB_TO_ENG)
    eng_chars_count = sum(1 for char in text if char in ENG_TO_HEB)
    
    # Logic: More Hebrew chars -> Convert to English
    if heb_chars_count > eng_chars_count:
        target_map = HEB_TO_ENG
        # Request 1: Convert to English and force Lowercase
        should_lower = True
    else:
        target_map = ENG_TO_HEB
        should_lower = False

    converted_chars = []
    for char in text:
        converted_chars.append(target_map.get(char, char))
    
    result = "".join(converted_chars)
    
    if should_lower:
        result = result.lower()
        
    return result

keyboard_controller = Controller()

def on_activate():
    try:
        keyboard_controller.release(TRIGGER_KEY)
        with keyboard_controller.pressed(Key.ctrl):
            keyboard_controller.tap('c')
        time.sleep(0.15)
        selected_text = pyperclip.paste()
        if not selected_text: return
        
        new_text = convert_text(selected_text)
        
        if new_text != selected_text:
            pyperclip.copy(new_text)
            
            # Request 2: Beep on successful conversion
            # Frequency: 1000Hz, Duration: 100ms
            winsound.Beep(1000, 100) 
            
            with keyboard_controller.pressed(Key.ctrl):
                keyboard_controller.tap('v')
    except Exception as e:
        print(f"Error: {e}")

def on_press(key):
    if key == TRIGGER_KEY:
        on_activate()

if __name__ == "__main__":
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()