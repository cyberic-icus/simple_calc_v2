"""

В этом модуле хранятся вспомогательные функции и данные.

"""
import math

info = {
	'+':': Сложение.',
	'-':': Вычитание.',
	'*':': Умножение.',
	'/':': Деление.',
	'cos(<выражение>)':':  косинус.',
	'sin(<выражение>)':': синус.',
	'tg(<выражение>)':': тангенс.',
	'ctg(<выражение>)':': котангенс.',
	'ceil(<выражение>)':'округление до ближайшего большего числа.',
	'fabs(<выражение>)':'модуль <выражение>.',
	'factorial(<выражение>)':'факториал числа <выражение>.',
	'floor(<выражение>)':'округление вниз.',
	'trunc(<выражение>)':'усекает значение <выражение> до целого.',
	'exp(<выражение>)':'e в степени <выражение>.',
	'log10(<выражение>)':'логарифм <выражение> по основанию 10.',
	'log2(<выражение>)':'логарифм <выражение> по основанию 2.',
	'sqrt(<выражение>)':'квадратный корень из <выражение>.',
	'acos(<выражение>)':'арккосинус <выражение>. В радианах.',
	'asin(<выражение>)':'арксинус <выражение>. В радианах.',
	'atan(<выражение>)':'арктангенс <выражение>. В радианах.',
	'degrees(<выражение>)':'конвертирует радианы в градусы.',
	'radians(<выражение>)':'конвертирует градусы в радианы.',
	'cosh(<выражение>)':'вычисляет гиперболический косинус.',
	'sinh(<выражение>)':'вычисляет гиперболический синус.',
	'tanh(<выражение>)':'вычисляет гиперболический тангенс.',
	'acosh(<выражение>)':'вычисляет обратный гиперболический косинус.',
	'asinh(<выражение>)':'вычисляет обратный гиперболический синус.',
	'atanh(<выражение>)':'вычисляет обратный гиперболический тангенс.',
	'gamma(<выражение>)':'гамма-функция <выражение>.',
	'lgamma(<выражение>)':'натуральный логарифм гамма-функции <выражение>.',
	'Число pi':': 3.141592653589793',
	'Число e':': 2.718281828459045',
}

def sum(a,b): return a + b
def sub(a,b): return a - b
def mul(a,b): return a * b
def div(a,b):
	if b != 0: return a / b
	else: return None

def sqrt(a): return math.sqrt(a)
def sin(a): return math.sin(a)
def cos(a): return math.cos(a)
def tg(a): return math.tan(a)
def ctg(a): return math.atan(a)
def ceil(a): return math.ceil(a)
def fabs(a): return math.fabs(a)
def factorial(a): return math.factorial(a)
def floor(a): return math.floor(a)
def trunc(a): return math.trunc(a)
def exp(a): return math.exp(a)
def expm1(a): return math.expm1(a)
def log1p(a): return math.log1p(a)
def log10(a): return math.log10(a)
def log2(a): return math.log2(a)
def sqrt(a): return math.sqrt(a)
def acos(a): return math.acos(a)
def asin(a): return math.asin(a)
def atan(a): return math.atan(a)
def degrees(a): return math.degrees(a)
def radians(a): return math.radians(a)
def cosh(a): return math.cosh(a)
def sinh(a): return math.sinh(a)
def tanh(a): return math.tanh(a)
def acosh(a): return math.acosh(a)
def asinh(a): return math.asinh(a)
def atanh(a): return math.atanh(a)
def gamma(a): return math.gamma(a)
def lgamma(a): return math.lgamma(a)

binary_operators = {
	'+' : sum,
	'-' : sub,
	'*' : mul,
	'/' : div,
}
actions_dict = {
	'#' : sin,
	'$' : cos,
	'@' : tg,
	'!' : ctg,
	';' : ceil,
	':' : fabs,
	'%' : factorial,
	'^' : floor,
	'&' : trunc,
	'~' : exp,
	'<' : expm1,
	'>' : log1p,
	'.' : log10,
	',' : log2,
	'[' : sqrt,
	']' : acos,
	'{' : asin,
	'}' : atan,
	'_' : degrees,
	'|' : radians,
}

def replacer(exp):
	"""
	Заменяет слова-обозначения функций на удобные в обращении символы

	input: str
	output: str

	cos(1) --> $(1)

	"""
	for i in range(exp.count(' ')):
		exp = exp.replace(' ', '')
	exp = exp + ' '
	exp = exp.replace('pi', '3.141592653589793').replace('e', '2.718281828459045').replace('()', '0').replace('--','+')
	for symbol, function in actions_dict.items():
		exp = exp.replace(f'{function.__name__}', f'{symbol}', )
		
	return exp



