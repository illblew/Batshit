import collections
import os
import random
import sys

seed = "13290873209321903820938120931809123831"
words = open("words.txt", "r").read().replace("\n","").split()

def wordData():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield ''.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)


def goBatshit(count):
    for i in range(0,int(count)):
        bat = wordData()
        sizeRand = random.randint(1024,1073741824)
        fileRand = random.randint(1024,66666666666666666666666)
        fname = "giant.out" + str(fileRand)
        fh = open(fname, 'w')
        while os.path.getsize(fname) < sizeRand:
            fh.write(bat.next())

if sys.argv[1]:
    count = sys.argv[1]
else:
    count = 1
print(count)
goBatshit(count)
