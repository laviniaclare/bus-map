from model import Agency, Route, Trip, StopTime, Stop

import unittest
import routes

####### Tests go here #######


class IntegrationTest(unittest.TestCase):

    def test_load_options(self):
        result = self.client.get('/')
        self.assertIn("Show Routes!", result.data)

    def test_prepare_routes_for_display(self):
        pass

    def test_get_routes_by_id(self):
        pass


class ModelTest(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
