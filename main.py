from pyscript import display
from js import document  

clubs = {
    'Art_club': {
        'Name': 'Art Club',
        'Pres': 'Ms. Macabago',
        'Loc': 'Room 607',
        'Mem': '45',
    },
    'Chess_club': {
        'Name': 'Chess Club',
        'Pres': 'Mr. Mergal',
        'Loc': 'Room 407',
        'Mem': '20',
    },
    'Ict_club': {
        'Name': 'Ict Club',
        'Pres': 'Ms. Ko',
        'Loc': 'Room 508',
        'Mem': '25',
    }
}

def generate(e):
    output = document.getElementById("output")
    output.innerHTML = ""

    selected = document.getElementById("clubDropdown").value  # Fixed ID
    club = clubs[selected]

    display(f"Club Name: {club['Name']}", target="output")
    display(f"Location: {club['Loc']}", target="output")
    display(f"President: {club['Pres']}", target="output")
    display(f"Members: {club['Mem']}", target="output")


