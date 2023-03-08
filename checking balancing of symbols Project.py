class Stack(self,Stack,pop,push):
    self.Stack=Stack

def ChechSymbols(input):
    symbolstack= Stack()
    balanced=0
    for symbols in input:
        if symbols in ["[","(","{"]:
            symbolstack.push(symbols)
        else:
            if symbolstack.isEmpty():
               balanced=0
            else:
               topSymbol = symbolstack.pop()
        if topSymbol != symbols:
            balanced=0
        else:
            balanced=1
    return balanced
print(ChechSymbols("([)"))