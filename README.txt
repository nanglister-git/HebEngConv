Hebrew-English Text Switcher (Windows 11)

Project Overview

This tool runs in the background and allows you to toggle selected text between Hebrew and English characters using a hotkey. It fixes accidental typing in the wrong keyboard layout.

Files

language_switcher.py - The main Python script (runs the logic).

install_and_build.bat - The installer script (builds the EXE and sets up Startup).

How to Install

Ensure both files above are in the same folder.

Right-click install_and_build.bat and select Run as Administrator.

It will install Python requirements (pynput, pyperclip, etc.).

It will convert the Python script into a standalone .exe.

It will copy the program to %LOCALAPPDATA% to keep it safe.

It will create a shortcut in your Windows Startup folder.

Once the black window closes, the program is running!

How to Use

Highlight any text that was typed in the wrong language (e.g., "akuo" instead of "שלום").

Press F9 on your keyboard.

The text will automatically flip to the correct language.

Features

Auto-Detection: Automatically detects if the text is mostly Hebrew or English and flips it to the other.

Lowercase English: When converting from Hebrew to English, the result is forced to lowercase.

Audio Feedback: You will hear a short "Beep" sound when a conversion is successful.

Startup: Runs automatically when you restart Windows.

Troubleshooting

Program not working? Check if HebEngFixer.exe is running in Task Manager.

Want to uninstall? 1. Delete the shortcut in C:\Users\[YourName]\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup.
2. Delete the folder C:\Users\[YourName]\AppData\Local\HebEngFixer.