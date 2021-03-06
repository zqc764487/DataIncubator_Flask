import os
import io
import app
import unittest
import tempfile

class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, app.app.config['DATABASE'] = tempfile.mkstemp()
        app.app.config['TESTING'] = True
        self.app = app.app.test_client()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(app.app.config['DATABASE'])

    def test_uploadPage(self):
        rv = self.app.get('/')
        print(rv.data)

    def upload(self):
        completePage = str(self.app.post('/upload',
                             data={
                                 'file' : (io.BytesIO(b'my test JPG content'), "testJPG.jpg")},
                             follow_redirects=True).data)
        index = self.findSrc(completePage)
        return completePage[index[0] : index[1]]

    #rough test for just getting the name of uploaded file
    def findSrc(self, s):
        i = s.find('img src="')+10
        j = i + 1
        while 1:
            if s[j]=='"':
                break
            j += 1
        return i, j



    def test_post(self):
        rv = self.upload()
        assert '/static/temp.jpg' in rv

if __name__ == '__main__':
    unittest.main()