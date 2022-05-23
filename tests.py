import unittest
from config import app
from routes import UserView

class test_View(unittest.TestCase):
    
    def test_userview(self):
        uv=UserView
        self.assertEqual(uv.page_size, 5, "page_size = %s instead of 5" % (uv.page_size) ) 
        self.assertEqual(uv.column_hide_backrefs, False, "column_hide_backrefs = %s instead of True" % (uv.column_hide_backrefs) )

if __name__ == '__main__':
    unittest.main()
