with open('notes.txt') as myF:
    print(myF.read(50))
    print(myF.tell())
    print(myF.read(10), end='*')
    print(myF.readline())                # it gave the line on which the stream was positioned (in the middl of 3rd line)


with open("notes.txt", "rb") as f:
    f.read(50)
    print(f.tell())

with open("notes.txt", "rb") as f:
    print(f.read(30))

with open("notes.txt") as f:
    print(repr(f.readline()))


with open("data.txt", "r") as f:
    f.seek(7)
    print(f.read(11))
