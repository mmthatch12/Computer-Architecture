import sys

PRINT_BEEJ = 1
HALT = 2

memory = [
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    PRINT_BEEJ,
    HALT
]

# program counter
pc = 0
running = True

while running:
    # execute instruction in memory

    command = memory[pc]

    if command == PRINT_BEEJ:
        print("Beej!")
    
    elif command == HALT:
        running = False

    else:
        print(f"Error: Unknown command: {command}")
        sys.exit(1)

    pc += 1

