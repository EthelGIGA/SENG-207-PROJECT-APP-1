import PySimpleGUI as sg
import pyttsx3
import tkinter as tk

Text_to_speech_engine = pyttsx3.init()
VoiceTypes = Text_to_speech_engine.getProperty('voices')


layout = [    [sg.Text('Select the type of voice:',text_color='black',background_color='white'), sg.Radio('Female', 'RADIO1', default=True, 
 key='Female',background_color='silver'), sg.Radio('Male', 'RADIO1', key='Male',background_color='silver')],
     [sg.Text('Enter text to speak:',text_color= 'black',background_color='silver')],
          
    [sg.InputText(key='input'),sg.Button('Speak',button_color='black')],
    
    [sg.Text("Volume:",text_color= 'black',background_color='silver')],
    [sg.Slider(range=(0, 1), resolution=0.1, default_value=0.5, orientation="h", key="-VOLUME-")],
    [sg.Text("Speed:",text_color= 'black',background_color='silver')],
    [sg.Slider(range=(100, 300), resolution=10, default_value=200, orientation="h", key="-SPEED-")], 

      
      
]

window = sg.Window('Realmz Text to Speech App', layout,background_color='silver')


while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input']
        if values['Male']:
            Text_to_speech_engine.setProperty('voice', VoiceTypes[0].id)
        elif values['Female']:
            Text_to_speech_engine.setProperty('voice', VoiceTypes[1].id) 
        text = values['input']
        volume = values["-VOLUME-"]
        speed = values["-SPEED-"]
        Text_to_speech_engine.setProperty("volume", volume)
        Text_to_speech_engine.setProperty("rate", speed)
    
        Text_to_speech_engine.say(text)
        Text_to_speech_engine.runAndWait()

Text_to_speech_engine.stop()



window.close()
