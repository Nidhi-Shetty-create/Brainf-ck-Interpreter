import sys
import time

# Step 0: Initial setup and environment
# For this step, ensure you have your IDE/editor set up and are ready to begin developing.
# No additional code is needed for this step, as it simply involves setting up your working environment.

# Step 1: REPL (Read-Evaluate-Print-Loop) for Brainf*ck
def run_interpreter(code):
    memory = [0] * 30000  # Initialize memory with 30,000 cells
    pointer = 0  # Data pointer
    code_pointer = 0  # Program counter

    # Loop through the Brainfuck code
    while code_pointer < len(code):
        command = code[code_pointer]

        if command == '>':
            pointer += 1
        elif command == '<':
            pointer -= 1
        elif command == '+':
            memory[pointer] += 1
        elif command == '-':
            memory[pointer] -= 1
        elif command == '.':
            print(chr(memory[pointer]), end='')  # Output the character at the pointer
        elif command == ',':
            memory[pointer] = ord(input("Input a character: ")[0])  # Input a character and store it
        elif command == '[':
            if memory[pointer] == 0:
                # Jump forward to the matching closing bracket
                open_brackets = 1
                while open_brackets != 0:
                    code_pointer += 1
                    if code[code_pointer] == '[':
                        open_brackets += 1
                    elif code[code_pointer] == ']':
                        open_brackets -= 1
        elif command == ']':
            if memory[pointer] != 0:
                # Jump backward to the matching opening bracket
                close_brackets = 1
                while close_brackets != 0:
                    code_pointer -= 1
                    if code[code_pointer] == ']':
                        close_brackets += 1
                    elif code[code_pointer] == '[':
                        close_brackets -= 1

        code_pointer += 1  # Move to the next command


# Step 2: Basic REPL to enter Brainf*ck code and run
def repl():
    while True:
        code = input("Enter Brainf*ck code (type 'exit' to quit): ").strip()
        if code.lower() == 'exit':
            print("Exiting...")
            break
        else:
            print("\nOutput:")
            start_time = time.time()  # Start measuring time
            run_interpreter(code)
            end_time = time.time()  # End measuring time
            print("\nExecution time: {:.6f} seconds".format(end_time - start_time))  # Print execution time


# Step 3: Compiler to target a simple Virtual Machine (VM)
# This will convert Brainf*ck code into a simplified bytecode representation.
def compile_to_bytecode(code):
    bytecode = []
    i = 0
    while i < len(code):
        if code[i] == '>':
            bytecode.append('MOVE_RIGHT')
        elif code[i] == '<':
            bytecode.append('MOVE_LEFT')
        elif code[i] == '+':
            bytecode.append('INCREMENT')
        elif code[i] == '-':
            bytecode.append('DECREMENT')
        elif code[i] == '.':
            bytecode.append('OUTPUT')
        elif code[i] == ',':
            bytecode.append('INPUT')
        elif code[i] == '[':
            bytecode.append('LOOP_START')
        elif code[i] == ']':
            bytecode.append('LOOP_END')
        i += 1
    return bytecode


# Step 4: Virtual Machine (VM) to execute bytecode
def run_bytecode(bytecode):
    memory = [0] * 30000  # Initialize memory with 30,000 cells
    pointer = 0  # Data pointer
    bytecode_pointer = 0  # Program counter

    while bytecode_pointer < len(bytecode):
        command = bytecode[bytecode_pointer]

        if command == 'MOVE_RIGHT':
            pointer += 1
        elif command == 'MOVE_LEFT':
            pointer -= 1
        elif command == 'INCREMENT':
            memory[pointer] += 1
        elif command == 'DECREMENT':
            memory[pointer] -= 1
        elif command == 'OUTPUT':
            print(chr(memory[pointer]), end='')  # Output the character at the pointer
        elif command == 'INPUT':
            memory[pointer] = ord(input("Input a character: ")[0])  # Input a character and store it
        elif command == 'LOOP_START':
            if memory[pointer] == 0:
                open_loops = 1
                while open_loops != 0:
                    bytecode_pointer += 1
                    if bytecode[bytecode_pointer] == 'LOOP_START':
                        open_loops += 1
                    elif bytecode[bytecode_pointer] == 'LOOP_END':
                        open_loops -= 1
        elif command == 'LOOP_END':
            if memory[pointer] != 0:
                close_loops = 1
                while close_loops != 0:
                    bytecode_pointer -= 1
                    if bytecode[bytecode_pointer] == 'LOOP_END':
                        close_loops += 1
                    elif bytecode[bytecode_pointer] == 'LOOP_START':
                        close_loops -= 1

        bytecode_pointer += 1  # Move to the next command


# Step 5: Function to load code from a file
def load_code_from_file(filename):
    try:
        with open(filename, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None


# Step 6: Further Optimization for performance
# Implement further optimizations like recognizing repeated operations and handling common loop patterns.

def main():
    print("Welcome to the Brainf*ck Interpreter!\n")
    while True:
        choice = input("Select an option:\n1. Enter Brainf*ck Code (REPL)\n2. Compile and Run Bytecode\n3. Load and Run from File\n4. Exit\nChoice: ")
        
        if choice == '1':
            # Step 1: Enter Brainf*ck code and run via REPL
            repl()
        elif choice == '2':
            # Step 3: Compile Brainf*ck code to bytecode and run via VM
            code = input("Enter Brainf*ck code to compile: ")
            start_time = time.time()  # Start measuring time for compilation
            bytecode = compile_to_bytecode(code)
            end_time = time.time()  # End measuring time for compilation
            print("\nCompilation time: {:.6f} seconds".format(end_time - start_time))  # Print compilation time
            
            print("\nExecuting Bytecode:")
            start_time = time.time()  # Start measuring time for execution
            run_bytecode(bytecode)
            end_time = time.time()  # End measuring time for execution
            print("\nExecution time: {:.6f} seconds".format(end_time - start_time))  # Print execution time
        elif choice == '3':
            # Step 5: Load and run from a file
            filename = input("Enter the file name containing Brainf*ck code: ")
            code = load_code_from_file(filename)
            if code:
                print("\nRunning the code from the file:")
                start_time = time.time()  # Start measuring time
                run_interpreter(code)
                end_time = time.time()  # End measuring time
                print("\nExecution time: {:.6f} seconds".format(end_time - start_time))  # Print execution time
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
