class Element:
    def __init__(self, symbol: str, arity: int):
        self.symbol = symbol
        self.arity = arity


class LogicElement(Element):
    def __init__(self, symbol: str, arity: int):
        super().__init__(symbol, arity)

    @staticmethod
    def neg():
        return LogicElement('¬', 1)

    @staticmethod
    def conj():
        return LogicElement('∧', 2)

    @staticmethod
    def disj():
        return LogicElement('∨', 2)

    @staticmethod
    def impl():
        return LogicElement('→', 2)

    @staticmethod
    def iff():
        return LogicElement('↔', 2)


class NonLogicElement(Element):
    def __init__(self, symbol: str, arity: int):
        super().__init__(symbol, arity)


class Function(NonLogicElement):
    def __init__(self, symbol: str, arity: int):
        super().__init__(symbol, arity)


class Constant(Function):
    def __init__(self, symbol: str):
        super().__init__(symbol, arity=0)


class Predicate(NonLogicElement):
    def __init__(self, symbol: str, arity: int):
        super().__init__(symbol, arity)


class Statement(Predicate):
    def __init__(self, symbol: str):
        super().__init__(symbol, arity=0)


class Variable(NonLogicElement):
    def __init__(self, symbol: str):
        super().__init__(symbol, arity=0)