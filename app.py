from flask import Flask, render_template, request
from cep import get_cep_address
from models import user as user_model

app = Flask(__name__)

@app.route('/create', methods=('GET', 'POST'))
def create():

    if request.method == 'POST': 
        
        name = request.form['name']
        last_name = request.form['last_name']
        cep = request.form['cep']

        user = {
            'name': name,
            'last_name': last_name,
            'cep': cep
        }

        address_response = get_cep_address(user['cep'])

        if address_response['status'] == True: 
            address = address_response['data']
            user['address'] = address
            user_model.save(user)
            return render_template('user.html', user=user)
        
        else: 
            error = address_response['message']
            return render_template('create.html', error=error)

    else: 
        return render_template('create.html')

if __name__ == "__main__":
    app.run(debug=True)