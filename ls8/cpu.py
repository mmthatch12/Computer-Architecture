"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.reg = [0] * 8
        self.pc  = 0 # program counter, address of the currently executing instruction
        self.ram = [0] * 256
        self.fl = 4
    
    def ram_read(self, mar):
        return self.ram[mar]

    def ram_write(self, mar, mdr):
        self.ram[mar] = mdr

    def load(self, filename):
        """Load a program into memory."""

        address = 0

        # For now, we've just hardcoded a program:

        program = []

        try:
            with open(filename) as f:
                for line in f:
                    comment_split = line.split("#")
                    num = comment_split[0].strip()

                    if num == "":
                        continue

                    val = int(num, 2)
                    program.append(val)
        
        except FileNotFoundError:
            sys.exit(2)

        for instruction in program:
            self.ram[address] = instruction
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""

        if op == "ADD":
            self.reg[reg_a] += self.reg[reg_b]
        #elif op == "SUB": etc

        elif op == "MUL":
            self.reg[reg_a] *= self.reg[reg_b]

        elif op == "CMP":
            if self.reg[reg_a] == self.reg[reg_b]:
                self.reg[self.fl] = 0b00000001
            elif self.reg[reg_a] < self.reg[reg_b]:
                self.reg[self.fl] = 0b00000100
            elif self.reg[reg_a] > self.reg[reg_b]:
                self.reg[self.fl] = 0b00000010

        else:
            raise Exception("Unsupported ALU operation")

    def trace(self):
        """
        Handy function to print out the CPU state. You might want to call this
        from run() if you need help debugging.
        """

        print(f"TRACE: %02X | %02X %02X %02X |" % (
            self.pc,
            #self.fl,
            #self.ie,
            self.ram_read(self.pc),
            self.ram_read(self.pc + 1),
            self.ram_read(self.pc + 2)
        ), end='')

        for i in range(8):
            print(" %02X" % self.reg[i], end='')

        print()

    def run(self):
        """Run the CPU."""

        running = True

        HLT = 0b00000001
        LDI = 0b10000010
        PRN = 0b01000111
        MUL = 0b10100010
        CMP = 0b10100111
        JMP = 0b01010100
        JEQ = 0b01010101


        while running:
            ir = self.ram_read(self.pc)
            operand_a = self.ram_read(self.pc+1)
            operand_b = self.ram_read(self.pc+2)
            print("self.ram", self.ram)
            print("self.reg", self.reg)

            opcode = ir #command
            if opcode == HLT:
                running = False

            elif opcode == LDI:
                self.reg[operand_a] = operand_b
                self.pc += 3

            elif opcode == PRN:
                print(self.reg[operand_a])
                self.pc += 2
            
            elif opcode == MUL:
                self.alu("MUL", operand_a, operand_b)
                self.pc += 3
            
            elif opcode == CMP:
                self.alu("CMP", operand_a, operand_b)
                self.pc += 3
            
            elif opcode == JMP:
                index = self.pc
                nextind = self.ram.index(self.reg[operand_a])
                if nextind > index:
                    self.pc += nextind - index
                elif nextind < index:
                    self.pc -= index - nextind 
            
            elif opcode == JEQ:
                index = self.pc
                nextind = self.ram.index(self.reg[operand_a])
                if self.reg[self.fl] == 0b00000001:
                    if nextind > index:
                        self.pc += nextind - index
                    elif nextind < index:
                        self.pc -= index - nextind 
                else:
                    self.pc += 2
            

            
            

            



        

