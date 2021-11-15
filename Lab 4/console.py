from FiniteAutomata import FiniteAutomata


class Console:
    def __init__(self):
        self.fa = None

    def read_FA(self):
        self.fa = FiniteAutomata.read(FiniteAutomata, r'C:\Facultate\Anul 3\Sem 1\FLCD\Labs\Lab 4\fa.txt')

    def display_all(self):
        print(self.fa)

    def display_states(self):
        print(self.fa.Q)

    def display_alphabet(self):
        print(self.fa.E)

    def display_transitions(self):
        print(self.fa.S)

    def display_final_states(self):
        print(self.fa.F)

    def check_DFA(self):
        print(self.fa.is_dfa())

    def check_accepted(self):
        seq = input()
        print(self.fa.is_accepted(seq))

    def display_menu(self):
        print("1.Read FA from file")
        print("2.Display FA")
        print("3.Display FA States")
        print("4.Display FA Alphabet")
        print("5.Display FA transitions")
        print("6.Display FA final states")
        print("7.Check DFA")
        print("8.Check accepted sequence")

    def run(self):
        cmds = {'1': self.read_FA, '2': self.display_all, '3': self.display_states, '4': self.display_alphabet,
                '5': self.display_transitions, '6': self.display_final_states, '7': self.check_DFA,
                '8': self.check_accepted}
        stop = False
        while not stop:
            self.display_menu()
            print(">>")
            cmd = input()
            if cmd in cmds.keys():
                cmds[cmd]()
            elif cmd == "exit":
                stop = True
            else:
                continue
