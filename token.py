operators = {'+': {'id': 'OP', 'priority': '0'},
             '-': {'id': 'OP', 'priority': '1'},
             '*': {'id': 'OP', 'priority': '2'},
             '/': {'id': 'OP', 'priority': '3'},
             '=': {'id': 'OP', 'priority': '4'},
             '+=': {'id': 'OP', 'priority': '5'},
             '-=': {'id': 'OP', 'priority': '6'},
             '*=': {'id': 'OP', 'priority': '7'},
             '/=': {'id': 'OP', 'priority': '8'},
             '==': {'id': 'OP', 'priority': '9'},
             '++': {'id': 'OP', 'priority': '10'},
             '--': {'id': 'OP', 'priority': '11'},
             ';': {'id': 'OP', 'priority': '12'},
             '/*': {'id': 'OP', 'priority': '13'},
             '*/': {'id': 'OP', 'priority': '14'},
             '.': {'id': 'OP', 'priority': '15'}
             }

identifier = {'ide': {'id': 'ID', 'priority': '0'}}


def tokener(para, val=None):
    if para in operators.keys():
        return list(operators[para].values())
    elif para in identifier.keys():
        return list(identifier[para].values())
    elif para == 'lit':
        return ['LT', val]
