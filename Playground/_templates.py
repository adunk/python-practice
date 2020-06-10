# String formatting with templates
# Compared to other string formatting methods, these have increases security functions
from string import Template

# The $ are important
templ = Template('You are watching ${title} by ${author}')

string = templ.substitute(title='Advanced Python', author='Andrew Dunkle')
print(string)

# Data can also be stored in a dictionary and passed into .substitute() later
data = {
    'title': 'Advanced Python',
    'author': 'Andrew Dunkle',
}
string2 = templ.substitute(data)
print(string2)
