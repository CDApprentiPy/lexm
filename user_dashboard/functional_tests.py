from selenium import webdriver
import unittest

class NewTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_if_page_loads(self):
        self.browser.get('http://localhost:8000')
        print self.browser.title
        self.assertIn('Home', self.browser.title)
        self.fail('Not loading!!!')

if __name__ == '__main__':
    unittest.main()
