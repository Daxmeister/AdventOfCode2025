import math

class Counter():
    def __init__(self):
        self.counter = 50
        self.zeroes = 0
    
    def read_line_old(self, line):
        letter = line[0]
        number = int(line[1:])

        if letter == "R":
            self.counter = (self.counter + number) % 100
        else:
            self.counter = (self.counter - number) % 100
        
        if self.counter == 0:
            self.zeroes += 1
    
    
    def read_line(self, line):
        letter = line[0]
        number = int(line[1:])

        if letter == "R":
            #self.counter = (self.counter + number) % 100
            self.modulo_counter(number, True)
        else:
            #self.counter = (self.counter - number) % 100
            self.modulo_counter(number, False)
        print("counter ", self.counter)
    
    def modulo_counter(self, number, is_positive):
        if is_positive:
            total = self.counter+number
            print("total", total)
            divided = total / 100
            print("divided", divided)
            self.zeroes += math.floor(divided)
            self.counter = (divided - math.floor(divided))*100
        else:
            total = self.counter - number
            divided = (total / 100)*-1
            #print(divided)
            if divided >=0 and divided < 1: # We need to catch when we go "down" to zero
                self.zeroes += 1
            self.zeroes += math.floor(divided)
            self.counter = (divided - math.floor(divided))*100

                
            
        
    
    def output(self):
        print(self.zeroes)
    


def main(file):
    counter = Counter()

    with open (file) as f:
        for line in f:
            counter.read_line(line.strip())
    counter.output()

#main("day1Input.txt")
main("test.txt")




