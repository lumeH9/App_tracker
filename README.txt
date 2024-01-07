Motivation

I started this project because i wanted to find out how much time i spend on different apps and web pages. The latter is still a work in progress, but the former is nearly complete. This data can provide valuable insight and help in making sure i spend my time more efficiently and constructively. Parents could also use this program to moniter their childs internet usage. 


Program description

The program has a GUI where the user is asked how many seconds they want to track their app usage for. After they input the duration and press the 'start' button the program starts to track how many seconds are spent on different apps during that time. Only the app that is currently open and the foremost window is analyzed. The apps name and seconds spent on it are saved into a dictionary. Once the tracking has completed the user can save the gathered data into their local MSSQL database by pressing the 'save' button.


Requirements

pip install PySimpleGUI, time, threading, psutil, re, win32process, win32gui, pypyodbc

A MSSQL or other database is required and you need to configure your database connection string variables in the 'database' file, so that they are set according to your own driver, server and database name. 


Running the program

Make sure you have python installed.

Double click run_program.bat in file explorer

or

type this command in cmd in the App_tracker file:

python app_gui_main.py

or 

open the same file in your IDE and run it there.


Running tests

Type this command in cmd:

python test_program_in_cmd.py