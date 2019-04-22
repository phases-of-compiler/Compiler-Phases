import string

terminals = list(string.ascii_lowercase + "+-*/()&")
non_terminals = list(string.ascii_uppercase)
eps = '@'
endmarker = '$'

# input_productions = {
#     'S': ['AaBb'],
#     'A': [eps],
#     'B': [eps]
# }

input_productions = {
    'E': ['TG'],
    'G': ['+TG', eps],
    'T': ['FU'],
    'U': ['*FU', eps],
    'F': ['(E)', '&']
}


firsts = {}
follows = {}


def first(non_terminal):
    """ Input: Productions of a specific non-terminal """
    if non_terminal in list(firsts.keys()):
        return firsts[non_terminal]
    first_list = set()
    productions = input_productions[non_terminal]
    for production in productions:
        for symbol in production:
            if symbol in terminals:
                first_list.add(symbol)
                break
            if symbol in non_terminals:
                next_first = first(symbol)
                temp_next = next_first.copy()
                if eps in temp_next:
                    temp_next.remove(eps)
                first_list = first_list.union(temp_next)
                if eps not in next_first:
                    break
            if symbol is eps:
                first_list.add(eps)
                break
    firsts[non_terminal] = first_list
    return first_list


def main_first():
    for k in input_productions.keys():
        first(k)


main_first()


def follow(non_terminal, start=False):
    if non_terminal in list(follows.keys()):
        return follows[non_terminal]
    # print("Follow for", non_terminal)
    follow_list = set()
    if start:
        follow_list.add(endmarker)
    for k, productions in input_productions.items():
        if k == non_terminal: continue
        # print("k is", k)
        for production in productions:
            # print("Production:", production)
            index = production.find(non_terminal)
            if index is -1:
                continue
            elif len(production) == index+1:
                follow_list = follow_list.union(follow(k))
                # print("Last!")
            elif production[index+1] in terminals:
                follow_list.add(production[index+1])
            elif production[index+1] in non_terminals:
                temp_index = index+1
                next_iter = True
                # print("non-terminal")

                while temp_index < len(production) and next_iter:
                    # print(temp_index)
                    first_next = first(production[temp_index])
                    # print(first_next)
                    if eps in first_next:
                        first_next.remove(eps)
                        if temp_index+1 == len(production):
                            # print("!!!")
                            first_next = first_next.union(follow(k))
                    else:
                        next_iter = False
                    follow_list = follow_list.union(first_next)
                    temp_index += 1
    follows[non_terminal] = follow_list
    return follow_list


def main_follow():
    for i, k in enumerate(input_productions.keys()):
        # print(k)
        if i == 0:
            follow(k, start=True)
        else:
            follow(k)


main_follow()

print("_______________________________________________\n")
print("Productions")
for k, v in input_productions.items():
    pro = ""
    for pr in v:
        pro += str(pr)+" | "
    print("{} : {}".format(k, pro[:-2]))
print("_______________________________________________\n")
print("First")
for k, v in firsts.items():
    print("{} : {}".format(k, v))
print("_______________________________________________\n")
print("Follow")
for k, v in follows.items():
    print("{} : {}".format(k, v))
print("_______________________________________________\n")
