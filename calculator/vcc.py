import os
import requests
import keyboard
from guizero import App, Text, PushButton, Box
from playsound import playsound
import update as us

class Calculator:
    def __init__(self):
        self.string = ""
        self.equation = ""
        self.characters = 0
        self.srv = None
        self.modded = False

        # Attempt to import custom mods
        try:
            import calculatorMod as mod
            self.modded = True
        except ImportError:
            print("No mod detected.")
            self.modded = False

        self.create_app()
        self.setup_hotkeys()
        self.check_updates()

        if self.modded:
            mod.shortcuts()
            print("Custom keyboard shortcuts activated.")
        else:
            print("Custom keyboard shortcuts failed to load.")

        print("Welcome to Very Cool Calculator (VCC), version 1.0")

    def create_app(self):
        """Creates and displays the calculator GUI."""
        self.app = App(title="Calculator", height=400, width=500)
        self.number_display = Text(self.app, text="0", size=24, align="top")

        # Define layout boxes
        command_box = Box(self.app, layout="grid", align="left", height=200, width=175)
        number_box = Box(self.app, layout="grid", align="left", height=200, width=175)
        operator_box = Box(self.app, layout="grid", align="right", height=200, width=175)

        # Command buttons configuration
        commands = [
            {"text": "AC", "command": self.ac, "grid": [0, 0]},
            {"text": "DEL", "command": self.delete, "grid": [0, 1]},
            {"text": "(", "command": lambda: self.input_symbol("("), "grid": [1, 0]},
            {"text": ")", "command": lambda: self.input_symbol(")"), "grid": [1, 1]},
        ]

        # Number buttons configuration
        numbers = [
            {"text": "1", "command": lambda: self.input_number("1"), "grid": [0, 0]},
            {"text": "2", "command": lambda: self.input_number("2"), "grid": [1, 0]},
            {"text": "3", "command": lambda: self.input_number("3"), "grid": [2, 0]},
            {"text": "4", "command": lambda: self.input_number("4"), "grid": [0, 1]},
            {"text": "5", "command": lambda: self.input_number("5"), "grid": [1, 1]},
            {"text": "6", "command": lambda: self.input_number("6"), "grid": [2, 1]},
            {"text": "7", "command": lambda: self.input_number("7"), "grid": [0, 2]},
            {"text": "8", "command": lambda: self.input_number("8"), "grid": [1, 2]},
            {"text": "9", "command": lambda: self.input_number("9"), "grid": [2, 2]},
            {"text": "0", "command": lambda: self.input_number("0"), "grid": [1, 3]},
            {"text": ".", "command": lambda: self.input_number("."), "grid": [2, 3]},
        ]

        # Operator buttons configuration
        operators = [
            {"text": "+", "command": self.plus, "grid": [0, 0]},
            {"text": "-", "command": self.minus, "grid": [1, 0]},
            {"text": "×", "command": self.times, "grid": [0, 1]},
            {"text": "÷", "command": self.divide, "grid": [1, 1]},
            {"text": "=", "command": self.equals, "grid": [0, 2]},
        ]

        # Create command buttons
        for btn in commands:
            PushButton(command_box, text=btn["text"], command=btn["command"], grid=btn["grid"])

        # Create number buttons
        for btn in numbers:
            PushButton(number_box, text=btn["text"], command=btn["command"], grid=btn["grid"])

        # Create operator buttons
        for btn in operators:
            PushButton(operator_box, text=btn["text"], command=btn["command"], grid=btn["grid"])

        self.app.display()

    def input_number(self, num):
        """Handles number and decimal point inputs."""
        if self.characters == 0 and num != ".":
            self.string = num
            self.equation = num
            self.characters = 1
        else:
            self.string += num
            self.equation += num
        self.update_display()

    def input_symbol(self, symbol):
        """Handles symbol inputs like brackets."""
        self.string += symbol
        self.equation += symbol
        self.characters = 1
        self.update_display()

    def ac(self):
        """Clears the current input."""
        self.string = ""
        self.equation = ""
        self.characters = 0
        self.update_display()

    def delete(self):
        """Deletes the last character from the input."""
        self.string = self.string[:-1]
        self.equation = self.equation[:-1]
        if not self.string:
            self.characters = 0
        self.update_display()

    def add_operator(self, display_op, eq_op):
        """Adds an operator to the input."""
        if self.characters == 0:
            self.display_error("Number required at the front")
        else:
            self.string += display_op
            self.equation += eq_op
            self.update_display()

    def plus(self):
        """Handles the plus operator."""
        self.add_operator("+", "+")

    def minus(self):
        """Handles the minus operator."""
        self.add_operator("-", "-")

    def times(self):
        """Handles the multiplication operator."""
        self.add_operator("×", "*")

    def divide(self):
        """Handles the division operator."""
        self.add_operator("÷", "/")

    def equals(self):
        """Evaluates the current equation."""
        try:
            result = eval(self.equation)
            self.string = str(result)
            self.equation = str(result)
            self.characters = 1
        except Exception:
            self.display_error("Invalid Syntax")
            self.characters = 0
        self.update_display()

    def display_error(self, message):
        """Displays an error message."""
        self.string = message
        self.equation = ""
        self.characters = 0
        self.update_display()

    def update_display(self):
        """Updates the display with the current string."""
        self.number_display.value = self.string if self.string else "0"

    def setup_hotkeys(self):
        """Sets up global hotkeys for calculator operations."""
        key_function_map = {
            '1': lambda: self.input_number("1"),
            '2': lambda: self.input_number("2"),
            '3': lambda: self.input_number("3"),
            '4': lambda: self.input_number("4"),
            '5': lambda: self.input_number("5"),
            '6': lambda: self.input_number("6"),
            '7': lambda: self.input_number("7"),
            '8': lambda: self.input_number("8"),
            '9': lambda: self.input_number("9"),
            '0': lambda: self.input_number("0"),
            '.': lambda: self.input_number("."),
            'shift+=': self.plus,
            'shift+8': self.times,
            'shift+9': lambda: self.input_symbol("("),
            'shift+0': lambda: self.input_symbol(")"),
            '/': self.divide,
            '+': self.plus,
            '-': self.minus,
            '*': self.times,
            'enter': self.equals,
            'backspace': self.delete,
            '(': lambda: self.input_symbol('('),
            ')': lambda: self.input_symbol(')'),
        }

        # Dynamically map letter keys to their functions
        for letter in 'abcdefghijklmnopqrstuvwxyz':
            key_function_map[letter] = lambda l=letter: self.handle_letter(l)

        for key, func in key_function_map.items():
            keyboard.add_hotkey(key, func)

    def handle_letter(self, letter):
        """Handles letter inputs by mapping them to predefined formulas."""
        file_path = f"vccData/{letter}"
        try:
            with open(file_path, "r") as f:
                formula = f.read()
                self.string += letter
                self.equation += formula
                self.characters = 1
        except FileNotFoundError:
            try:
                with open(file_path, "x") as f:
                    formula = input(f"Assign the letter '{letter}' to a number or equation: ")
                    f.write(formula)
                self.string += letter
                self.equation += formula
                self.characters = 1
            except Exception:
                self.display_error("Please refer to the terminal window.")
                self.characters = 0
        self.update_display()

    def check_updates(self):
        """Checks for updates by comparing local and remote versions."""
        try:
            with open('update.txt', 'r') as v:
                current_version = v.read().strip()
            os.remove("update.txt")
            response = requests.get(
                'https://raw.githubusercontent.com/thetiger21/Calculator/main/calculator/update.txt',
                auth=('user', 'pass')
            )
            response.raise_for_status()
            with open('update.txt', 'wb') as f:
                f.write(response.content)
            with open('update.txt', 'r') as vrs:
                new_version = vrs.read().strip()
            if current_version != new_version:
                us.update()
            else:
                print("No update available.")
        except Exception as e:
            print(f"Update check failed: {e}")

def main():
    Calculator()

if __name__ == "__main__":
    main()
