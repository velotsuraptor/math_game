import random as r


class Game:
    def __init__(self):
        self.operators = None
        self.mn = None
        self.mx = None
        self.correct = 0
        self.wrong = 0
        self.num_g = 0
        self.sum_t = 0
        self.all_opers = []

    def stats(self):
        return (f'Correct: {self.correct}\n'
                f'Wrong: {self.wrong}\n'
                f'Number of games: {self.num_g}\n'
                f'Average time: {self.sum_t}\n')

    def sel_mode(self):
        try:
            print('Select games complexity:')
            self.mn = int(input('Select min number: \n'))
            self.mx = int(input('Select max number: \n'))
            self.operators = input('Write down all the operators you want to use: +, -, * \n')
            if ' ' in self.operators:
                self.operators = [i for i in self.operators.split(' ')]
            if ' ' not in self.operators:
                self.operators = [i for i in self.operators]
        except TypeError:
            print('Invalid input\n')
        for i in self.operators:
            if i not in self.all_opers:
                print('Invalid input!\n', self.operators)
                quit()

    def game(self):
        while True:
            try:
                ex = f'{r.randint(self.mn, self.mx)} {r.choice(self.operators)} {r.randint(self.mn, self.mx)}'
                print(ex)
                c_ans = eval(ex)
                u_ans = int(input())
                if c_ans == u_ans:
                    self.correct += 1
                    print(f'Correct!\nCorrect:{self.correct}\nWrong: {self.wrong}')
                    continue
                elif c_ans != u_ans:
                    self.wrong += 1
                    print(f"Wrong\nCorrect:{self.correct}\nWrong: {self.wrong}")
            except ValueError:
                print("You've paused game:( Here are your stats!\n"
                      f'Correct: {self.correct}\n'
                      f'Wrong: {self.wrong}\n')
                break
        ans = input("\nMaybe you've changed your mind and now you wanna play?\n Y/N\n")
        if ans == 'Y':
            self.game()
        else:
            quit()

    def play(self):
        self.sel_mode()
        print("Let's play! To exit print anything but numbers.")
        self.game()


g = Game()
g.play()
