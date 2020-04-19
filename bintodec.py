import PySimpleGUI as sg


class PythonScreen:
    def __init__(self):
        sg.change_look_and_feel('DarkGrey')
        # layout
        layout = [
            [sg.Text('Enter a binary number', size=(20,0)), sg.Input(size=(15, 0), key='binary')],
            [sg.Button('Convert')],
            [sg.Output(size=(37, 8))]
        ]
        # window
        self.window = sg.Window("Binary to Decimal converter").layout(layout)

    def start(self):
        while True:
            # Extract data from screen
            self.button, self.values = self.window.Read()
            binary = self.values['binary']
            decimal = 0
            for digit in binary:
                decimal = decimal * 2 + int(digit)
            print(decimal)


screen = PythonScreen()
screen.start()
