"""CPU functionality."""

import sys

class CPU:
    """Main CPU class."""

    def __init__(self):
        """Construct a new CPU."""
        self.ram = [0]*255
        self.reg = [0]*8
        self.pc = 0 # program counter
        self.sp = 242
        pass

    def ram_read(self, mar): # mar = address in binary 
        # turn mar (memory address register)
        # into a base 10 number
        # that is the point in the ram you want to access
        # and return.
        # mar should be <= 255
        # and the value stored at that memory location
        # should also be less than 255
        # in this case we aren't really storing bytes we are 
        # storing values in ram, and as long as those values can
        # be represented by a number less than 255 the computer will work
        return self.ram[mar]

    def ram_write(self, mdr, mar): # mdr = data , mar = address
        # store mdr in ram[mar]
        self.ram[mar] = mdr
        print('success')
        pass


    def load(self,filepath):
        """Load a program into memory."""
        with open(filepath,'r') as f:
            program = f.read().splitlines()

        address = 0

        # For now, we've just hardcoded a program:

        # program = [
        #     # From print8.ls8
        #     0b10000010, # LDI R0,8
        #     0b00000000,
        #     0b00001000,
        #     0b01000111, # PRN R0
        #     0b00000000,
        #     0b00000001, # HLT
        # ]

        for instruction in program:
            if instruction == ' ' or instruction == "":
                continue
            elif instruction[0] == '#':
                continue
            self.ram[address] = int(instruction.split()[0],2)
            address += 1


    def alu(self, op, reg_a, reg_b):
        """ALU operations."""
        ADD = 160
        MUL = 162

        if op == ADD:
            self.reg[reg_a] += self.reg[reg_b] # may neeed % 256
        #elif op == "SUB": etc
        elif op == MUL:
            self.reg[reg_a] *= self.reg[reg_b] 
            self.reg[reg_a] = self.reg[reg_a] % 255
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
        TEST = 0
        HLT = 1
        PRN = 71
        LDI = 130
        ADD = 160
        MUL = 162
        ALU = [ADD,MUL]
        #Stack
        PUSH = 69
        POP = 70
        while True:
            ir = self.ram[self.pc] # instruction register = point in ram (specified by program counter)
            operand_a = self.ram[self.pc+1]
            operand_b = self.ram[self.pc+2]
            if ir == TEST:
                print('test acheived')
                sys.exit()
                pass

            elif ir == PUSH:
                self.ram[self.sp] = self.reg[operand_a]
                self.sp -= 1
                self.pc += 2
                pass

            elif ir == POP:
                self.sp += 1
                self.reg[operand_a] = self.ram[self.sp]
                self.pc += 2
                pass

            elif ir in ALU:
                self.alu(ir,operand_a,operand_b)
                self.pc +=3 # TODO check to make sure that this assumption is correct
                pass

            elif ir == PRN:
                # Print the contents of the value stored in register[operand_a]
                value = self.reg[operand_a]
                print(value)
                self.pc += 2
                pass

            elif ir == LDI:
                # set the operand_a register
                # to the value operand_b
                self.reg[operand_a] = operand_b
                self.pc += 3
                pass

            elif ir == HLT:
                print('end of program')
                sys.exit()
                pass

            else:
                print(f'Invalid instruction {ir} at pc location {self.pc}')
                sys.exit()
                pass

        pass
