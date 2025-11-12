import ply.lex as lex

# List of token names
# Add COMMA to tokens list
tokens = (
    'DO', 'WHILE', 'FOR', 'IF', 'ELSE', 'SWITCH', 'CASE', 'DEFAULT', 'BREAK',
    'RETURN', 'INT', 'VOID', 'IDENTIFIER', 'NUMBER',
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'SEMI', 'COLON', 'COMMA',
    'PLUS', 'MINUS', 'MULT', 'DIV', 'ASSIGN',
    'EQ', 'NE', 'LT', 'LE', 'GT', 'GE'
)

# Add comma rule
t_COMMA = r','

# Regular expression rules for simple tokens
t_DO = r'do'
t_WHILE = r'while'
t_FOR = r'for'
t_IF = r'if'
t_ELSE = r'else'
t_SWITCH = r'switch'
t_CASE = r'case'
t_DEFAULT = r'default'
t_BREAK = r'break'
t_RETURN = r'return'
t_INT = r'int'
t_VOID = r'void'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_COLON = r':'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULT = r'\*'
t_DIV = r'/'
t_ASSIGN = r'='
t_EQ = r'=='
t_NE = r'!='
t_LT = r'<'
t_LE = r'<='
t_GT = r'>'
t_GE = r'>='

# A regular expression rule for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Check if the identifier is a reserved keyword
    reserved = {
        'do': 'DO',
        'while': 'WHILE',
        'for': 'FOR',
        'if': 'IF',
        'else': 'ELSE',
        'switch': 'SWITCH',
        'case': 'CASE',
        'default': 'DEFAULT',
        'break': 'BREAK',
        'return': 'RETURN',
        'int': 'INT',
        'void': 'VOID'
    }
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t

# A regular expression rule for numbers
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Define a rule to track line numbers (useful for error messages)
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'

# Error handling rule
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test data (optional, for individual testing)
if __name__ == '__main__':
    data = """
    int main() {
        int x = 5;
        if (x > 0) {
            return 1;
        } else {
            return 0;
        }
    }
    """
    lexer.input(data)
    for tok in lexer:
        print(tok)
