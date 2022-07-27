import requests

def get_cep_address(cep):

	if len(cep) == 8:
		url = 'https://viacep.com.br/ws/'+ cep +'/json/'
		request = requests.get(url)

		address_data = request.json()

		if 'erro' not in address_data:

			return {
				'status': True,
				'data': address_data
			}
			
		else:
			return {
				'status': False,
				'message': 'Não foi possível obter as informações deste CEP'
			}
	else: 
		return {
			'status': False,
			'message': 'CEP inválido'
		}


