from pyscript import display, document

teams = {
    "7_Ruby": "Red Bulldogs",
    "7_Emerald": "Green Hornets",
    "7_Sapphire": "Blue Bears",
    "7_Topaz": "Yellow Tigers",
    "8_Ruby": "Red Bulldogs",
    "8_Emerald": "Green Hornets",
    "8_Sapphire": "Blue Bears",
    "8_Topaz": "Yellow Tigers",
    "9_Ruby": "Red Bulldogs",
    "9_Emerald": "Green Hornets",
    "9_Sapphire": "Blue Bears",
    "9_Topaz": "Yellow Tigers",
    "10_Ruby": "Red Bulldogs",
    "10_Emerald": "Green Hornets",
    "10_Sapphire": "Blue Bears",
    "10_Topaz": "Yellow Tigers",
}

def signup_form(e):
    username = document.getElementById('username').value
    password = document.getElementById('password').value
    
    if not username or not password:
        document.getElementById('signup_output').innerHTML = 'Please fill in all fields'
    elif len(password) < 7:
        document.getElementById('signup_output').innerHTML = 'Password must be at least 7 characters long'
    else:
        document.getElementById('signup_output').innerHTML = 'Account created. You may now log in using your credentials.'

def team_checker_form(e):
    grade = document.getElementById('grade').value
    section = document.getElementById('section').value
    requirement1 = document.getElementById('requirement1').value
    requirement2 = document.getElementById('requirement2').value

    if requirement1 == "no" or requirement2 == "no":
        document.getElementById('teamchecker_output').innerHTML = "Not eligible. Please complete requirements first"
    elif grade and section:
        team_key = f"{grade}_{section}"
        team_name = teams.get(team_key, "Unknown Team")
        document.getElementById('teamchecker_output').innerHTML = f"Congratulations! You are part of the {team_name}"
    else:
        document.getElementById('teamchecker_output').innerHTML = "Please select your grade and section"


names = [
    "Abayon",
    "Antes",
    "Apostol",
    "Banaag",
    "Barrientos",
    "Casal",
    "Coeli",
    "David",
    "De Mata",
    "Dela Cruz F",
    "Dela Cruz L",
    "Dellejero",
    "Fukuda",
    "Fukuda",
    "Gozum",
    "Ibay",
    "Lim",
    "Lozano",
    "Mamauag",
    "Navarro",
    "Precones",
    "Ramos",
    "Sidhu",
    "Villamayor",
    "Zaragoza"
]

output = ""
for name in names:
    output += f"{name}<br>"
    document.getElementById("name_list").innerHTML = output




