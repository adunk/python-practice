import re

str = 'an example word:cat!'

# match = re.search(pat, str)

# The 'r' at the start of the pattern string designates a python "raw" string which passes through backslashes without
# change which is very handy for regular expressions.

# . (a period) -- matches any single character except newline '\n'
# \w -- (lowercase w) matches a "word" character: a letter or digit or underbar [a-zA-Z0-9_]
# \W (upper case W) matches any non-word character.
# \b -- boundary between word and non-word
# \s -- (lowercase s) matches a single whitespace character -- space, newline, return, tab, form
# \S (upper case S) matches any non-whitespace character.
# \t, \n, \r -- tab, newline, return
# \d -- decimal digit [0-9] (some older regex utilities do not support but \d, but they all support \w and \s)
# ^ = start, $ = end -- match the start or end of the string

# \ -- inhibit the "specialness" of a character. So, for example, use \. to match a period or \\ to match a slash. If
# you are unsure if a character has special meaning, such as '@', you can put a slash in front of it, \@, to make sure
# it is treated just as a character.

match = re.search(r'word:\w\w\w', str)
match = re.search(r'..g', 'piiig')  # found, match.group() == "iig"

# On success, match.group() is matched text.
print(match)

# Repetition
# Things get more interesting when you use + and * to specify repetition in the pattern

# + -- 1 or more occurrences of the pattern to its left, e.g. 'i+' = one or more i's
# * -- 0 or more occurrences of the pattern to its left
# ? -- match 0 or 1 occurrences of the pattern to its left

match = re.search(r'pi+', 'piiig')  # found, match.group() == "piii"

# Finds the first/leftmost solution, and within it drives the + as far as possible (aka 'leftmost and largest').
# In this example, note that it does not get to the second set of i's.
match = re.search(r'i+', 'piigiiii')  # found, match.group() == "ii"

# Square Brackets
# Square brackets can be used to indicate a set of chars, so [abc] matches 'a' or 'b' or 'c'. The codes \w, \s etc.
# work inside square brackets too with the one exception that dot (.) just means a literal dot. For the emails problem,
# the square brackets are an easy way to add '.' and '-' to the set of chars which can appear around the @ with the
# pattern r'[\w.-]+@[\w.-]+' to get the whole email address:

# More square-bracket features: You can also use a dash to indicate a range, so [a-z] matches all lowercase letters.
# To use a dash without indicating a range, put the dash last, e.g. [abc-]. An up-hat (^) at the start of a
# square-bracket set inverts it, so [^ab] means any char except 'a' or 'b'.

str = 'purple alice-b@google.com monkey dishwasher'

match = re.search(r'[\w.-]+@[\w.-]+', str)
if match:
    print(match.group())  ## 'alice-b@google.com'

# Group Extraction
# The "group" feature of a regular expression allows you to pick out parts of the matching text. Suppose for the emails
# problem that we want to extract the username and host separately. To do this, add parenthesis ( ) around the username
# and host in the pattern, like this: r'([\w.-]+)@([\w.-]+)'. In this case, the parenthesis do not change what the
# pattern will match, instead they establish logical "groups" inside of the match text. On a successful search,
# match.group(1) is the match text corresponding to the 1st left parenthesis, and match.group(2) is the text
# corresponding to the 2nd left parenthesis. The plain match.group() is still the whole match text as usual.

match = re.search(r'([\w.-]+)@([\w.-]+)', str)
if match:
    print(match.group())  ## 'alice-b@google.com' (the whole match)
    print(match.group(1))  ## 'alice-b' (the username, group 1)
    print(match.group(2))  ## 'google.com' (the host, group 2)
