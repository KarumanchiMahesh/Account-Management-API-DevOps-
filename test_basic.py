import unittest
import helper, services


class TestSum(unittest.TestCase):

    def test_header(self):
        headers = 'application/json'
        result = helper.is_headers_supported(headers)
        self.assertEqual(result, True)
        

    def test_nagtive_header(self):
        negative_headers = 'application/xml'
        self.assertEqual(helper.is_headers_supported(negative_headers), False)

    def test_no_account_id(self):
        data = {'account_id':'a40bcc03-6f39-418c-ad0b-97e14f522ec1', 'amount':None}
        request = helper.validate_request_body(data)['status']
        self.assertEqual(request, 400)
    
    def test_no_amount(self):
        data = {'amount': 1}
        request = helper.validate_request_body(data)['status']
        self.assertEqual(request, 400)
    
    def test_wrong_account_id_type(self):
        data = {'account_id':12313, 'amount': 12}
        request = helper.validate_request_body(data)['status']
        self.assertEqual(request, 400)
    
    def test_wrong_amount_type(self):
        data = {'account_id':'a40bcc03-6f39-418c-ad0b-97e14f522ec1', 'amount': '123'}
        request = helper.validate_request_body(data)['status']
        self.assertEqual(request, 400)

    def test_wrong_account_id_format(self):
        data = {'account_id':'aca2', 'amount': 12}
        request = helper.validate_request_body(data)['status']
        self.assertEqual(request, 400)
    
    def test_add_initial_balance(self):
        response = services.update_amount_status('a40bcc03-6f39-418c-ad0b-97e14f522ec9', 10)
        self.assertEqual(response['status'], 200)

    def test_add_balance(self):
        response = services.update_amount_status('a40bcc03-6f39-418c-ad0b-97e14f522ec9', 10)
        self.assertEqual(response['status'], 200)

    def test_deduct_balance(self):
        response = services.update_amount_status('a40bcc03-6f39-418c-ad0b-97e14f522ec9', -10)
        self.assertEqual(response['status'], 200)

    def test_get_balance_existing_account(self):
        response = services.get_account_balance('a40bcc03-6f39-418c-ad0b-97e14f522ec9')
        self.assertEqual(response['status'], 200)
        self.assertEqual(response['balance'], 10)
        
    def test_get_balance_non_existing_account(self):
        response = services.get_account_balance('a40bcc03-6f39-418c-ad0b-97e14f522ec5')
        self.assertEqual(response['status'], 404)

if __name__ == '__main__':
    unittest.main()