from auxiliary import *

def cicle(target, base, rulesList, newFacts):

    if len(rulesList) == 0:

        if len(newFacts) == 0:
            return False

        for each in newFacts:
            base.append(each[0])

        newFacts = []
        rulesList = rules.copy()
        return cicle(target, base, rulesList, newFacts)

    else:
        currentRule = rulesList.pop(0)
        conditionalsInBase = True

        print("Verifying rule: ", currentRule)

        for conditional in currentRule[0]:
            if(conditional not in base):
                conditionalsInBase = False
                break

        if conditionalsInBase:

            for consequent in currentRule[1]:
                newFacts.append(consequent)
                print(colors.green, "\nFact verified\nadding '%c' to the base\n" % consequent, colors.end)
                if (target == consequent):
                    return True

            rules.remove(currentRule)

        return cicle(target, base, rulesList, newFacts)


def topDown(rules, base, target):
    print(colors.red, "\nStarting base: ", base)
    print("Target: ", target, colors.end, "\n")

    if (target in base):
        return True

    newFacts = []
    rulesList = rules.copy()

    return cicle(target, base, rulesList, newFacts)


rules = readRules()
base = readBase()
target = readTarget()

result = topDown(rules, base, target)
print(end="Verdict: ")
printResult(result)