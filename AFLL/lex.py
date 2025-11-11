import ply.lex as lex

# List of token names
tokens = (
    'DEF',
    'ID',
    'NUMBER',
    'STRING',
    'LPAREN',
    'RPAREN',
    'LBRACKET',
    'RBRACKET',
    'LBRACE',
    'RBRACE',
    'COLON',
    'COMMA',
    'ASSIGN',
    'FOR',
    'IN',
    'WHILE',
    'RANGE',
    'MATCH',
    'CASE',
    'UNDERSCORE',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LT',
    'GT',
    'LE',
    'GE',
    'EQ',
    'NE',
    'PASS',
    'BREAK',
    'CONTINUE',
    'RETURN',
    'INDENT',
    'DEDENT',
    'NEWLINE',
)

# Reserved words
reserved = {
    'def': 'DEF',
    'for': 'FOR',
    'in': 'IN',
    'while': 'WHILE',
    'range': 'RANGE',
    'match': 'MATCH',
    'case': 'CASE',
    'pass': 'PASS',
    'break': 'BREAK',
    'continue': 'CONTINUE',
    'return': 'RETURN',
}

# Token rules
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COLON = r':'
t_COMMA = r','
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_EQ = r'=='
t_NE = r'!='
t_UNDERSCORE = r'_'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_STRING(t):
    r'\"([^\\\n]|(\\.))*?\"'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    return t

# Ignore spaces and tabs
t_ignore = ' \t'

# Track indentation (simplified)
indent_stack = [0]

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test function
if __name__ == '__main__':
    data = '''
def add(x, y):
    return x + y

for i in range(10):
    pass
'''
    lexer.input(data)
    for tok in lexer:
        print(tok)
