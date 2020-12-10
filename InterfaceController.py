class InterfaceController:
	interface = {
		'1': {'name':'Оценка монет1', 'func': 'f'},
		'2': {'name':'Оценка монет2', 'func': 'f'},
		'3': {'name':'Оценка монет3', 'func': 'f'},
		'4': {'name':'Оценка монет4', 'func': 'f'},
		'5': {'name':'Оценка монет4', 'func': 'f'},
		'6': {'name':'Оценка монет4', 'func': 'f'},
		'7': {'name':'Ценные монеты', 'func': 'f'},
		'8': {'name':'О программе', 'func': 'about_us'},
		'0': {'name':'Выход из программы', 'func': 'exit'},
	}

	def getInterface(self):
		for id, characters in self.interface.items():
			print(f"{id}: {characters['name']}")


