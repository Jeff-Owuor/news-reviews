import unittest

from application.articles_model import  News_article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the news_source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = News_article("Tragedy after Audi R8 crashed into tree in Oldbury Road in Smethwick","https://i2-prod.birminghammail.co.uk/incoming/article23840558.ece/ALTERNATES/s1200/0_IMG-1624.jpg","2022-05-02T08:49:25Z","https://www.birminghammail.co.uk/black-country/man-dies-audi-r8-crash-23840538")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,News_article))


if __name__ == '__main__':
    unittest.main()