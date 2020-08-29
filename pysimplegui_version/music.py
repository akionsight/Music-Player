import pygame
import json
def Play(file):
    '''
    playes the song
    '''
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

def Reset():
    '''
    plays the song again from beginning
    '''
    pygame.mixer.music.stop()
    pygame.mixer.music.play()

def Pause():
    '''
    pauses the song
    '''
    pygame.mixer.music.pause()

def Unpause():
    '''
    unpauses the song
    '''
    pygame.mixer.music.unpause()

def ExitWindow():

    '''
    exits the player safely
    '''
    pygame.mixer.stop()
    exit()

def adjust_volume(volume):
    '''
    adjusts volume !
    '''
    actual_volume = volume / 10
    pygame.mixer.music.set_volume(actual_volume)

def get_settings():
    '''
    return settings loaded from configuration.json file
    '''
    settings_read = open("configaration.json", 'r')
    dict__ = json.loads(settings_read.read())
    return dict__

def append_new_settings(new_settings):
    '''
    addes new settings to configaration.json file
    '''
    settings = open("configaration.json", 'w')
    settings.truncate(0)
    settings.write(json.dumps(new_settings))



    
