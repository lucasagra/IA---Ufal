def readRules():
    rules = []
    while (True):
        line = input()
        if (line == "END"):
            break

        conditional, consequent = line.split("=>")
        rules += [[[s.strip(' ') for s in conditional.split('^')], [s.strip(' ') for s in consequent.split('^')]]]

    return rules

def readBase():
    base = []
    while (True):
        line = input()
        if (line == "END"):
            break

        [base.append(symbol) for symbol in line.split()]

    return base

def readTarget():
    target = ""
    while (True):
        line = input()
        if (line == "END"):
            break

        target = line

    return target


SPACE_SIZE = 3
class colors:
    yellow = "\033[93m"
    green = "\033[92m"
    red = "\033[91m"
    blue = "\033[96m"
    end = "\033[0m"


def printResult(result):
    print(colors.green if result else colors.red, str(result), colors.end, sep='')

