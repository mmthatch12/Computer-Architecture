import sys

PRINT_BEEJ     = 1 #0000 0001
HALT           = 2 #0000 0010
PRINT_NUM      = 3 #0000 0011
SAVE           = 4 #0000 0100
PRINT_REGISTER = 5 #0000 0101
ADD            = 6 #0000 0110

memory = [
    PRINT_BEEJ,
    SAVE,
    65,
    2,
    SAVE,
    20,
    3,
    ADD,
    2,
    3,
    PRINT_REGISTER,
    2,
    PRINT_BEEJ,
    PRINT_NUM,
    46,
    PRINT_BEEJ,
    PRINT_BEEJ,
    HALT
]

registers = [0] * 8

# program counter
pc = 0
running = True

while running:
    # execute instruction in memory

    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
        pc += 1

    elif command == PRINT_NUM:
        num = memory[pc+1]
        print(num)
        pc += 2
    
    elif command == HALT:
        running = False
        pc += 1

    elif command == SAVE:
        num = memory[pc + 1]
        reg  = memory[pc + 2]
        registers[reg] = num
        pc += 3

    elif command == ADD:
        reg_a = memory[pc+1]
        reg_b = memory[pc+2]
        registers[reg_a] += registers[reg_b]
        pc += 3
    
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(registers[reg])
        pc += 2

    else:
        print(f"Error: Unknown command: {command}")
        sys.exit(1)

