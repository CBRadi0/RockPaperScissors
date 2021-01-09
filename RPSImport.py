import random

class RPS:
    def __init__(self):
        self.choices = ['Rock', 'Paper', 'Scissors']
        self.rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
        self.paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

        self.scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

        

    def setUp(self):
        print('ROCK PAPER SCISSORS\n\n1 - for Rock\n2 - for Paper\n3 - for Scissors\n')
        self.playerChoice = input('Type: 1, 2 or 3: \n')
        self.computerChoice = random.choice(self.choices)
        self.playerAutoChoice = random.choice(self.choices)
    def processChoice(self):
        try:
            if self.playerChoice == '1':
                self.playerChoice = 'Rock'
            elif self.playerChoice == '2':
                self.playerChoice = 'Paper'
            elif self.playerChoice == '3':
                self.playerChoice = 'Scissors'
            else:
                print(f"********You did not enter a correct choice, we selected {self.playerAutoChoice} for you*********\n\n")
                self.playerChoice = self.playerAutoChoice

        except:
            print(f"********You did not enter a correct choice, we selected {self.playerAutoChoice} for you*********\n\n")
            self.playerChoice = self.playerAutoChoice
        
    def play(self):
        # If Player Chooses Rock
        if self.playerChoice == 'Rock' and self.computerChoice  == 'Rock':
            print(f'Player Chose\n{self.rock}\n\n  Computer Chose\n{self.rock}\n\n The game is a draw!!!')
        elif self.playerChoice == 'Rock' and self.computerChoice  == 'Paper':
            print(f'Player Chose\n{self.rock}\n\n  Computer Chose\n{self.paper}\n\n Computer Wins!!!')
        elif self.playerChoice == 'Rock' and self.computerChoice  == 'Scissors':
            print(f'Player Chose\n{self.rock}\n\n  Computer Chose\n{self.scissors}\n\n Player Wins!!!')
        #If Player Chooses Paper
        if self.playerChoice == 'Paper' and self.computerChoice  == 'Rock':
            print(f'Player Chose\n{self.paper}\n\n  Computer Chose\n{self.rock}\n\n Player Wins!!!')
        elif self.playerChoice == 'Paper' and self.computerChoice  == 'Paper':
            print(f'Player Chose\n{self.paper}\n\n  Computer Chose\n{self.paper}\n\n The game is a draw!!!')
        elif self.playerChoice == 'Paper' and self.computerChoice  == 'Scissors':
            print(f'Player Chose\n{self.paper}\n\n  Computer Chose\n{self.scissors}\n\n Computer Wins!!!')
        #If Player Chooses Scissors
        if self.playerChoice == 'Scissors' and self.computerChoice  == 'Rock':
            print(f'Player Chose\n{self.scissors}\n\n  Computer Chose\n{self.rock}\n\n Computer Wins!!!')
        elif self.playerChoice == 'Scissors' and self.computerChoice  == 'Paper':
            print(f'Player Chose\n{self.scissors}\n\n  Computer Chose\n{self.paper}\n\n Player Wins!!!')
        elif self.playerChoice == 'Scissors' and self.computerChoice  == 'Scissors':
            print(f'Player Chose\n{self.scissors}\n\n  Computer Chose\n{self.scissors}\n\n The game is a draw!!!')



        