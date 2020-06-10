with open('scores.txt', 'w') as f:
    # w --> write
    # r --> read
    # r+ --> read and write
    # a --> append
    # t --> ???

    # Show attributes and properties of that file
    print(f'Name: {f.name}')
    print(f'Mode: {f.mode}')

    # Write to a file
    # In the 'write' mode this will write the entire file as given (meaning anything previously in the file is lost)
    # If you want to add content to an existing file, use the 'append' mode
    f.write('GBJ: 100\nKHD: 99\nBBB: 89')
    # This isn't needed when using the with ... f: pattern. Happens automatically
    # f.close()

# Read the file
with open('scores.txt', 'r') as new_file:
    # read() method takes an input of the number of characters you want to read
    # read(10) will read the first 10 characters
    print(f'Reading... {new_file.read()}')

    # In these examples we read the file in sequences of 10 characters.
    # These won't work if the above read() has been run as the whole file has already been read
    print(f'Reading 10 characters... {new_file.read(10)}')
    print(f'Reading next 10 characters... {new_file.read(10)}')

    # We can change this behavior by setting the seek pointer to a given index.
    # close() will also reset the seek point back to 0
    new_file.seek(0)

    # Read one line at a time
    # Note this will also change the seek pointer
    print(f'My one line: {new_file.readline()}')

    for line in new_file:
        # This will find and replace 'BBB' with 'PDJ' for each line
        # This will not save the file though, just the in-memory string object
        new_score = line.replace('BBB', 'PDJ')
        print(new_score)
