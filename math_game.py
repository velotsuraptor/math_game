import random
import time
correct = 0
incorrect = 0
num_of_gam = 0
sum_time = 0
choise = input('Введіть обсяг розміру чисел:\n1)1-9\n2)1-50\n3)1-100\n4)1-1000\nДля зупинки гри напишіть stop\n')
if choise == '1':
    while True:
        n1 = random.randint(1, 9)
        n2 = random.randint(1, 9)
        l1 = ['+', '-']
        sym = random.choice(l1)
        if sym == '+':
            print(f'{n1}+{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 + n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} Incorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
        if sym == '-':
            print(f'{n1}-{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 - n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
if choise == '2':
    while True:
        n1 = random.randint(1, 50)
        n2 = random.randint(1, 50)
        l1 = ['+', '-']
        sym = random.choice(l1)
        if sym == '+':
            print(f'{n1}+{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 + n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
        if sym == '-':
            print(f'{n1}-{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 - n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
if choise == '3':
    while True:
        n1 = random.randint(1, 100)
        n2 = random.randint(1, 100)
        l1 = ['+', '-']
        sym = random.choice(l1)
        if sym == '+':
            print(f'{n1}+{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 + n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
        if sym == '-':
            print(f'{n1}-{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 - n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
if choise == '4':
    while True:
        n1 = random.randint(1, 1000)
        n2 = random.randint(1, 1000)
        l1 = ['+', '-']
        sym = random.choice(l1)
        if sym == '+':
            print(f'{n1}+{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 + n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')
        if sym == '-':
            print(f'{n1}-{n2} = ')
            num_of_gam += 1
            tt = time.time()
            res = n1 - n2
            ans = input()
            if ans == 'stop':
                break
            elif int(ans) == res:
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                correct += 1
                print(f'Correct! It took you {int(tt3)} secs!\nCorrect:{correct} \nIncorrect:{incorrect}.')
                continue
            else:
                incorrect += 1
                tt2 = time.time()
                tt3 = tt2 - tt
                sum_time += tt3
                print(f'Wrong choise, correct answer is {res}\nCorrect:{correct} \nIncorrect:{incorrect}.')

print(f'Good job!\nCorrect: {correct} \nIncorrect: {incorrect}\nYour average time is {int(sum_time/num_of_gam)} sec!')
text = input('Натисніть ентер для виходу з програми.')