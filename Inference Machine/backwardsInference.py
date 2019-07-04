from auxiliary import *

def buildGraph(rules):
    graph = {}
    for conditionals, consequents in rules:
        for each in consequents:
            if (each not in graph): graph[each] = []
            graph[each] += [conditionals]

    return graph

def backwards(graph, base, target):

    if (target in base):
        return(True)

    if (target not in graph):
        return False

    for rule in graph[target]:
        for element in rule:
            if (backwards(graph, base, element)):
                base.append(element)
            else:
                break
        else:
            return True

    return False

rules = readRules()
base = readBase()
target = readTarget()

graph = buildGraph(rules)
print("\nInference Graph:", graph)

result = backwards(graph, base, target)
print(end="Verdict: ")
printResult(0, result)