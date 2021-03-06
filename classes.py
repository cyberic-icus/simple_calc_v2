from exceptions import NotPairedBracketError, LettersFoundError
from string import ascii_letters
import functions

class ExpressionValidator:
	"""
	Проверяет введеное выражение на парность скобов и латинские буквы.

	"""
	def __init__(self, expression):
		self.expression = expression


	def _count_matches(self, expression, match):
		"""
		Считает количество вхождений в строке

		"""
		counter = 0
		for element in expression:
			if element == match:
				counter += 1
		return counter

	
	def _are_brackets_paired(self):
		"""
		Считает количество открывающихся и закрывающихся скобок, бросает исключение если есть скобка без пары.

		"""
		if self._count_matches(self.expression, '(') != self._count_matches(self.expression, ')'):
			raise NotPairedBracketError
		else:
			pass

	def _are_there_letters(self):
		"""
		Проверяет есть ли латинские буквы в веденном выражении, бросает исключение если есть в выражении.

		"""
		for char in self.expression:
			if char in ascii_letters:
				raise LettersFoundError
		else:
			pass

	def check(self):
		"""
		Мейн интерфейс, просто прогоняет проверочку по методам, если не все ок - выдает эксепшн.

		"""
		self._are_brackets_paired()
		self._are_there_letters()

class TokenCreator:
	"""
	Создает нормальные для обработки токены из выражения.

	"""
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
				z.append(float(a))
				for i in tokens[cb+1:]:
					z.append(i)

				return z

	def _replace_all_minsum_wnegative(self, tokens):
		"""
		Заменяет разбитые отрицательные числа на реальные отрицательные числа во всем выражении и убирает скобки.

		"""
		neg_num = self._count_neg_nums(tokens)

		for _ in range(neg_num):
			tokens = self._replace_minusnum_wnegative(tokens)
		return tokens

	def _tokenize_expression(self):
		"""
		Создаем токены из выражения, помещенного в конструктор.

		"""
		tokens = []
		fp, lp = (None, None)

		for i,char in enumerate(self.expression):
			if char.isdigit() and fp is None:
				fp = i
			elif not char.isdigit() and char != '.':
				lp = i
				if self.expression[fp:lp]:
					tokens.append(float(self.expression[fp:lp]))
				tokens.append(char)
				fp, lp = (lp+1, None)

		return self._replace_all_minsum_wnegative(tokens[:len(tokens)-1])

	def _count_neg_nums(self, tokens):
		"""
		Считаем количество отрицательных чисел

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

class Counter:
	"""
	Основной класс для счета выражений.

	"""
	def __init__(self, expression):
		self.expression = expression
		self.tokens = TokenCreator(expression).get_tokens()

	def _find(self,tokens, match):
		"""
		Ищем первое вхождение элемента и возвращаем индекс.

		"""
		for index, element in enumerate(tokens):
			if match == element:
				return index

	def _rfind(self,tokens, match):
		"""
		Ищем Последнее вхождение элемента и возвращаем индекс.

		"""
		for index, element in enumerate(tokens[::-1]):
			if match == element:
				return len(tokens)-index-1

	def _count_nonbracket_exp(self, tokens):
		"""
		Считает простейшие выражения без скобок.

		"""
		for operator, function in functions.binary_operators.items():
			if self._find(tokens, operator) is not None:
				left = tokens[:self._find(tokens, operator)]
				right = tokens[self._find(tokens, operator)+1:]

				if len(left)==1 and len(right)==1:
					return function(
						left[0],
						right[0]
					)
				elif len(left)==1 and type(left[0]) is float :
					return function(
						left[0],
						self._count_nonbracket_exp(right)
					)
				elif len(right)==1 and type(right[0]) is float:
					return function(
						self._count_nonbracket_exp(left),
						right[0]
					)
				else:
					return function(
						self._count_nonbracket_exp(left),
						self._count_nonbracket_exp(right),
					)
	def _count_exp(self, tokens):
		"""
		Считает выражения со скобками

		"""
		if tokens.count('(') != 0:
			for _ in range(tokens.count('(')):
				deepest_opened_bracket = self._rfind(tokens, '(')
				deepest_closed_bracket = self._find(tokens[deepest_opened_bracket:], ')')

				before = tokens[:deepest_opened_bracket]
				bracketed_exp_result = self._count_nonbracket_exp(tokens[deepest_opened_bracket+1:deepest_opened_bracket+deepest_closed_bracket])
				after = tokens[deepest_opened_bracket+deepest_closed_bracket+1:]

				tokens = tokens[:deepest_opened_bracket]
				tokens.append(bracketed_exp_result)

				for element in after:
					tokens.append(element)

				return self._count_nonbracket_exp(tokens)
		else:
			return self._count_nonbracket_exp(tokens)



	def get_result(self):
		"""
		Выдает результат

		"""
		tokens = self.tokens
		try:
			result = self._count_exp(self.tokens)
			return result
		except Exception:
			return None