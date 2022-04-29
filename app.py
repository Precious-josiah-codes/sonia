from sonia_skills.sonia_speak import SoniaSpeak
from sonia_skills.skills import SoniaSkills


sonia = SoniaSpeak()
sonia_skill = SoniaSkills()


sonia.speak('Hello, im sonia, your virtual companion, Here is a list of what i could do')
print('''
1. tell a joke
2. play a riddle
3. play you a music
''')

while True:
    sonia.speak('Whats your name')
    username = input('Enter name: ')
    sonia.speak(f'nice to meet you { username }, what would you have me do?')
    task = input('What would you have me do for you: ')
    validate = sonia_skill.validate_task(task, username)

    if not validate:
        sonia.speak(f'im sorry {username}, i cant do that at the moment')

    break


