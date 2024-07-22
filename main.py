import sys
from operations import Operations

def main():
    ops = Operations()
    #Map of all operations 
    operators = {
        '+': ops.plus,
        '-': ops.minus,
        '*': ops.multiplication,
        '/': ops.division
    }
    stack = []
    try: 
        while True: 
            user_input = input("> ").strip().split()
            for char in user_input: 
                if char == 'q':
                    sys.exit()
                if not char.isdigit() and char not in operators and not char.lstrip('-').isdigit(): 
                    print("Not a valid input. Goodbye!")
                    sys.exit()
                if char in operators:
                    # If char is an operator, call operation
                    operators[char](stack)
                #Add to stack if number 
                else:
                    stack.append(int(char))
            if stack: 
              print(stack[-1])
    except KeyboardInterrupt:
        print("\nUser interrupted program. Now exiting...")
        sys.exit()

if __name__ == "__main__":
    main()