import PySimpleGUI as sg


def showWindow():
    layout = [[sg.Text("Enter URL")], [sg.Input(key='-INPUT-')], [sg.Text(size=(40,1), key='-OUTPUT-')], [sg.Button("SUBMIT")]]

    # Create the window
    window = sg.Window("Input", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "SUBMIT":
            window['-OUTPUT-']('Downloading...')

            window['-OUTPUT-']('Done!')

            window['-INPUT-']('')
        if event == sg.WIN_CLOSED:
            break

    window.close()
