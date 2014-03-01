import unittest
from logger import Logger


class TestBackend:
    @staticmethod
    def get_last():
        return "my_last_line"

    @staticmethod
    def append(log):
        TestBackend.next_line = log


class TestFrontend:
    @staticmethod
    def query(text, suggestion):
        TestFrontend.text = text
        TestFrontend.suggestion = suggestion
        return 'my_next_line'


class LoggerTest(unittest.TestCase):
    def setUp(self):
        self.logger = Logger(TestBackend(), TestFrontend)

    def test_log(self):
        self.logger.log()
        self.assertEqual('my_last_line', TestFrontend.text)
        self.assertEqual('my_next_line', TestBackend.next_line)

if __name__ == '__main__':
    unittest.main()
