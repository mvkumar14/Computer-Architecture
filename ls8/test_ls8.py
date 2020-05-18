import unittest
from cpu import *

class Test(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU()

    def test_read_write(self):
        # address and value to write
        write_value = 0b00001000
        address = 0b00000000
        # write to address, and then read from address
        self.cpu.ram_write(write_value,address)
        output = self.cpu.ram_read(address)
        # check if the write value matches
        # the read value
        self.assertEqual(write_value,output)

if __name__ == '__main__':
    unittest.main()