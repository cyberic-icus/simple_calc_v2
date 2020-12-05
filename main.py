from classes import Counter
from exceptions import NotPairedBracketError, LettersFoundError

if __name__ == '__main__':

	my_input = str(input("Введите ваше выражение:"))
	result = None
	while my_input != 'qqq':
		try:
			result = Counter(my_input).get_result()

			if result is None:
				print('Чето ты не то делаешь....')
			else: print(result)
			my_input = str(input("Введите ваше выражение:"))

		except NotPairedBracketError:
			print('Найдено разное количество открывающихся и закрывающихся скобок.')
			my_input = str(input("Введите ваше выражение:"))
			continue

		except LettersFoundError:
			print('Найдены буквы.')
			my_input = str(input("Введите ваше выражение:"))
			continue

		except Exception as e:
			print('Хз че случилось')
			my_input = str(input("Введите ваше выражение:"))
			continue