import ply.yacc as yacc
from lex import tokens

# Grammar Rules

def p_program(p):
    '''program : statement_list'''
    print("Valid Python Program!")
    p[0] = p[1]

def p_statement_list(p):
    '''statement_list : statement
                     | statement_list statement'''
    pass

def p_statement(p):
    '''statement : function_def
                | list_declaration
                | for_loop
                | while_loop
                | match_statement
                | NEWLINE'''
    pass

# 1. FUNCTION DEFINITION
def p_function_def(p):
    '''function_def : DEF ID LPAREN param_list RPAREN COLON NEWLINE function_body'''
    print(f"Parsed function definition: {p[2]}")
    p[0] = ('function', p[2], p[4], p[8])

def p_param_list(p):
    '''param_list : 
                 | ID
                 | param_list COMMA ID'''
    pass

def p_function_body(p):
    '''function_body : simple_statement
                    | compound_statement'''
    pass

def p_simple_statement(p):
    '''simple_statement : PASS NEWLINE
                       | RETURN expression NEWLINE
                       | BREAK NEWLINE
                       | CONTINUE NEWLINE'''
    pass

def p_compound_statement(p):
    '''compound_statement : statement_list'''
    pass

# 2. LIST/ARRAY DECLARATION
def p_list_declaration(p):
    '''list_declaration : ID ASSIGN LBRACKET element_list RBRACKET NEWLINE'''
    print(f"Parsed list declaration: {p[1]}")
    p[0] = ('list', p[1], p[4])

def p_element_list(p):
    '''element_list : 
                   | expression
                   | element_list COMMA expression'''
    pass

# 3. FOR LOOP
def p_for_loop(p):
    '''for_loop : FOR ID IN range_call COLON NEWLINE loop_body'''
    print(f"Parsed for loop with variable: {p[2]}")
    p[0] = ('for', p[2], p[4], p[7])

def p_range_call(p):
    '''range_call : RANGE LPAREN expression RPAREN
                 | RANGE LPAREN expression COMMA expression RPAREN
                 | ID'''
    pass

# 4. DO-WHILE LOOP (using while with condition check pattern)
def p_while_loop(p):
    '''while_loop : WHILE expression COLON NEWLINE loop_body'''
    print(f"Parsed while loop")
    p[0] = ('while', p[2], p[5])

def p_loop_body(p):
    '''loop_body : simple_statement
                | compound_statement'''
    pass

# 5. MATCH STATEMENT (Switch equivalent in Python 3.10+)
def p_match_statement(p):
    '''match_statement : MATCH expression COLON NEWLINE case_list'''
    print(f"Parsed match statement")
    p[0] = ('match', p[2], p[5])

def p_case_list(p):
    '''case_list : case_block
                | case_list case_block'''
    pass

def p_case_block(p):
    '''case_block : CASE expression COLON NEWLINE simple_statement
                 | CASE UNDERSCORE COLON NEWLINE simple_statement'''
    pass

# EXPRESSIONS
def p_expression(p):
    '''expression : ID
                 | NUMBER
                 | STRING
                 | expression PLUS expression
                 | expression MINUS expression
                 | expression TIMES expression
                 | expression DIVIDE expression
                 | expression LT expression
                 | expression GT expression
                 | expression LE expression
                 | expression GE expression
                 | expression EQ expression
                 | expression NE expression
                 | LPAREN expression RPAREN'''
    pass

# Error rule
def p_error(p):
    if p:
        print(f"Syntax error at token {p.type} ('{p.value}') at line {p.lineno}")
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# Test function
if __name__ == '__main__':
    test_cases = [
        # Function definition
        '''def add(x, y):
    return x + y
''',
        # List declaration
        '''numbers = [1, 2, 3, 4, 5]
''',
        # For loop
        '''for i in range(10):
    pass
''',
        # While loop
        '''while x < 10:
    pass
''',
        # Match statement
        '''match status:
    case 1:
        pass
    case _:
        pass
'''
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n{'='*50}")
        print(f"Test Case {i}:")
        print(f"{'='*50}")
        print(test)
        print(f"{'-'*50}")
        
        from lex import lexer
        parser.parse(test, lexer=lexer)
