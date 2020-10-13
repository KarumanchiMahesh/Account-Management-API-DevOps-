from flask import Flask, request, jsonify
import pandas as pd
import services, helper
import json, ast

app = Flask(__name__)

@app.route('/amount', methods = ['POST', 'GET'])
def update_amount():
    is_headers_supported = helper.is_headers_supported(request.headers['Content-Type'])
    if(is_headers_supported == False):
        return 'Headers not supported', 415

    arg_check = (request.get_json(force=True))
    arg_check1= ast.literal_eval(json.dumps(arg_check))
    amount = arg_check1.get('amount')
    account_id = arg_check1.get('account_id')
    is_valid_request_body = helper.validate_request_body({'amount': amount, 'account_id': account_id})
    if(is_valid_request_body['status'] == 400):
        return 'Bad request',400

    id = request.json['account_id']
    amount = request.json['amount']
    update_amount_res = services.update_amount_status(id, amount)
    return jsonify({'balance':update_amount_res['balance']}), update_amount_res['status']

@app.route('/balance/<account_id>')
def get_balance(account_id):
    get_balance_res = services.get_account_balance(account_id)
    return jsonify({'balance': get_balance_res['balance']}), get_balance_res['status']

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=8080, debug=True)
