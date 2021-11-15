class FiniteAutomata:
    def __init__(self, Q, E, q0, F, S):
        self.Q = Q
        self.E = E
        self.q0 = q0
        self.F = F
        self.S = S

    def read(self, file_name):
        with open(file_name) as file:
            Q = self.get_line(file.readline())
            E = self.get_line(file.readline())
            q0 = self.get_line(file.readline())[0]
            F = self.get_line(file.readline())

            file.readline()

            S = {}
            for line in file:
                line = line.replace("(", "").replace(")", "").replace("->", "").replace(",", " ").split()
                src = line[0]
                route = line[1]
                dst = line[2]

                if (src, route) in S.keys():
                    S[(src, route)].append(dst)
                else:
                    S[(src, route)] = [dst]

            if not self.validate(Q, E, q0, F, S):
                raise Exception("Wrong input file.")

            return FiniteAutomata(Q, E, q0, F, S)

    @staticmethod
    def get_line(line):
        return line.strip().split(' ')[2:]

    @staticmethod
    def validate(Q, E, q0, F, S):
        if q0 not in Q:
            return False
        for f in F:
            if f not in Q:
                return False
        for key in S.keys():
            state = key[0]
            symbol = key[1]
            if state not in Q:
                return False
            if symbol not in E:
                return False
            for dest in S[key]:
                if dest not in Q:
                    return False
        return True

    def is_dfa(self):
        for k in self.S.keys():
            if len(self.S[k]) > 1:
                return False
        return True

    def is_accepted(self, seq):
        if self.is_dfa():
            crt = self.q0
            for symbol in seq:
                if (crt, symbol) in self.S.keys():
                    crt = self.S[(crt, symbol)][0]
                else:
                    return False
            return crt in self.F
        return False

    def __str__(self):
        return "Q = { " + ', '.join(self.Q) + " }\n" \
                "E = { " + ', '.join(self.E) + " }\n" \
                "q0 = { " + self.q0 + " }\n" \
                "F = { " + ', '.join(self.F) + " }\n" \
                "S = { " + str(self.S) + " } "
