import os;
class InterfaceController:
	interface = {
		'1': {'name':'Расписание археологических выставок', 'func': 'rasp_table'},
		'2': {'name':'', 'func': 'f'},
		'3': {'name':'Ордена и медали Украины с 1901г. по 1960г.', 'func': 'falerist_uk'},
		'4': {'name':'Гербы Украины с 1901г. по 1960г.', 'func': 'herbs_uk'},
		'5': {'name':'Оборудование и снаряжения для археологии', 'func': 'f'},
		'6': {'name':'Военная археология Украины с 1901г. по 1960г.', 'func': 'military_uk'},
		'7': {'name':'Ценные монеты Украины', 'func': 'coins_uk'},
		'8': {'name':'О программе', 'func': 'about_us'},
		'0': {'name':'Выход из программы', 'func': 'quit'},
	}

	def __init__(self, name):
		self.name = name;
	
	def getInterface(self):
		print('//========================================\\\\');
		print(self.name);
		print('\\\\========================================//');

		for id, characters in self.interface.items():
			print(f"{id} > {characters['name']}");

		self.selectInterface();

	# Функция для очистки консоли от старой информации
	def clearConsole(self):
		print('Для продолжения нажмиет любую клавишу');
		input();
		os.system('clear');
		self.getInterface();

	# Функция для выбора пункта меню. Используется рекурсия для 
	def selectInterface(self):
		try:
			self.selectMenu = input('\r\nВыберите пункт меню >>> ');
			print(self.interface[self.selectMenu]['func']());
		except KeyError:
			print('Такого пункта меню не существует, повторите ввод:')
			self.selectInterface();

	def exit(self):
		self.clearConsole();
		print('Программа завершена');


