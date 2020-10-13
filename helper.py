import re
import json, ast

def is_headers_supported(headers):
    if(headers == 'application/json'):
        return True
    else:
        return False

def validate_request_body(request):

    UUID_PATTERN = re.compile(r'^[\da-f]{8}-([\da-f]{4}-){3}[\da-f]{12}$', re.IGNORECASE)

    if('account_id' not in request 
        or request['amount'] == None
        or isinstance(request['amount'],str) 
        or isinstance(request['account_id'],str) == False 
        or UUID_PATTERN.match(request['account_id']) == None):
        return dict({'status': 400})
    else:
        return dict({'status': 200})
