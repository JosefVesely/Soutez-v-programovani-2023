# Documentation: https://www.pysimplegui.org/en/latest/
import PySimpleGUI as sg

def create_window():
    layout = [
        []
    ]
    return sg.Window("Title", layout)


window = create_window()

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break

    # Code

window.close()