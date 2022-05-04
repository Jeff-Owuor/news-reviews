import unittest
from application.source_model import News_source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news_source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = News_source("Associated Press","bbc-news","This is breaking at the moment")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,News_source))


if __name__ == '__main__':
    unittest.main()