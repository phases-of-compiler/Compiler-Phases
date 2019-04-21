import re
import token

f = open("code.txt", "r")

co = f.readline()

con = re.split("\s+", co)
print(con)
tokens = list()

for i in con:
    if re.fullmatch("[a-zA-Z_][a-zA-Z0-9_]*", i):
        tokens.append(token.tokener('ide'))
    elif re.fullmatch("[0-9]*", i) or re.fullmatch("[0-9]+.[0-9]+", i):
        tokens.append(token.tokener("lit", i))
    elif re.fullmatch("[;=+.]*", i):
        tokens.append(token.tokener(i))

print("Generated Tokens : ", tokens)
