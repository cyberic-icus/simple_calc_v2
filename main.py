from classes import TokenCreator
import functions

class Counter:
	def __init__(self, expression):
		self.expression = expression
		self.tokens = TokenCreator(expression).get_tokens()

	def _find(self,tokens, match):
		for index, element in enumerate(tokens):
			if match == element:
				return index

	def _rfind(self,tokens, match):
		for index, element in enumerate(tokens[::-1]):
			if match == element:
				return len(tokens)-index-1

	def _count_nonbracket_exp(self, tokens): 
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
		tokens = self.tokens
		print(self.tokens)
		return self._count_exp(tokens)
		
a = Counter('5+2*(3+2)').get_result()
print(a)