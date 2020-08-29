import PySimpleGUI as sg
from get_file import get_file
import music
import os

settings = music.get_settings()
file = get_file()
file_basename = os.path.basename(file)
try:
    sg.theme(settings['theme'])
except TypeError:
    sg.popup("settings loader failed")
    exit()
def settings_menu():
        
    settings_layout = [
        [sg.Text("settings")],
        [sg.Combo(sg.theme_list(), key='-THEME-')],
        [sg.Text("default Volume :-"),sg.Slider(range=(0, 10), default_value=5, orientation='horizontal', key='-VOLUME-')],
        [sg.OK(), sg.Cancel()]
    ]
    window = sg.Window("settings", layout=settings_layout)
    while True:
        event, values = window.read()
        if event in ("OK"):
            window.close()
            theme = values['-THEME-']
            default_volume = values['-VOLUME-']
            return {
                'theme' : theme,
                'volume' : default_volume 
            }

layout = [ 
    [sg.Button("settings", key='-SETTINGS-')],
    [sg.Button("Play", size=["30", "2"], key='-PLAY-')], 
    [sg.Button("Pause", size=["30", "2"], key='-PAUSE-')],
    [sg.Button("UnPause", size=["30", "2"], key='-UNPAUSE-')],
    [sg.Button("Reset", size=['30', '2'], key="-RESET-")],
    [sg.Button("Exit Player", size=['30', '2'], key="-EXIT_PLAYER-")],
    [sg.Text("Volume :-"),sg.Slider(range=(0, 10), default_value=settings['volume'], orientation='horizontal', key='-VOLUME-', enable_events=True)],
    [sg.Text('_'*30)],
    [sg.Text(file_basename, key='-MUSIC_FILE_NAME-')],
    [sg.Text("Please restart the player to enable new settings", visible=False, key='-SETTINGS_WARN-')]
]
window = sg.Window("Music Player", layout=layout, element_justification='center', auto_size_buttons=True, resizable=True)
while True:
    event, values = window.read()
    if event in ('-EXIT_PLAYER-', None):
        music.ExitWindow()

    elif event in ('-PLAY-'):
        music.Play(file)
        music.adjust_volume(settings['volume'])
    elif event in ("-PAUSE-"):
        music.Pause()

    elif event in ('-UNPAUSE-'):
        music.Unpause()

    elif event in ("-RESET-"):
        music.Reset()
    
    elif event in ('-VOLUME-'):
        volume = values['-VOLUME-']
        music.adjust_volume(volume)

    elif event in ("-SETTINGS-"):
        new_settings = settings_menu()
        music.append_new_settings(new_settings)
        window['-SETTINGS_WARN-'].Update(visible=True)

    else:
        sg.popup("event not recognised")

