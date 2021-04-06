import unittest

from main import Element, LogicElement


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




if __name__ == '__main__':
    unittest.main()
