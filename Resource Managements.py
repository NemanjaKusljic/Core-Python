# Default Encoding
import sys
print(sys.getdefaultencoding())

#Writing Text
f = open('Training_01.txt', mode = 'wt')
f.write('What is this magic?\n')
f.write("It's Python ;)")
#after close it becomes visible to other progams
f.close()

g = open('Training_01.txt', mode = 'rt')
#print(g.read())
print(g.readline())

#read every line into list
print(g.readlines())
g.close()

# Appending Text
h = open('Training_01.txt', mode = 'at')
h.writelines(
    ['Son of man, \n',
    'You cannot say, or guess, ',
    'A heap of broken images, ',
    'where the sun beats\n'
    ]
)
h.close()

r = open('Training_01.txt', mode = 'rt')
for line in r:
    sys.stdout.write(line)
r.close()


def read_series(filename):
# Read series and close automatically
# return list of integers

    with open(filename, mode='rt') as f:
        return[int(line.strip()) for line in f]
