import PySimpleGUI as sg
import time
from ThreadReturn import ThreadWithReturnValue
from AppTracker import track_time
from database import save_data

font = ("Helvetica", 16)
sg.set_options(font=font)
sg.theme('Purple')

layout = [
    [sg.Text('How many seconds do you want to track your app usage for? '), sg.Text(size=(20,1), key='text')],
    [sg.Text(''), sg.Text(size=(50,12), key='dict')], # 50,12
    [sg.Input(key='input')],
    [sg.Button('Start'), sg.Button('Exit'), sg.Button('Save', disabled=True)],
    [sg.ProgressBar(100, orientation='h', expand_x=True, size=(20, 20),  key='-PBAR-')],  
    [sg.Text('Progress bar', key='-OUT-', enable_events=True, font=('Arial Bold', 16), justification='center', expand_x=True)]
]
window = sg.Window('App tracker', layout, [10,100])

while True:
    event, values = window.read()
    print('event:', event)
    print('values:', values)

    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    if event == 'Start':
        try:
            input = int(values['input'])
        except:
            window['dict'].update('Only integers are allowed')
            continue
        pbar = 0
        window['Save'].update(disabled=True)
        thread = ThreadWithReturnValue(target=track_time, args=(input,), daemon=True) # creating thread in order to track apps and update progress bar simultaneously
        thread.start()
        # updating progress bar based on user input (seconds)
        for i in range(input):
            pbar = pbar + (100/input)
            window['-PBAR-'].update(pbar)
            time.sleep(1)
            print(pbar)

        response = thread.join() # waiting for thread to complete
        print('thread response: ', response)
        window['dict'].update(f'Dictionary key-value pairs of app(s) and seconds spent on them: {str(response)}')
        window['Save'].update(disabled=False)
        
    if event == 'Save':
        window['dict'].update('Saving dictionary data to database')
        window['Save'].update(disabled=True)
        save_data(response)

window.close()