import psutil
import time
import re
import win32process as wproc
import win32gui

# user inputs how many seconds they want to track their app usage for
# function returns dictionary of app names and seconds used

def track_time(seconds):
    pattern = re.compile(".exe", re.IGNORECASE)
    process_time={} # used to save app name and how much time it has been in use 
    
    while seconds > 0:
        window = win32gui.GetForegroundWindow()
        tid, pid = wproc.GetWindowThreadProcessId(window)
        try:
            open_app = psutil.Process(pid).name() # app that is currently open and in use
        except psutil.NoSuchProcess: # error can occur if you save the pid and leave the app window before its name is retrieved
            print('Error process no longer exists!')
            pass
        else:
            open_app = pattern.sub("", open_app) # cleaning app name
            time.sleep(1)
            if open_app not in process_time.keys(): # check if app has been used before
                process_time[open_app] = 0 # create new key-value pair if not
            process_time[open_app] = process_time[open_app] + 1 # updates time spent on app
            seconds  = seconds - 1
    print(process_time)
    return process_time