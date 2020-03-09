import unittest
import sys
sys.path.append('.')
from src import app as my_file
my_obj = my_file.CustomCollector


class TestStringMethods(unittest.TestCase):


    def test_method_fail( self ):
        x, y = my_obj.url_resp(self, URL="https://httpstat.us/503")
        print("x=== {}, y===== {}".format(x,y))
        print("---Test 1")

    def test_method_success( self ):
        x, y = my_obj.url_resp(self, URL="https://httpstat.us/200")
        print("x=== {}, y===== {}".format(x,y))
        print ( "---Test 2" )

    def test_method_metrics_status( self ):
        x = my_file.metrics().status_code
        print(x)
        print ( "---Test 3" )

    def test_method_api_response ( self ) :
        response = my_file.app.test_client().get('/metrics')
        self.assertEqual ( response.status_code , 200 )
        print("API Response Code:", response.status_code )
        print ( "---Test 4" )

    def test_method_collector_200 ( self ) :
        x , y = my_file.CustomCollector.url_resp(self, URL="https://httpstat.us/200")
        print("x=== {}, y===== {}".format(x,y))
        print ( "---Test 5" )

    def test_method_collector_503 ( self ) :
        print(my_file.REGISTRY.register(my_file.CustomCollector()))
        print ( "---Test 6" )

if __name__ == '__main__':
    unittest.main()