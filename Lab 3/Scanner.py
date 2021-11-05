from SymbolTable import SymbolTable
from ProgramInternalForm import ProgramInternalForm
import re


class Scanner:
    def __init__(self, symbol_table, pif):
        self.symbol_table = symbol_table
        self.pif = pif
        self.operators = ['+', '-', '*', '/', '%', '=', '<', '>', '<=', '=', '>=', '!=', '==', '!']
        self.separators = ['[', ']', '{', '}', ':', ';', ' ', '(', ',', ')']
        self.rwords = ['array', 'char', 'const', 'do', 'else', 'if', 'int', 'of', 'input', 'output', 'for', 'break',
                       'then', 'var', 'string', 'boolean', 'true', 'false', 'while', 'typedef', 'start!', 'end!']

    def get_string_token(self, line, index):
        token = ''
        quotes = 0

        while index < len(line) and quotes < 2:
            if line[index] == '\'':
                quotes += 1
            token += line[index]
            index += 1

        return token, index

    def tokenize(self, line):
        token = ''
        index = 0
        tokens = []
        while index < len(line):
            if self.is_part_of_operator(line[index]):
                if token:
                    tokens.append(token)
                token, index = self.get_string_token(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] == '\'':
                if token:
                    tokens.append(token)
                token, index = self.getStringToken(line, index)
                tokens.append(token)
                token = ''  # reset token

            elif line[index] in self.separators:
                if token:
                    tokens.append(token)
                token, index = line[index], index + 1
                tokens.append(token)
                token = ''  # reset token

            else:
                token += line[index]
                index += 1
        if token:
            tokens.append(token)
        return tokens

    def is_part_of_operator(self, char):
        for op in self.operators:
            if char in op:
                return True
        return False

    def is_identifier(self, token):
        return re.match(r'^[a-z]([a-zA-Z]|[0-9])*$', token) is not None

    def is_constant(self, token):
        return re.match(r'^(0|-?[1-9][0-9]*)$|^\'.\'$|^\'.*\'$', token) is not None
