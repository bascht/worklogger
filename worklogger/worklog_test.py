import unittest
import os
from unittest import mock

from worklog import Worklog


@mock.patch('worklogger.Worklog.time',
            mock.PropertyMock(return_value='23:52'))
@mock.patch('worklogger.Worklog.date',
            mock.PropertyMock(return_value='01.02.2014 Saturday'))
class WorklogTest(unittest.TestCase):
    def setUp(self):
        try:
            os.mkdir('data')
            testing = open('data/testing.md', 'w')
            testing.writelines(
                ["* 23:41 first entry\n", "* 23:42 last entry\n"])
            testing.close()
        except FileExistsError:
            print("data directory is dirty.")

        self.worklog = Worklog('data/testing.md')

    def tearDown(self):
        os.remove('data/testing.md')
        os.rmdir('data')

    def test_last(self):
        last = self.worklog.get_last()
        self.assertEqual('* 23:41 first entry\n', last[0])
        self.assertEqual('* 23:42 last entry\n', last[1])

    def test_header(self):
        self.worklog.today(location='MyLocation')
        my_header = self.worklog.get_last(4)
        self.assertEqual('# 01.02.2014 Saturday\n', my_header[0])
        self.assertEqual('\n', my_header[1])
        self.assertEqual('## (23:52 - 16:00)\n', my_header[2])

    def test_append(self):
        self.worklog.append('this is my next')
        my_next = self.worklog.get_last()
        self.assertEqual('* 23:42 last entry\n', my_next[0])
        self.assertEqual('* 23:52 this is my next\n', my_next[1])

if __name__ == '__main__':
    unittest.main()
