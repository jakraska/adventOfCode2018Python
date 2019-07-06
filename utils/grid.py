
class grid:
    data = []
    width = 0
    height = 0

    def __init__(self, width, height, initialFill):
        self.data = [[initialFill] * width for i in range(height)]
        self.width = width
        self.height = height

    def draw(self):
        for x in range(0, self.width):
            output = ''
            for y in range(0, self.height):
                output = output + str(self.data[x][y])
            print output
