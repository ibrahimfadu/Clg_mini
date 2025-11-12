import ply.yacc as yacc
from lex import tokens, lexer

# --- Define the grammar rules ---

# Starting point of the grammar
def p_program(p):
    '''program : function_definition'''
    print("Syntax is valid!")

# 1. Function Definition Construct
def p_function_definition(p):
    '''function_definition : type IDENTIFIER LPAREN parameters RPAREN LBRACE statements RBRACE'''

def p_parameters(p):
    '''parameters : parameter_list
                  | empty'''
    
def p_parameter_list(p):
    '''parameter_list : parameter_list COMMA parameter
                      | parameter'''

def p_parameter(p):
    '''parameter : type IDENTIFIER'''

def p_type(p):
    '''type : INT
            | VOID'''

# 2. For Loop Construct
def p_for_loop(p):
    '''for_loop : FOR LPAREN for_init SEMI condition SEMI for_update RPAREN LBRACE statements RBRACE'''

def p_for_init(p):
    '''for_init : assignment
                | declaration
                | empty'''

def p_for_update(p):
    '''for_update : assignment
                  | empty'''

# 3. Do-While Loop Construct
def p_do_while_loop(p):
    '''do_while_loop : DO LBRACE statements RBRACE WHILE LPAREN condition RPAREN SEMI'''

# 4. Nested If-Else Construct
def p_if_else_statement(p):
    '''if_else_statement : IF LPAREN condition RPAREN LBRACE statements RBRACE else_part'''

def p_else_part(p):
    '''else_part : ELSE LBRACE statements RBRACE
                 | ELSE if_else_statement
                 | empty'''

# 5. Switch-Case Construct
def p_switch_statement(p):
    '''switch_statement : SWITCH LPAREN expression RPAREN LBRACE case_list RBRACE'''

def p_case_list(p):
    '''case_list : case_list case
                 | case'''

def p_case(p):
    '''case : CASE expression COLON statements BREAK SEMI
            | DEFAULT COLON statements BREAK SEMI'''

# --- Supporting Grammar Rules ---

def p_statements(p):
    '''statements : statements statement
                  | statement
                  | empty'''

def p_statement(p):
    '''statement : expression_statement
                 | declaration_statement
                 | if_else_statement
                 | for_loop
                 | do_while_loop
                 | switch_statement
                 | return_statement
                 | LBRACE statements RBRACE'''

def p_expression_statement(p):
    '''expression_statement : expression SEMI
                           | assignment SEMI
                           | SEMI'''  # empty statement

def p_declaration_statement(p):
    '''declaration_statement : declaration SEMI'''

def p_declaration(p):
    '''declaration : type IDENTIFIER
                   | type IDENTIFIER ASSIGN expression'''

def p_assignment(p):
    '''assignment : IDENTIFIER ASSIGN expression'''

def p_condition(p):
    '''condition : expression'''

def p_expression(p):
    '''expression : simple_expression
                  | simple_expression relation simple_expression'''

def p_simple_expression(p):
    '''simple_expression : term
                        | simple_expression PLUS term
                        | simple_expression MINUS term'''

def p_term(p):
    '''term : factor
            | term MULT factor
            | term DIV factor'''

def p_factor(p):
    '''factor : IDENTIFIER
              | NUMBER
              | LPAREN expression RPAREN'''

def p_relation(p):
    '''relation : EQ
                | NE
                | LT
                | LE
                | GT
                | GE'''

def p_return_statement(p):
    '''return_statement : RETURN expression SEMI
                       | RETURN SEMI'''

def p_empty(p):
    'empty :'
    pass

# --- Error Handling ---
def p_error(p):
    if p:
        print(f"Syntax error at token '{p.value}' (type: {p.type}) at line {p.lineno}")
        # Skip ahead to the next semicolon or brace to continue parsing
        parser.errok()
        # Look for next semicolon, brace, or newline to resync
        while True:
            tok = parser.token()
            if not tok or tok.type in ['SEMI', 'LBRACE', 'RBRACE']:
                break
    else:
        print("Syntax error at EOF")

# Build the parser
parser = yacc.yacc()

# --- Test the parser with the chosen constructs ---
if __name__ == '__main__':
    print("=" * 50)
    print("TESTING C++ CONSTRUCTS WITH PLY")
    print("=" * 50)

    test_cases = [
        # Test 1: Do-While Loop
        """
        int main() {
            do {
                x = x - 1;
            } while (x > 0);
        }
        """,
        # Test 2: Nested If-Else
        """
        void check() {
            if (a == 10) {
                if (b < a) {
                    result = 1;
                } else {
                    result = 2;
                }
            } else {
                result = 3;
            }
        }
        """,
        # Test 3: For Loop
        """
        int loop() {
            for (,i = 0; i < 10; i = i + 1) {
                sum = sum + i;
            }
        }
        """,
        # Test 4: Switch-Case
        """
        void choice() {
            switch (option {
                case 1:
                    x = 10;
                    break;
                case 2:
                    x = 20;
                    break;
                default:
                    x = 0;
                    break;
            }
        }
        """,
    ]

    for i, code in enumerate(test_cases, 1):
        print(f"\n--- Test Case {i}: ---")
        print("Input Code Snippet:")
        print(code.strip())
        print("Parser Output:")
        try:
            result = parser.parse(code)
            if result is None:
                print("✅ SUCCESS: Parsing completed without syntax errors.")
        except Exception as e:
            print(f"❌ FAILED: An error occurred: {e}")
