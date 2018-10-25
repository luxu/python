import rows

def lerArquivo():
	s = 'tabelaRoyale.txt'
	with open(s) as _file:
	    text = _file.read()
	print(text)

lerArquivo()

def t_rows():
	data = [{'name': 'Álvaro Justen', 'age': 30},
	        {'name': 'Another Guy', 'age': 42},]
	table = rows.import_from_dicts(data)

	for person in table:
	    # namedtuples are returned for each row
	    print_person(person)

def print_person(person):
    print('{} is {} years old.'.format(person.name, person.age))

