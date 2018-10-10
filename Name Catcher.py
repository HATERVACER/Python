o = {"Ярослав"}
while True:
	a = input('Введите имя: ')
	if a in o:
		print ("Снова привет)")
	elif a == ("ЗАКАЛИБАЛ СПРАШИВАТЬ!"):
		while True:
			print('Знаю')
	else:
		print('Привет')
		o.add(a)