__author__ = 'johnburrin'

import unittest
import types
import PywwsRawHandler


class MyTestCase(unittest.TestCase):
    def test_isclass(self):
        """
            Test isclass

        """
        test_class = PywwsRawHandler.PywwsRawHandler
        assert isinstance(test_class, object)

    def test_openfile(self):
        """
            Test File exists
        """
        pywws_observation = PywwsRawHandler.PywwsRawHandler()
        assert isinstance(pywws_observation.open_raw_file, object)

    def test_readfile(self):

        """


        """
        pywws_observation = PywwsRawHandler.PywwsRawHandler()
        pywws_observation.open_raw_file('test_data/2014-02-07.txt')

        assert isinstance(pywws_observation.fo, object)

        pywws_observation.read_raw_line()
        assert isinstance(pywws_observation.data, list)
        pywws_observation.dump_data()

if __name__ == '__main__':
    unittest.main()
