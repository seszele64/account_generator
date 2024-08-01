# create api to get random person info


from flask import Flask, jsonify, request, Response
from main2 import table, create_person
from random_info.datatypes import Person

import asyncio
import queue
import threading

app = Flask(__name__)

def run_in_queue(func, *args):
    q = queue.Queue()
    q.put(threading.Thread(target=func, args=args))
    q.get().start()
    return q.get().join()

@app.route('/get_user_agent', methods=['GET'])
def get_user_agent():
    user_agent = request.headers.get('User-Agent')
    return f'User-Agent: {user_agent}'

@app.route('/random_person', methods=['GET'])
def get_random_person():

    person = create_person()

    return jsonify(
        {
            'first_name': person.name.first_name,
            'last_name': person.name.last_name,
            'birthdate': person.birthdate,
            'company_name': person.company.name,
            'company_occupation': person.company.occupation,
            'phone': person.contact.phone,
            'email': person.contact.email,
            'street_name': person.address.street_name,
            'street_number': person.address.street_number,
            'zip_code': person.address.zip_code,
            'city': person.address.city
        }
    )

# proxy -> get ip address

# phone api -> confirming
## show all my orders
from phone import api as phone_api

@app.route('/my_orders', methods=['GET'])
def get_my_orders():
    import json
    # Make a request to get user balance
    return phone_api.get_orders()
    
    
## show status of my order, by order id
@app.route('/order_status/<order_id>', methods=['GET'])
def get_order_status(order_id):
    # Make a request to get user balance
    order_status = phone_api.async_get_activation_status(order_id)
    # order_status is string, make it json, create custom dict
    dict_order_status = {
        'order_id': order_id,
        'status': order_status
    }

    return jsonify(dict_order_status)


# buy phone number
@app.route('/buy_phone_number/<country>/<product>', methods=['GET'])
def get_phone_number(country, product):
    # Make a request to get user balance
    phone_number = phone_api.async_buy_activation_number(country, product)
    return jsonify(phone_number)

# login / password api -> returns the end user data so one can login to the website
@app.route('/login_data', methods=['GET'])
def get_login_data():
    pass
    # Make a request to get user balance
    # login_data = api.get_login_data()
    # return jsonify(login_data)

if __name__ == '__main__':
    app.run(debug=True)