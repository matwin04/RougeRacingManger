from appJar import gui
import webbrowser
import time
import pyautogui
import subprocess
import os


        
app = gui("RRM", "400x200")
app.startTabbedFrame("MainMenu") 
app.startTab("MainMenu")  
time_label = app.addLabel("time", "")
time_label.config(font=("Arial", 20))
def update_time():
    current_time = time.strftime("%I:%M:%S %p")
    time_label.config(text=current_time)
    app.after(1000, update_time)
update_time()


app.startTab("Command Center")
app.addLabelOptionBox("Select Client",["select clients"])
app.addLabelOptionBox("Select Command",["List of Commands","Run Sigma","New Race LB","Restart","Shut Down","Sleep"])
app.stopTab()



app.go()