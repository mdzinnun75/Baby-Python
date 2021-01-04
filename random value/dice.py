import random


class Dice1:
    def first_value(self):
        value = [1, 2, 3, 4, 5, 6]
        got_value = random.choice(value)
        value2 = [1, 2, 3, 4, 5, 6]
        got_value2 = random.choice(value2)
        return got_value, got_value2

'''
    def last_value():
        value2 = [1, 2, 3, 4, 5, 6]
        got_value2 = random.choice(value2)
        return got_value2
        '''

dice = Dice1()
print(dice.first_value())

# class Result(dice1):
    # print(dice1.first_value(), dice1.last_value())

'''
    class Dice:
        def roll(self):
            first = random.randint(1 ,6)
            last = random.randint(1, 6)
            return first , second

    dice = Dice()
    print(dice.roll)
'''