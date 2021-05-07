import time
selected = ""


def lineprint(startlinenumber, linecount):
    for a in range(linecount):
        file = open("texts.txt", 'r', encoding="latin1")
        line = file.readlines()[startlinenumber]
        if setting.lower() == "m":
            print(line, end="")
            input("")
        elif setting.lower() == "a":
            print(line, end="")
            time.sleep(2)
        startlinenumber += 1


def lineinput(linenumber, count, notopened):
    global selected
    file = open("texts.txt", 'r', encoding="latin1")
    line = file.readlines()[linenumber]
    if notopened:
        selected = input(line)
    number = 1
    for a in range(count):
        number_str = str(number)
        if selected == number_str:
            return number_str
        else:
            number += 1


print("Möchtest du eine automatische oder manuelle Geschichtsführung?")
setting = input("Drücke A für Automatisch oder M für Manuell: ")

if setting.lower() == "m":
    i = input("Drücke Enter um fortzufahren...")

lineprint(1, 3)
lineprint(10, 5)
if lineinput(100, 2, True) == "1":
    lineprint(15, 4)
elif lineinput(100, 2, False) == "2":
    lineprint(19, 4)
    if lineinput(101, 3, True) == "1":
        lineprint(23, 3)
    elif lineinput(101, 3, False) == "2":
        lineprint(26, 2)
    elif lineinput(101, 3, False) == "3":
        lineprint(28, 5)
        if lineinput(102, 3, True) == "1":
            lineprint(33, 4)
            if lineinput(103, 2, True) == "1":
                lineprint(44, 2)
            elif lineinput(103, 2, False) == "2":
                lineprint(46, 1)
        elif lineinput(102, 3, False) == "2":
            lineprint(37, 2)
        elif lineinput(102, 3, False) == "3":
            lineprint(39, 5)
            if lineinput(104, 2, True) == "1":
                lineprint(47, 3)
            elif lineinput(104, 2, False) == "2":
                lineprint(50, 2)

print(" ")
input("Press Enter to close")

quit()
