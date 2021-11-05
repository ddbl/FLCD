from Scanner import *


def main():
    fileName = "p1err.txt"
    exceptionMessage = ""
    st = SymbolTable()
    pif = ProgramInternalForm()
    scanner = Scanner(st, pif)

    with open(fileName, 'r') as file:
        lineCounter = 0
        for line in file:
            lineCounter += 1
            tokens = re.findall(r"[A-Za-z0-9]+|\S", line)  #scanner.tokenize(line.strip())
            extra = ''
            for i in range(len(tokens)):
                if tokens[i] in scanner.rwords + scanner.separators + scanner.operators:
                    if tokens[i] == ' ':  # ignore adding spaces to the pif
                        continue
                    pif.add(tokens[i], -1)
                elif scanner.is_identifier(tokens[i]):
                    if st.find(tokens[i]) is None:
                        id = st.insert(tokens[i])
                        pif.add("id", id)
                elif scanner.is_constant(tokens[i]):
                    const = st.insert(extra + tokens[i])
                    pif.add("const", const)
                else:
                    exceptionMessage += 'Lexical error at token ' + tokens[i] + ' at line ' + str(lineCounter) + "\n"

    with open('st.out', 'w') as writer:
        writer.write(str(st))

    with open('pif.out', 'w') as writer:
        writer.write(str(pif))

    if exceptionMessage == '':
        print("Lexically correct")
    else:
        print(exceptionMessage)


if __name__ == '__main__':
    main()
