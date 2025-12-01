import math

class Counter():
    def __init__(self):
        self.counter = 50
        self.zeroes = 0
    
    '''def read_line_old(self, line):
        letter = line[0]
        number = int(line[1:])

        if letter == "R":
            self.counter = (self.counter + number) % 100
        else:
            self.counter = (self.counter - number) % 100
        
        if self.counter == 0:
            self.zeroes += 1'''
    
    
    def read_line(self, line):
        letter = line[0]
        number = int(line[1:])

        if letter == "R":
            self.modulo_counter(number, True)
        else:
            self.modulo_counter(number, False)
    
    def modulo_counter(self, number, is_positive):
        # We count the number of wrap arounds
        
        if is_positive:
            total = self.counter+number
            wraps, self.counter = divmod(total, 100)
            self.zeroes += wraps

        else:
            if self.counter ==0:
                self.zeroes -= 1 # In this special case we overcount when we start from 0 and go down
                
            total = self.counter-number
            wraps, self.counter = divmod(total, 100)
            self.zeroes += -wraps # Because divmod returns "negative wraps"
            if self.counter ==0: # We need to catch when we go "down" to zero
                self.zeroes += 1
    
    def output(self):
        print(self.zeroes)
    

def main(file):
    counter = Counter()
    with open (file) as f:
        for line in f:
            counter.read_line(line.strip())
    counter.output()

main("day1Input.txt")
#main("test.txt")




