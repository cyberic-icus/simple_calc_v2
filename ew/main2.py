"""
TODO:
1. Слепить цифры воедино
2. 


"""



exp = '(-20)+2*(12+(-1))-10'
exp1 = '1000*10-124+18+(-1412) '
exp2 = '(-2)*(-2)*100 '
exp3 = '(-3'
exp = exp + ' '

# tokens = []
# x = 0
# for char in exp:
# 	# print(char, char.isdigit())
# 	if char.isdigit():
# 		x = x*10 + int(char)
# 	else:
# 		if x != 0:
# 			tokens.append(x)
# 		tokens.append(char)
# 		x = 0

# tokens = tokens[:len(tokens)-1]
# #print(tokens)


# tokens = ['(','-2',')','+','2','*','(','12','+','(','-1',')',')','-','10']

class ValidTokenCreator:
	global get_tokens


	def get_tokens(self):
		def find(tokens, match):
			for index, element in enumerate(tokens):
				if element == match:
					return index

		def rfind(tokens, match):
			buff = -1
			for index, element in enumerate(tokens):
				if element == match:
					buff = index
			return buff

		tokens = []
		x = 0
		for char in self:
			# print(char, char.isdigit())
			if char.isdigit():
				x = x*10 + int(char)
			else:
				if x != 0:
					tokens.append(x)
				tokens.append(char)
				x = 0

		tokens = tokens[:len(tokens)-1]
		def normalize(tokens):
			ob, cb = (0,0)
			for index, element in enumerate(tokens):
				if element =='(':
					ob = index
				elif element == ')':
					cb = index
				if abs(ob - cb) ==3:
					print(tokens, ob, cb,  "TOKENS")
					a = tokens[ob+1:cb][0]+str(tokens[ob+1:cb][1])
					print(f'{tokens[ob:cb]}')
					#print(int(a))
					z = tokens[:ob]

					print(z, 'AAA')
					#z.extend([int(a)]).extend(tokens[cb+1:])
					print(a)
					z.append(int(a))
					print(z, 'AAA1')
					for i in tokens[cb+1:]:
						z.append(i)
					# print("bef", tokens[:ob])
					# print("aft", tokens[cb+1:])

					print(z, 'AAA2')
					return z
					ob, cb = (0,0)


		neg_num_counter = 0
		for index, element in enumerate(tokens):
				if element =='(' and tokens[index+3]==')':
					neg_num_counter +=1


		for _ in range(neg_num_counter):
			tokens = normalize(tokens)
			print(tokens, "333")

		return tokens

			#print(ob, cb)
			# opened_brace = rfind(tokens, '(')
			# closed_brace = rfind(tokens, ')')
			# print(opened_brace, closed_brace)


	def __init__(self, expression):
		self.expression = expression
		self.tokens = get_tokens(expression + ' ')


a = ValidTokenCreator(exp).tokens
print(a, "A")



