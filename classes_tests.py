from classes import TokenCreator, ExpressionValidator, Counter
from exceptions import NotPairedBracketError, LettersFoundError
import unittest

class TestTokenCreator(unittest.TestCase):
    def test_tokenizing(self):
        expressions = (
            '(-20)+2*(12+(-1))-10',
            '1000*10-124+18+(-1412)',
            '(-2)*(-2)*100',
            '(-14.2)+124.4*0.1-2*(-1.24)'
        )
        results = (
            [-20.0, '+', 2.0, '*', '(', 12.0, '+', -1.0, ')', '-', 10.0],
            [1000.0, '*', 10.0, '-', 124.0, '+', 18.0, '+', -1412.0],
            [-2.0, '*', -2.0, '*', 100.0],
            [-14.2, '+', 124.4, '*', 0.1, '-', 2.0, '*', -1.24],
        )
        for exp, res in zip(expressions, results):
            self.assertEqual(TokenCreator(exp).get_tokens(), res)

class TestExpressionValidator(unittest.TestCase):
    def test_paired_bracket_validation(self):
        expressions = (
            '(-20+2*(12+(-1))-10',
            '1000*10-124+18+-1412)',
            '(-2)*-2)*100',
        )
        for exp in expressions:
            self.assertRaises(NotPairedBracketError, TokenCreator(exp).get_tokens)

    def test_letters_found_validation(self):
        expressions = (
            '(asd-20)+2*(12+dfs(-1))-10',
            '1000*10-zx124+18+(-1412)',
            '(-2)*(-2xcv)*100',
        )
        for exp in expressions:
            self.assertRaises(LettersFoundError, TokenCreator(exp).get_tokens)

    def test_not_paired_bracket_validation(self):
        expressions = (
            '((-20+2*(12+(-1))-10',
            '1000*10-124+18-1412))',
            '(-2)*-2)*100)',
        )

        for exp in expressions:
            self.assertRaises(NotPairedBracketError, TokenCreator(exp).get_tokens)

class TestCounter(unittest.TestCase):
    def test_counting(self):
        exps_res = ( # Спасибо Назарову Никите, за написанные выражения!
            ('4+1', 5),
            ('(-1)*(-1)+5', 6),
            ('4/2', 2),
            ('2/1', 2),
            ('(2*2)/2', 2),
            ('6*(-1)+5', -1),
            ('3+3', 6),
            ('(-1)+1', 0),
            ('0+1+1', 2),
            ('0+(-1)', -1),
        )
       
        for exp in exps_res:
            self.assertEqual(exp[1], Counter(exp[0]).get_result())

    

if __name__ == '__main__':
    unittest.main()