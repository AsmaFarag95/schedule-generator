"""
GUI app of schedule-generator application.
Made by useing PySimpleGUI.
"""
import PySimpleGUI as sg
from schedule import main
#to handle user input 
def is_valid_year(value):
    
    if int(value) and 2023 <= int(value) <= 2030:
        return
    return sg.popup_error('Invalid input for Year. Please enter a numeric value between 2023 and 2030.')#pop error message for the user

def is_valid_month(value):
    if int(value) and 1 <= int(value) <= 12:
        return 
    return sg.popup_error('Invalid input for Month. Please enter a numeric value between 1 and 12.')

 

sg.theme('LightGreen') # Keep things interesting for your users

layout = [
    [sg.Text('Updated Schedule Generator', font=("Helvetica", 20))],
    [sg.Text('Choose Employee Excel File', size=(20, 1))],
    [sg.In(key='-MANAGER_FILE-', size=(25, 1)), sg.FileBrowse(file_types=(("Excel Files", "*.xlsx"),))],
    [sg.Text('Choose Teams File', size=(20, 1))],
    [sg.In(key='-TEAMS_FILE-', size=(25, 1)), sg.FileBrowse(file_types=(("Excel Files", "*.numbers"),))],
    [sg.HorizontalSeparator()],
    [sg.Text('Enter valid year YYYY and month MM',  size=(40, 1))],
    [sg.Text('Year:', size=(15, 1)), sg.Input(key='-YEAR-', size=(4, 1))],
    [sg.Text('Month:', size=(15, 1)), sg.Input(key='-MONTH-', size=(4, 1))],
    [sg.ProgressBar(1000, orientation='h',size=(30, 20), key='progressbar',bar_color=('green', 'white'))],
    [sg.Button('Calculate', key="-CALCULATE-"), sg.Exit()],
    [sg.HorizontalSeparator()],
    [sg.Text('New Section', size=(20, 1))],
    [sg.Button('New Action', key="-NEW_ACTION-")]
]


window = sg.Window('Window that stays open', layout)

while True: # The Event Loop
    event, values = window.read()

    managerFile = values['-MANAGER_FILE-']
    teamsFile = values['-TEAMS_FILE-']
    yearInput = int(values['-YEAR-'])
    monthInput = int(values['-MONTH-'])
    
    
    if event == '-CALCULATE-':
        if  is_valid_year(yearInput):
            continue
        if  is_valid_month(monthInput):
            continue
            break
    
    try:
        main(managerFile, yearInput, monthInput, teamsFile)
    except Exception as e:
        sg.popup_error(f'An error occurred: {str(e)}')
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

        
        

     
 
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

window.close()
