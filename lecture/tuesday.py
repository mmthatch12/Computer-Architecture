import sys

PRINT_BEEJ     = 1 #0000 0001
HALT           = 2 #0000 0010
PRINT_NUM      = 3 #0000 0011
SAVE           = 4 #0000 0100
PRINT_REGISTER = 5 #0000 0101
ADD            = 6 #0000 0110

memory = [0]*256

registers = [0] * 8

# program counter
pc = 0
running = True


def load_memory(filename):

    try:
        address = 0
        with open(filename) as f:
            for line in f:
                comment_split = line.split("#")
                num = comment_split[0].strip()

                if num == "":
                    continue

                val = int(num) #base 10 but ls-8 is base 2

                memory[address] =val
                address += 1

    except FileNotFoundError:
        print(f"{sys.argv[0]}: {filename} not found")
        sys.exit(2)

if len(sys.argv) != 2:
    print("Usage: file.py filename", file=sys.stderr)
    sys.exit(1)

load_memory(sys.argv[1])



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

    else:
        print(f"Error: Unknown command: {command}")
        sys.exit(1)

