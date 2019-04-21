from anytree import Node
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
    output = []
    for element in elements:
        print("\nOpstack: ", opstack)
        print("Output: ", output)
        print("Element added:", element)
        if element in letters:
            output.append(element)
            continue
        if element in ops:
            if len(opstack) == 0:
                opstack.append(element)
                continue
            if precedence[element] >= precedence[opstack[-1]]:
                opstack.append(element)
                continue
            if precedence[element] < precedence[opstack[-1]]:
                while True:
                    output.append(opstack.pop())
                    if len(opstack) == 0:
                        break
                    if not precedence[element] < precedence[opstack[-1]]:
                        break
                opstack.append(element)

    while len(opstack) > 0:
        output.append(opstack.pop())

    return output


output = infix_to_postfix("d=z*a/b+c")

print("\n----- Done -----")
print(output)
