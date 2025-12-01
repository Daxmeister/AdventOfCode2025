class Counter():
    def __init__(self):
        self.counter = 50
        self.zeroes = 0
    
    def read_line(self, line):
        letter = line[0]
        number = int(line[1:])

        if letter == "R":
            self.counter = (self.counter + number) % 100
        else:
            self.counter = (self.counter - number) % 100
        if self.counter == 0:
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