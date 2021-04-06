import unittest

from main import Element, LogicElement, NonLogicElement, Function, Constant, Predicate, Statement, Variable


class TestElement(unittest.TestCase):
    def test_init(self):
        a = Element(symbol='*', arity=5)
        self.assertEqual(a.symbol, '*')
        self.assertEqual(a.arity, 5)


class TestLogicElement(unittest.TestCase):
    def test_neg(self):
        n = LogicElement.neg()
        self.assertEqual(n.symbol, '¬')
        self.assertEqual(n.arity, 1)

    def test_and(self):
        n = LogicElement.conj()
        self.assertEqual(n.symbol, '∧')
        self.assertEqual(n.arity, 2)

    def test_or(self):
        n = LogicElement.disj()
        self.assertEqual(n.symbol, '∨')
        self.assertEqual(n.arity, 2)

    def test_impl(self):
        n = LogicElement.impl()
        self.assertEqual(n.symbol, '→')
        self.assertEqual(n.arity, 2)

    def test_iff(self):
        n = LogicElement.iff()
        self.assertEqual(n.symbol, '↔')
        self.assertEqual(n.arity, 2)


class TestNonLogicElement(unittest.TestCase):
    def test_init(self):
        e = NonLogicElement('@', 4)
        self.assertEqual(e.symbol, '@')
        self.assertEqual(e.arity, 4)


class TestFunction(unittest.TestCase):
    def test_init(self):
        f = Function(symbol='f', arity=2)
        self.assertEqual(f.symbol, 'f')
        self.assertEqual(f.arity, 2)


class TestConstant(unittest.TestCase):
    def test_init(self):
        c = Constant(symbol='A')
        self.assertEqual(c.symbol, 'A')
        self.assertEqual(c.arity, 0)


class TestPredicate(unittest.TestCase):
    def test_init(self):
        p = Predicate(symbol='r', arity=3)
        self.assertEqual(p.symbol, 'r')
        self.assertEqual(p.arity, 3)


class TestStatement(unittest.TestCase):
    def test_init(self):
        s = Statement(symbol='p')
        self.assertEqual(s.symbol, 'p')
        self.assertEqual(s.arity, 0)


class TestVariable(unittest.TestCase):
    def test_init(self):
        v = Variable(symbol='x')
        self.assertEqual(v.symbol, 'x')
        self.assertEqual(v.arity, 0)


if __name__ == '__main__':
    unittest.main()
