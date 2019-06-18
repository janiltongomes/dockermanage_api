#import string
import unittest
import sys
import json



class TestContainers(unittest.TestCase):

    @unittest.skipIf('docker' not in sys.modules, "Requires module Docker in python")
    def test_get_containers_list(self):
        from application import app
        request, response = app.test_client.get('/api/containers/list')
        self.assertEqual(response.status, 200, "Should be http code 200")
        dataResponse = json.loads(response.text)
        verifyResponseData = True if 'data' in dataResponse else False
        self.assertEqual(verifyResponseData, True)

if __name__ == '__main__':
    unittest.main()
