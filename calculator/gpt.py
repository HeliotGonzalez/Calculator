from guizero import App, Text, TextBox, PushButton

def update_display(value):
    current = display.value
    display.value = current + str(value)

def clear_display():
    display.value = ""

def calculate():
    try:
        result = eval(display.value)
        display.value = str(result)
    except Exception as e:
        display.value = "Error"

# Create the main app window
app = App("Calculator", width=300, height=400)

# Display for showing the input and results
display = TextBox(app, width=20, height=2, text="", grid=[0, 0])

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

for (text, row, col) in buttons:
    if text == 'C':
        button = PushButton(app, text=text, grid=[col, row], command=clear_display)
    elif text == '=':
        button = PushButton(app, text=text, grid=[col, row], command=calculate)
    else:
        button = PushButton(app, text=text, grid=[col, row], command=lambda t=text: update_display(t))

# Start the app
app.display()
