from SymbolTable import SymbolTable

if __name__ == '__main__':
    st = SymbolTable()
    tokens = ["var",
              "\"string constant\"",
              "true",
              "false",
              "var",
              "36542",
              "-7654",]

    for t in tokens:
        st.insert(t)

    for t in tokens:
        print(f"Token found at {st.find(t)}")
