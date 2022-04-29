from sonia_skills.sonia_speak import SoniaSpeak
from playsound import playsound
from pathlib import Path

sonia = SoniaSpeak()


class SoniaSkills:
    def __init__(self):
        self.sonia_skills = ['riddle', 'music', 'song']

        # riddles logic
        self.riddles_correctly = 0
        self.average_iq_test = 2
        self.riddles = [
            {'riddle': 'What word begins with a T, ends with a T, and has a T in it?', 'answer': 'teapot'},
            {'riddle': 'princess mother has three children. Their names are prince, tom, whats the name of the third child', 'answer': 'princess'},
            {'riddle': 'What word is spelled wrong in the dictionary? ', 'answer': 'wrong'},
            {'riddle': 'A boat sinks, and every single person drowns. Who survives? ', 'answer': 'married people'},
            {'riddle': 'Kelly has three daughters, and each daughter has a brother. How many children does Kelly have? ', 'answer': 'four'},
            {'riddle': 'The more you take, the more you leave behind. What are they?', 'answer': 'footsteps'},
        ]


    def validate_task(self, task, name):
        check_task = list(filter(lambda x: x in task, self.sonia_skills))

        if check_task:
            if check_task[0] == 'riddle':
                sonia.speak('here is a list of riddle, please impress me by answering at least 4 riddles correctly')
                self.riddle(name)
                return True
            elif check_task[0] == 'music' or check_task[0] == 'song':
                sonia.speak('what would you like me to play')
                music_name = input('Enter music title: ')
                try:
                    self.play_music(music_name)
                    return True
                except KeyboardInterrupt:
                    sonia.speak('stopping music')
                    return True
            
        else:
            return False          
       


    def riddle(self, name):
        for index, riddle in enumerate(self.riddles):
            sonia.speak(riddle['riddle'])
            answer = input('Enter answer: ')

            if answer == riddle['answer']:
                self.riddles_correctly += 1
                if index != len(self.riddles) - 1:
                    sonia.speak(f'correct {name}, proceeding to the next riddle')
                else:
                    sonia.speak(f'correct {name}')

            else:
                if index != len(self.riddles) - 1:
                    sonia.speak(f'incorrect {name}, proceeding to the next riddle')
                else:
                    sonia.speak(f'incorrect {name}')


            if index == len(self.riddles) - 1:
                if self.riddles_correctly >= self.average_iq_test:
                    sonia.speak(f'you did great {name}, you answered {self.riddles_correctly} riddles out of {len(self.riddles)} correctly')
                else:
                    sonia.speak(f'you did poorly {name}, you answered only {self.riddles_correctly} riddles correctly out of {len(self.riddles)} riddles')

    def play_music(self, music_name):
        sonia.speak(f'playing {music_name}, just a quick hint. hold control c on your keyboard to stop music')
        print('CTRL+C to stop music')  

        music_path = str(Path(__file__).parent) + '\\' + 'music' + '\\' + f'{music_name}.mp3'

        playsound(music_path) 

          






