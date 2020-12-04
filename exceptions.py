class NotPairedBracketError(Exception):
	def __str__(self):
		return "Brackets are not paired."

class LettersFoundError(Exception):
	def __str__(self):
		return "Letters found."

class EmptyBracketsError(Exception):
	def __str__(self):
		return "Empty brackets found."