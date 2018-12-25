import rows
import json


def lerArquivo():
	s = '../players_br.txt'
	with open(s) as _file:
	    # resultado = _file.read()
	    resultado = json.dumps( _file.read(), indent=4, ensure_ascii=False)
	return resultado


def t_rows(data):
	# data = [{'name': 'Álvaro Justen', 'age': 30},
	#         {'name': 'Another Guy', 'age': 42},]
	table = rows.import_from_dicts(data)

	for person in table:
	    # namedtuples are returned for each row
	    print_person(person)

def print_person(person):
    print('{} is {} years old.'.format(person.name, person.age))

# print(type(lerArquivo()))

FILENAME="../players_br.txt"

rows convert $FILENAME.txt $FILENAME.xlsx
# t_rows()
