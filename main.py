from exceptions import (
						NotPairedBracketError,
						LettersFoundError,
)
from string import ascii_letters
import functions

class ExpressionModifier:
	def __init__(self, expression):
		self.expression = expression

	def _replace_functions_mtbracket_epi(self):
		return functions.replacer(self.expression)

	def modifiy(self):
		return self._replace_functions_mtbracket_epi()

class ExpressionValidator:
	def __init__(self, expression):
		self.expression = expression


	def _count_matches(self, expression, match):
		counter = 0
		for element in expression:
			if element == match:
				counter += 1
		return counter

	
	def _are_brackets_paired(self):
		if self._count_matches(self.expression, '(') != self._count_matches(self.expression, ')'):
			raise NotPairedBracketError
		else:
			pass

	def _are_there_letters(self):
		for char in self.expression:
			if char in ascii_letters:
				raise LettersFoundError
		else:
			pass

	def _are_there_mtbrackets(self):
		counter = 0
		for element in expression:
			if element == match:
				counter += 1
		return counter

	def check(self):
		self._are_brackets_paired()
		self._are_there_letters()

class TokenCreator:
	def _replace_minusnum_wnegative(self, tokens):
		"""
		Ищет минус и  число в скобках и заменяет их вместе со скобками на отрицательное число.

		"""
		ob, cb = (0,0)
		for index, element in enumerate(tokens):
			if element =='(':
				ob = index
			elif element == ')':
				cb = index
			if abs(ob - cb) ==3:
				a = tokens[ob+1:cb][0]+str(tokens[ob+1:cb][1])
				z = tokens[:ob]
				z.append(int(a))
				for i in tokens[cb+1:]:
					z.append(i)

				return z

	def _replace_all_minsum_wnegative(self, tokens):
		neg_num = self._count_neg_nums(tokens)

		for _ in range(neg_num):
			tokens = self._replace_minusnum_wnegative(tokens)
		return tokens

	def _tokenize_expression(self):
		"""
		Создаем токены из выражения, помещенного в конструктор.

		"""
		tokens = []
		x = 0
		for char in self.expression:
			if char.isdigit():
				x = x*10 + int(char)
			else:
				if x != 0:
					tokens.append(x)
				tokens.append(char)
				x = 0
		return self._replace_all_minsum_wnegative(tokens[:len(tokens)-1])

	def _count_neg_nums(self, tokens):
		"""
		Считаем количество отрицательных чисел.
		"""
		neg_num_counter = 0
		for index, element in enumerate(tokens):
				if element =='(' and tokens[index+3]==')':
					neg_num_counter +=1
		return neg_num_counter

	def get_tokens(self):
		"""
		Создаем удобные токены и возвращаем их.

		"""
		self.ExpressionValidator.check()
		return self._tokenize_expression()

	def __init__(self, expression):
		self.expression = expression + ' '
		self.ExpressionValidator = ExpressionValidator(expression)



a = TokenCreator('1+1-(-1)*1231').get_tokens()
print(a)

# class ExpressionModifier:
# 	def __init__(self, expression):
# 		self.expression = expression

# 	def _replace_functions_mtbracket_epi(self):
# 		return functions.replacer(self.expression)

# 	def modifiy(self):
# 		return self._replace_functions_mtbracket_epi()

# # a = ExpressionModifier('1--1+sin(1)+()-1').modifiy()
# # print(a)