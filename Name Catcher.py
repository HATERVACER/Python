# Множество из которого будут браться имена, добавлятся в него.
o = {"Ярослав"}
# Цикл, чтобы программа не закрывалась после первого прохождения цикла
while True:
	# Эта переменная будет спрашивать имя, и записывать имя в себя
	a = input('Введите имя: ')
	# Есть ли во множестве "o" переменная "a" в которую записалось значение введеное в нее
	if a in o:
		# Будет выводится при проверке на "a" в "o"
		print ("Привет, я тебя знаю, ", a)
	# Является ли значение переменной "a" словом "Выход"
	elif a == "Выход":
		# Будет выводится после проверки
		print("Увидимся!")
		# Выход
		break
	# Троллинг, ялвляется ли значение переменной "a" словом "ЗАКАЛИБАЛ СПРАШИВАТЬ!" 
	elif a == "ЗАКАЛИБАЛ СПРАШИВАТЬ!":
		# Цикл
		while True:
			# Вывод в цикле
			print('Знаю')
	# В любом другом случае 
	else:
		# Вывод после подтверждения того что переменная "a" не проверилась всеми другими if'ами
		print('Привет, но я тебя не знаю, ', a)
		# Добавление во множество
		o.add(a)
