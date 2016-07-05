from easygui.boxes.choice_box import choicebox
from phase1 import phase1
from phase2 import phase2

__author__ = 'po0ya'

choices = [
    'Phase1',
    'Phase2'
]

choice = choicebox(msg='Please select project phase:', choices=choices)

if choice == choices[0]:
    phase1()
else:
    phase2()
