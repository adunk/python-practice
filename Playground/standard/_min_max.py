player_one_score = 1
player_two_score = 10

print(min(player_one_score, player_two_score))
print(max(player_two_score, player_one_score))

# Compare first mismatched letter alphabetically.
# In this case h come before i, so Kathryn is returned
print(min('kathryn', 'katie'))
# This will return katie: i is greater than h
print(min('kathryn', 'katie'))
