import FreeSimpleGUI as sg

# Create GUI components
label = sg.Text("type is todo")
input_box = sg.Input(tooltip="enter todo here")
add_button = sg.Button("Add")

# Define the layout
layout = [[label], [input_box], [add_button]]

# Create the window
window = sg.Window('my todo app', layout)

# Event loop to keep the window open
while True:
    event, values = window.read()  # Read events and input values
    if event == sg.WINDOW_CLOSED:  # Check if the window is closed
        break  # Exit the loop

# Close the window when the loop ends
window.close()
