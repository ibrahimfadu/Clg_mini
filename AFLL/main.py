"""
Python Syntax Validator using PLY Tools
Tests 5 Constructs:
1. Function Definition
2. List Declaration
3. For Loop
4. While Loop (Do-While alternative)
5. Match Statement (Switch alternative)
"""

from lex import lexer
from yacc import parser

def test_construct(title, code):
    print(f"\n{'='*60}")
    print(f"{title}")
    print(f"{'='*60}")
    print("Input Code:")
    print(code)
    print(f"{'-'*60}")
    print("Parsing Result:")
    try:
        result = parser.parse(code, lexer=lexer)
    except Exception as e:
        print(f"✗ Error: {e}")
    print(f"{'='*60}\n")

if __name__ == '__main__':
    print("\n" + "="*60)
    print("PYTHON SYNTAX VALIDATOR - PLY IMPLEMENTATION")
    print("="*60)
    
    # Test 1: Function Definition
    test_construct(
        "TEST 1: FUNCTION DEFINITION",
        '''def calculate(a, b, c):
    return a + b
'''
    )
    
    # Test 2: List Declaration
    test_construct(
        "TEST 2: LIST DECLARATION",
        '''my_list = [10, 20, 30, 40, 50]
'''
    )
    
    # Test 3: For Loop
    test_construct(
        "TEST 3: FOR LOOP",
        '''for counter in range(5):
    pass
'''
    )
    
    # Test 4: While Loop
    test_construct(
        "TEST 4: WHILE LOOP",
        '''while x < 100:
    continue
'''
    )
    
    # Test 5: Match Statement (Switch)
    test_construct(
        "TEST 5: MATCH STATEMENT (SWITCH)",
        '''match value:
    case 1:
        pass
    case 2:
        pass
    case _:
        break
'''
    )
    
    # Test 6: Invalid Syntax
    test_construct(
        "TEST 6: INVALID SYNTAX (Missing colon)",
        '''def broken(x)
    return x
'''
    )
    
    print("\n" + "="*60)
    print("ALL TESTS COMPLETED")
    print("="*60)
