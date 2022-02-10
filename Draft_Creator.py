import csv
import operator
from itertools import cycle
import PySimpleGUI as sg
import traceback
import Person
people = []
outliers = []
person = Person.Person(
    "423423423",
    "Bob",
    "1"
)
num_line = 0
TeamCount = 0
TeamSize = 0


# -------------- GUI --------------
sg.theme('DarkGrey13')     
layout = [
    [sg.Text('Find the location of the csv file:', size =(30, 1)), sg.FileBrowse('  Click here  ', key = '-LOCATION-')],
    [sg.Text('How many players will the teams have?', size =(30, 1)), sg.InputText('', key = '-TEAMS-')],
    [sg.Text('How many teams do you want?', size =(30, 1)), sg.InputText('', key = '-COUNT-')],
    [sg.Text('Paste Discord ID column header', size =(30, 1)), sg.InputText('', key = '-INPUTIDS-')],
    [sg.Text('Paste name column header', size =(30, 1)), sg.InputText('', key = '-INPUTNAMES-')],
    [sg.Text('Paste skill level column header', size =(30, 1)), sg.InputText('', key = '-INPUTSKILL-')],
    [sg.Checkbox('Include name, and skill level', default=False, key="-All-")],
    [sg.Button("Calculate!", button_color=("#006000"), mouseover_colors=("#008000")), sg.Button("Clear Output", button_color=("#9e6515"), mouseover_colors=("#bf7a19"), size =(9, 1)), sg.Button("Exit", button_color=("#8A0000"), mouseover_colors=("#ad0000"))],
    [sg.Output(size=(600,200), key = '-OUTPUT-')]
]

Window = sg.Window('Hypes Draft Team Maker', layout,size=(800,600))
try:
    while True:
        event, values = Window.read()
        if event is None or event == 'Exit':
            break
        elif event == "Clear Output":
            Window['-OUTPUT-'].Update('')
        elif event == "Calculate!":
            error = 0
            location = values['-LOCATION-']
            TeamSize = values['-TEAMS-']
            TeamCount = values['-COUNT-']
            InputIDS = values['-INPUTIDS-']
            Skill = values['-INPUTSKILL-']
            All = values['-All-']
            Names = values['-INPUTNAMES-']  
            # Handle if they leave something blank
            if location == '':
                print("No location was entered!\n")
                error += 1
            if TeamSize == '':
                print("No team size was entered!\n")
                error += 1
            if TeamCount == '':
                print("No team count was entered!\n")
                error += 1
            if InputIDS == '':
                print("No discord ID colummn was entered!\n")
                error += 1
            if Skill == '':
                print("No skill colummn was entered!\n")
                error += 1
            if Names == '':
                print("No name colummn was entered!\n")
                error += 1
                
            if location != "":
                if location.endswith('.csv'):
                    pass
                else:
                    print("The file isnt a csv file! Make sure to download the sheet as csv!\n")
            
            if error > 0:
                if error > 1:
                    print("Errors found! Check the messages above for details.\n")
                else:
                    print("Error found! Check the message above for details.\n")
            else:
                location = values['-LOCATION-']
                TeamSize = values['-TEAMS-']
                TeamCount = values['-COUNT-']
                InputIDS = values['-INPUTIDS-']
                Skill = values['-INPUTSKILL-']
                All = values['-All-']
                Names = values['-INPUTNAMES-'] 
                people = []
                outliers = []
                num_line = 0
                person = Person.Person(
                    "423423423",
                    "Bob",
                    "1"
                )
                
                # -------------- Actual Code --------------
                location = str(location).replace('\\', '\\\\')
                filename = open(location, "r")
                file = csv.DictReader(filename, delimiter= ',')
                for col in file:
                    num_line +=1
                    person = Person.Person(
                    col[InputIDS],
                    col[Names],
                    col[Skill]
                )
                    people.append(person)
                players = int(TeamCount) * int(TeamSize)
                outlierCount = int(num_line) - int(players)
                print("There are", outlierCount, "outliers.")
                print("There will be", TeamCount, "teams of", TeamSize,end='.')

                for i in range(0,outlierCount):
                    outliers.append(people.pop())

                people.sort(key=operator.attrgetter('skill'))
                
                li = [*range(0,0), *range(int(TeamCount) - 1,-1, -1)] 
                it = cycle(li)
                TeamNumber = 1
                Teams = []
                for i in range(int(TeamCount)):
                    Teams.append([])
                    
                for player in people:
                    TeamNumber = next(it)
                    Teams[TeamNumber].append(player)

                for Team in Teams:
                    TeamNumber += 1
                    print(f'\nTEAM {TeamNumber}:')
                    for player in Team:
                        if All == True:
                            print(f'<@{player.id}>', "-", player.name, "-", player.skill)
                        else:
                            print(f'<@{player.id}>')
                print()
                print("OUTLIERS:")

                for player in outliers:
                    if All == True:
                        print(f'<@{player.id}>', "-", player.name, "-", player.skill)
                    else:
                        print(f'<@{player.id}>')
                print()
                print("---------------Task Finished---------------")
                print()
except Exception as e:
    tb = traceback.format_exc()
    sg.Print(f'An error happened. Ping HypeLights with a screenshot of this.  Here is the info:', e, tb)
    sg.popup_error(f'AN EXCEPTION OCCURRED!', e, tb)