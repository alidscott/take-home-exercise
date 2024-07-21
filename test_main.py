import unittest
from unittest.mock import patch
from io import StringIO
from main import main



class TestSum(unittest.TestCase):

    @patch('builtins.input', side_effect=['f', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_invalid_input(self, mock_stdout, mock_input):
        try: 
            main()
        except SystemExit:
            pass
        self.assertEqual(mock_stdout.getvalue(), "Not a valid input. Goodbye!\n")

    @patch('builtins.input', side_effect=['10 * 3', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_bad_operations(self, mock_stdout, mock_input):
        try: 
            main()
        except SystemExit:
            pass
        self.assertEqual(mock_stdout.getvalue(), "Need 2 operands before operator! Now exiting...\n")

    @patch('builtins.input', side_effect=['5 5 5 8 + + -', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_addition_subtraction(self, mock_stdout, mock_input):
        try: 
            main()
        except SystemExit:
            pass
        self.assertEqual(mock_stdout.getvalue(), "-13\n")

    @patch('builtins.input', side_effect=['1 1 -', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_subtract(self, mock_stdout, mock_input):
        try: 
            main()
        except SystemExit:
            pass
        self.assertEqual(mock_stdout.getvalue(), "0\n")

    @patch('builtins.input', side_effect=['2 2 4 * /', 'q'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mult_div(self, mock_stdout, mock_input):
        try: 
            main()
        except SystemExit:
            pass
        self.assertEqual(mock_stdout.getvalue(), "0.25\n")


if __name__ == '__main__':
    unittest.main()