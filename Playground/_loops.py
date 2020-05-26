
secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5

# while pw != secret:
#     count += 1
#     if count > max_attempt:
#         break
#     pw = input(f'{count}: What is the secret word? ')
# else:
#     auth = True
#
# print('Authorized' if auth else 'calling the FBI!')

animals = ('cat', 'dog', 'pony', 'dinosaur', 'bear', 'bunny')

for pet in animals:
    if pet == 'pony':
        continue
    # if pet == 'bear':
    #    break
    print(pet)
else:
    print('that is all of the animal!')
