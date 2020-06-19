# Sorting a Dictionary by Value
data = {
    'red': 1,
    'black': 3,
    'green': 2
}

s = sorted(data.items(), key=lambda x: x[1])
print(s)
# Same sort in reverse
sr = sorted(data.items(), key=lambda x: x[1], reverse=True)
print(sr)
