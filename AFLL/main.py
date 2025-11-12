from lex import lexer
from yacc import parser

tests = [
    ("Function Definition", "int main() { int x = 10; return x; }"),
    ("For Loop", "for(int i=0; i<10; i=i+1) { continue; }"),
    ("While Loop", "while(x<10) { x=x+1; }"),
    ("Do-While Loop", "do { x=x+1; } while(x<10);"),
    ("If-Else", "if(x>0){x=x-1;} else {x=0;}"),
    ("Switch", "switch(x){ case 1: break; case 2: break; default: break; }"),
]

print("\nC++ Syntax Validator (PLY)\n" + "="*60)
for title, code in tests:
    print(f"\n{'='*60}\n{title}\n{'='*60}\n{code}\n{'-'*60}")
    try:
        result = parser.parse(code, lexer=lexer)
        if result is None:
            print("✅ Syntax is VALID")
    except Exception as e:
        print(f"❌ Error: {e}")
