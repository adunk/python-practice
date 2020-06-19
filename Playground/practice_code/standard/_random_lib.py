import random

print(random.random())
decider = random.randrange(2)
if decider == 0:
    print('heads')
else:
    print('tails')

dice = random.randrange(1, 7)
print(f'You rolled a {dice}')

# Random Choices
lottery_winners = random.sample(range(100), 5)
print(lottery_winners)

possible_pets = ['cat', 'dog', 'fish']
print(random.choice(possible_pets))

cards = ['jack', 'queen', 'king', 'ace']
random.shuffle(cards)
print(cards)
