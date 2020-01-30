import sys

PRINT_BEEJ     = 1 #0000 0001
HALT           = 2 #0000 0010
PRINT_NUM      = 3 #0000 0011
SAVE           = 4 #0000 0100
PRINT_REGISTER = 5 #0000 0101
ADD            = 6 #0000 0110
PUSH           = 7
POP            = 8
CALL           = 9
RET            = 10

memory = [0] * 256

registers = [0] * 8

SP = 7

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
        print(registers)

    elif command == ADD:
        reg_a = memory[pc+1]
        reg_b = memory[pc+2]
        registers[reg_a] += registers[reg_b]
        pc += 3
        print(registers)
    
    elif command == PRINT_REGISTER:
        reg = memory[pc + 1]
        print(registers[reg])
        pc += 2

    elif command == PUSH:
        reg = memory[pc+1]
        val = registers[reg]

        register[SP] -=1
        memory[registers[SP]] = val
        pc += 2

    elif command == POP:
        reg = memory[pc+1]
        val = memory[registers[SP]]
        registers[reg] = val
        registers[SP] += 1

        pc += 2

    elif command == CALL:
        val = pc +2
        registers[SP] -= 1
        memory[registers[SP]] = val
        reg = memory[pc +1]
        subroutine_address = registers[reg]
        pc = subroutine_address 
        

    elif command == RET:
        return_address = registers[SP]
        pc = memory[return_address]
        SP += 1

    else:
        print(f"Error: Unknown command: {command}")
        sys.exit(1)

