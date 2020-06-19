import tempfile

# useful for storing data only useful for the execution of the program

# Create a temporary file
temp = tempfile.TemporaryFile()

# Write to a temporary file
# write() takes a bytes object. In order to convert a string to a bytes literal, we place b in front of the string
temp.write(b'Save this special number for me: 12349876')
# Reset seek pointer back to 0
temp.seek(0)

# Read the temporary file
print(temp.read())

# Close the temporary file
temp.close()
