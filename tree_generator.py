from anytree import Node, RenderTree
from anytree.exporter import DotExporter
import string

precedence = {
    '=': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}

letters = list(string.ascii_letters)
ops = list(precedence.keys())


def infix_to_postfix(elements):
    opstack = []
    outputer = []
    for element in elements:
        if element in letters:
            outputer.append(element)
            continue
        if element in ops:
            if len(opstack) == 0:
                opstack.append(element)
                continue
            if precedence[element] > precedence[opstack[-1]]:
                opstack.append(element)
                continue
            if precedence[element] <= precedence[opstack[-1]]:
                while True:
                    outputer.append(opstack.pop())
                    if len(opstack) == 0:
                        break
                    if not precedence[element] <= precedence[opstack[-1]]:
                        break
                opstack.append(element)

    while len(opstack) > 0:
        outputer.append(opstack.pop())

    return outputer


output = infix_to_postfix("d=z*a/b+c")

print("Postfix Form of the equation : ", output)

nodedict = {}

listed = []

for i in output:
    if i not in ops:
        listed.append(Node(i))
        # print(listed)
    elif i in ops:
        nodedict[i] = Node(i)
        # print(nodedict)
        pop1, pop2 = listed.pop(), listed.pop()
        nodedict[i].children = [pop2, pop1]
        listed.append(Node(i))
print(nodedict['+'].children)
print("Nodes : ", nodedict)
node = []

# for i in range(len(nodedict.keys())):
#     node.append(list(nodedict.keys())[i])
#     node[i].children = list(nodedict.values())[i]
#     print(node[i].children)

for pre, _, noder in RenderTree(nodedict['=']):
    print("%s%s" % (pre, noder))
