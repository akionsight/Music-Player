import PySimpleGUI as sg
def get_file():
    layout = [ [sg.Text('Please find the file to play')],
                [sg.Input(), sg.FileBrowse(button_text='Browse File')],
                [sg.OK()]]

    window = sg.Window("Select File").Layout(layout)
    while True:
        event, values = window.read()
        if event in (None, 'OK'):
            window.close()
            file_name = values[0]
            return file_name


