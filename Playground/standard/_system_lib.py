import sys

# Print arguments
print(f'Number of arguments: {len(sys.argv)} arguments')
print(f'Arguments {sys.argv}')

# Remove arguments
# Removes the first argument from the list (which is always the file path argument)
sys.argv.remove(sys.argv[0])
print(f'Arguments {sys.argv}')

# Sume up the arguments
arguments = sys.argv
sum = 0
for arg in arguments:
    try:
        number = int(arg)
        sum += number
    except Exception:
        print('bad input')

print(sum)
