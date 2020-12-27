import PySimpleGUI as sg
import downloader as d


def showWindow():
    layout = [[sg.Text("Enter URL")], [sg.Input(key='-URL-')], [sg.Input(key='-NAME-', size=(20,1))], [sg.Text(size=(40,1), key='-OUTPUT-')], [sg.Button("SUBMIT")]]

    # Create the window
    window = sg.Window("Input", layout)

    # Create an event loop
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "SUBMIT":
            window['-OUTPUT-']('Downloading...')
            d.download(values['-URL-'], values['-NAME-'])
            window['-OUTPUT-']('Done!')

            window['-URL-']('')
            window['-NAME-']('')
        if event == sg.WIN_CLOSED:
            break

    window.close()
