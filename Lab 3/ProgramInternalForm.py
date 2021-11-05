class ProgramInternalForm:
    def __init__(self):
        self.values = []

    def add(self, token, position):
        self.values.append((token, position))

    def __str__(self):
        output = ""
        for pair in self.values:
            output += pair[0] + " -> " + str(pair[1]) + "\n"
        return output
