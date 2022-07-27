import sqlite3

def save(user):
	''' Salvar usuário '''

	conn = sqlite3.connect('database.db')

	name = user['name']
	last_name = user['last_name']
	cep = user['cep']
	street = user['address']['logradouro']
	district = user['address']['bairro']
	city = user['address']['localidade']
	state = user['address']['uf']

	sql = "insert into users (name, last_name, cep, street, district, city, state) \
		values ('" + name + "', '" + last_name + "', '" + cep +"', \
			'" + street + "', '" + district + "', '" + city + "', '" + state + "')"

	print(sql)

	conn.execute(sql)

	conn.commit()

	conn.close()
