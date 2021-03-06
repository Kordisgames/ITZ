import os;
class InterfaceController:

	def __init__(self, name):
		self.name = name;
		self.interface = {
			'1': {'name':'Расписание археологических выставок', 'func': 'rasp_table'},
			'2': {'name':'Оборудование и снаряжения для археологии', 'func': 'equipment'},
			'3': {'name':'Боны Украины с 1970г. по 2005г.', 'func': 'bones_uk'},
			'4': {'name':'Ордена и медали Украины', 'func': 'falerist_uk'},
			'5': {'name':'Гербы Украины', 'func': 'herbs_uk'},
			'6': {'name':'Военная археология Украины', 'func': 'military_uk'},
			'7': {'name':'Ценные монеты Украины', 'func': 'coins_uk'},
			'8': {'name':'О программе', 'func': 'about_us'}, # +
			'0': {'name':'Выход из программы', 'func': 'quit'}, # +
		}
	def getInterface(self):
		print('//======================================================================\\\\')
		print(self.name);
		print('\\\\======================================================================//')

		for id, characters in self.interface.items():
			print(f"{id} > {characters['name']}");

		self.selectInterface();

	# Функция для очистки консоли от старой информации
	def clearConsole(self):
		print('\r\n>>> Для продолжения нажмиет любую клавишу _');
		input();
		os.system('clear');

	# Функция для выбора пункта меню. Используется рекурсия для 
	def selectInterface(self):
		try:
			self.selectMenu = input('\r\nВыберите пункт меню >>> ');
			print();
			functionx = getattr(self, self.interface[self.selectMenu]['func']);
			functionx();
		except KeyError:
			print('Такого пункта меню не существует, повторите ввод:')
			self.selectInterface();

	def quit(self):
		print('Вы вышли из программы. Чтобы открыть справочник снова - запустите программу заново');
		self.clearConsole();

	def about_us(self):
		print('//======================================================================\\\\')
		print(self.name);
		print('| Автор: Нестеренко Вячеслав Юрьевич                                     |');
		print('| Версия программы: v0.0.17a                                             |');
		print('| Email: kordis.games@gmail.com                                          |');
		print('\\\\======================================================================//')
		self.clearConsole();
		self.getInterface();

	def rasp_table(self):
		self.raspisanie = [
			{'date': ['23.01.2021', '23.01.2021'], 'name': '\"Украина самоцветная\"', 'organizate': 'Природоведческий музей НАН Украины', 'address': 'г. Киев, м. Театральная, ул. Богдана Хмельницкого, 15.'},
			{'date': ['14.12.2018', '01.02.2019'], 'name': ' находок, полученных в результате работ археологических экспедиций во время полевого сезона 2018', 'organizate': 'Харьковский национальный университет имени В. Н. Каразина', 'address': 'площадь Свободы 4, 61022, Харьков'}
		]

		for item in self.raspisanie:
			print('|========================================================================|')
			print(f"C {item['date'][0]} до {item['date'][1]} {item['organizate']} организовывает выставку {item['name']}.\r\nАдрес музея: {item['address']}");
		
		self.clearConsole();
		self.getInterface();

	def equipment(self):
		self.text = """
Археологу во время раскопок всегда нужно иметь свой собственный небольшой набор инструментов, просто для того, чтобы под рукой всегда был знакомый инструмент. Вот содержимое этого набора, который должен находится в рюкзаке каждого археолога.

1. Ромбовидный шпатель (вид штукатурной лопатки), истинно археологический инструмент. В Соединенных Штатах широко распространена марка «Маршаллтаун» с одним лезвием и рукояткой. От дешевых заменителей отказываюсь. Эта лопатка является многосторонним инструментом для раскрытия небольших предметов или снятия почвы возле небольших объектов, таких как очаги. В руках специалиста это также замечательный «отскребывающий» инструмент, идеальный для обнаружения темных контуров столбов или сложных стратиграфических слоев на стенках траншей. Для удобства при ношении есть кобура.
2.Небольшая кисточка для чистки.

3. Нож для колки льда или набор зубочисток для тонких раскопочных работ, таких как очистка костей в почве. Некоторые раскопщики предпочитают самодельные палочки из бамбука, говорят, они более деликатны в работе.
4. Три или четыре кисти шириной 50 миллиметров или менее необходимы для тонкой очистки.
5. Десятиметровая рулетка. Желательно носить с собой свою собственную, потому что другие рулетки всегда кем-то используются. Сейчас при большинстве раскопок измерения ведутся в метрической системе, поэтому и рулетка должна быть соответствующей.
6. Карандаши, резинки, чернильные ручки для маркировки артефактов.
7. Пластиковые пакеты различных размеров с замками-молниями. Никуда без них!
8. Не забудьте шляпу с широкими полями, тент, солнечные очки, хорошие крепкие ботинки, а также перчатки и наколенники, если вы чувствуете, что они вам понадобятся. Если требуются строительные каски, их вам выдадут. Желательны повязки на голову.
9. Все более обычным становится легкий портативный компьютер.""";
		print(self.text)
		self.clearConsole();
		self.getInterface();
	
	def bones_uk(self):
		self.bone = [
			{'name': 'Карбованцы', 'nominal': '1 000', 'period': ['1992', '1995'], 'price': '26'},
			{'name': 'Карбованцы', 'nominal': '1 000 000', 'period': ['1992', '1995'], 'price': '890'},
			{'name': 'Карбованцы', 'nominal': '50 000', 'period': ['1992', '1995'], 'price': '120'},
		]
		print('|========================================================================|')
		for item in self.bone:
			print(f"{item['name']} номиналом в {item['nominal']} периода {item['period'][0]}-{item['period'][1]}г. стоят ~{item['price']}грн.");

		self.clearConsole();
		self.getInterface();

	def military_uk(self):
		print('|========================================================================|')
		print('Раздел справочника находится в разработке...')
		self.clearConsole();
		self.getInterface();
	
	def herbs_uk(self):
		self.herbs = [
			{'name':'Герб г.Винница', 'size': ['19', '21'], 'material': 'медь золото, красное дерево, краски на натуральной основе', 'year': '1939', 'price': '3699'},
		]
		print('|========================================================================|')
		for item in self.herbs:
			print(f"{item['name']} сделан из таких материалов: {item['material']}, размер герба составляет {item['size'][0]}см. по ширине и {item['size'][1]}см. в высоту. Герб датируется {item['year']} годом, и на сегодняшний день его ориентировочная стоимость составляет ~{item['price']}грн.");

		self.clearConsole();
		self.getInterface();
	
	def falerist_uk(self):
		print('|========================================================================|')
		print('Раздел справочника находится в разработке...')
		self.clearConsole();
		self.getInterface();

	def coins_uk(self):
		print('|========================================================================|')
		print('Раздел справочника находится в разработке...')
		self.clearConsole();
		self.getInterface();