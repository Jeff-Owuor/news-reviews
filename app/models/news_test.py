import unittest
from news import News_source

class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news_source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_movie = News_source("Associated Press")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,News_source))


if __name__ == '__main__':
    unittest.main()