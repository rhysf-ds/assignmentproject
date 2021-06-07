import random
import pandas as pd

questionset = {
    0: {'Question': 'What position did Harry Potter play on the Quidditch team?',
        'Answer': ['Seeker'],
        'Other': ['keeper', 'Bludger', 'Chaser']},
    1: {'Question': 'which of the following is not an unforgivable curse?',
        'Answer': ['Sectum Sempra'],
        'Other': ['Avada Kedavra', 'Cruciatus', 'Imperius']},
    2: {'Question': 'What is a Thestral?',
        'Answer': ['An Invisible Winged Horse'],
        'Other': ['A Pixie', 'A Half Giant', 'A Living Plant']},
    3: {'Question': 'What animal represents Ravenclaw?',
        'Answer': ['Eagle'],
        'Other': ['Raven', 'Bear', 'Owl']},
    4: {'Question': 'Dobby\'s tombstone says \"Here Lies Dobby\" and ends with what?',
        'Answer': ['A free elf'],
        'Other': ['A True Friend', 'A Loyal Servant', 'Master of socks']},
    5: {'Question': 'What magical talent does harry potter share with voldemort?',
        'Answer': ['Parselmouth'],
        'Other': ['Legilimency', 'Occlumency', 'Animagus']},
    6: {'Question': 'What jumps out of the train window, on their trip to hogwarts in the philosophers stone?',
        'Answer': ['A Chocolate frog'],
        'Other': ['Scabbers, Rons rat', 'Crookshanks, hermiones cat', 'A house elf']},
    7: {'Question': 'What is the dursleys address?',
        'Answer': ['4 privet drive'],
        'Other': ['221b Baker street', '177A Bleecker Street', '12 Grimmauld Place']},
    8: {'Question': 'Who is Fluffy?',
        'Answer': ['Hagrids Three Headed Dog'],
        'Other': ['Hermione\'s Cat', 'Harry\' Owl', 'Hagrids Hippogryph']},
    9: {'Question': 'What impact do dementors have on people?',
        'Answer': ['Drain all of their happiness'],
        'Other': ['Cause people the attach each other', 'Control their mind', 'Make them insane']},
    10: {'Question': 'Who Kills Dumbledore?',
         'Answer': ['Severus Snape'],
         'Other': ['Draco Malfoy', 'Voldemort', 'Bellatrix Lestrange']},
    11: {'Question': 'Which platform at Kings Cross station does the Hogwarts Express leave from?',
         'Answer': ['9 and 3/4'],
         'Other': ['1 and a half', '42', '7 and 6/12']},
    12: {'Question': 'Who is Harry Potter\'s godfather?',
         'Answer': ['Sirius Black'],
         'Other': ['Dumbledore', 'Severus Snape', 'Hagrid']},
    13: {'Question': 'What did Harry Potter give to Dobby to free him from the Malfoys?',
         'Answer': ['A Sock'],
         'Other': ['A parchment declaring his freedom', 'A silver dagger', 'his own wand']},
    14: {'Question': 'What potion can change someone\'s appearance to match someone else\'s?',
         'Answer': ['Polyjuice potion'],
         'Other': ['Veritaserum', 'Felix Felicis', 'Wiggenweld Potion']},
    15: {'Question': 'What is the name of the wand shop on Diagon Alley?',
         'Answer': ['Olivanders'],
         'Other': ['Flourish and Blotts', 'Gringotts', 'Magical Menagerie']},
    16: {'Question': 'What was the make and model of Harry\'s first broomstick?',
         'Answer': ['Nimbus 2000'],
         'Other': ['Comet 290', 'Firebolt', 'Cleansweep Eleven']},
    17: {'Question': 'What phrase closes the marauders map?',
         'Answer': ['Mischief managed'],
         'Other': ['Misconduct Achieved', 'Shenanigans Sorted', 'Funny business conducted']},
    18: {'Question': 'Who was the half blooded prince?',
         'Answer': ['Severus Snape'],
         'Other': ['Sirius Black', 'Harry Potter', 'Voldemort']},
    19: {'Question': 'What is the incantation for lighting up your wand?',
         'Answer': ['Luminos'],
         'Other': ['Inca solaris', 'Accio Lumo', 'Alohomorra']},
    20: {'Question': 'What is the name of the luck potion?',
         'Answer': ['Felix Felicis'],
         'Other': ['Polyjuice Potion', 'Veritaserum', 'Wolfsbane potion']}
}


# create a list of questions in the form of a dictionary of dictionaries
# it allows for easy and organised management of the questions, their correct answers and answer sets


class Player:
    def __init__(self, playername):
        self.playername = playername
        self.points = 0
        self.answers = []

    # create a player class that will hold the details for players like their score and their name
    def correctanswer(self):
        self.points += 1

    def answerlog(self, questionnumber, playeranswer, correctanswer):
        self.answers.append([questionnumber, playeranswer, correctanswer])

    def allanswers(self):
        for x in self.answers:
            print(f'For question {x[0]} you answered {x[1]}, which was correct' if x[1] == x[2] else
                  f'For question {x[0]} you answered {x[1]} which was incorrect, the answer was {x[2]}')


# function to print out the answers to all the questions that the player answered, it conditionally
# checks for each answer whether or not it was correct


class Question:
    def __init__(self, questionnum):
        self.question = questionset[questionnum]['Question']
        self.correct = questionset[questionnum]['Answer']
        self.wrong = questionset[questionnum]['Other']
        self.choices = [i for i in range(1, 5)]
        self.answerjoin = self.correct + self.wrong
        random.shuffle(self.answerjoin)
        self.answers = dict(zip(self.choices, self.answerjoin))

    # create a question class to build a question object for each round of the game
    # it accepts an integer then uses that to pull the appropriate question from the question dictionary
    def rightanswer(self):
        return self.correct[0]

    def prompt(self):
        return print(f'{self.question} \n\
        1.) {self.answers[1]} \n\
        2.) {self.answers[2]} \n\
        3.) {self.answers[3]} \n\
        4.) {self.answers[4]} ')


# the question object has a prompt to return the question and it's potential answers

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.qset = []
        self.qset = random.sample(range(0, 20), self.rounds)
        self.leaderboard = []

    # the game object holds the information on the game itself, number of rounds and generates the random set of numbers
    # which is used to pull each question
    def questionset(self):
        return self.qset

    def addtoleaderboard(self, playername, score):
        self.leaderboard.append([playername, score])

    def finalscore(self):
        self.df = pd.DataFrame(self.leaderboard, columns=['Name', 'Score']).sort_values('Score',
                                                                                        ascending=False).reset_index(
            drop=True)
        self.df.index += 1
        self.winner = self.df['Name'][1]
        self.avg = round(self.df['Score'].mean())
        print(f'Thank you for playing! {self.winner} won! \n'
              f'the average score for all players was {self.avg} \n'
              'the leaderboard is: \n')
        return self.df
# this function creates a dataframe of the previously stored names and scores, sorts them by the score
# and gets the average score for everyone then prints out the final message once the game is over

def roundinput():
    rounds = 0
    while rounds == 0 or not 1 <= rounds <= 20:
        try:
            rounds = int(input('How many questions would you like to play? (max 20): '))
            if 1 <= rounds <= 20:
                return rounds
            else:
                print('invalid number please choose between 1 and 20')
                continue
        except:
            print('Incorrect input please try again')
        break

def playernameinput(quiz):
    while 1:
        pname = input('What is your name?: ')
        if pname in list(i[0] for i in quiz.leaderboard):
            print('Name already in leaderboard please try again')
        elif pname == '':
            print('player name can\'t be blank please try again')
        else:
            return pname


def questioninput(a,q):
    while a.lower() not in dict((k, v.lower()) for k, v in q.answers.items()).values():
        a = input('Your answer: ').strip()
        if a.isnumeric():
            if int(a) in q.answers.keys():
                a = q.answers[int(a)]
                return a
            elif a.lower() not in dict((k, v.lower()) for k, v in q.answers.items()).values():
                print(
                    'Sorry, invalid answer please try again. Enter Either the answer number or the answer')
            else:
                print(
                    'Sorry, invalid answer please try again. Enter Either the answer number or the answer')
                continue
        elif a.lower() in dict((k, v.lower()) for k, v in q.answers.items()).values():
            return a
        else:
            print(
                'Sorry, invalid answer please try again. Enter Either the answer number or the answer')
            continue


def answercheck(a, q, p , num):
    if a.lower() == q.rightanswer().lower():
        print('correct!')
        p.correctanswer()
        p.answerlog(num, a, q.rightanswer())
    else:
        print('Sorry, Wrong answer!')
        p.answerlog(num, a, q.rightanswer())


def play():
    print('Welcome to the harry potter quiz! Thank you for playing')
    rounds = roundinput()
    quiz = Game(rounds)
    # this while loop & try axcept block manages the inputs for the number of rounds, ensuring that its an integer
    # and within the range that's allowed
    while 1:
        p = Player(playernameinput(quiz))
        num = 0
        for i in quiz.questionset():
            q = Question(i)
            q.prompt()
            num += 1
            a = ''
            a = questioninput(a, q)
            answercheck(a, q, p, num)
        print(f'Thanks for playing! You scored {p.points} which is {(p.points / rounds) * 100}%')
        p.allanswers()
        quiz.addtoleaderboard(p.playername, p.points)
        r = input('Do you want to play another round?: ')
        if r.lower() == 'yes':
            continue
        else:
            print(quiz.finalscore())
            break


play()
