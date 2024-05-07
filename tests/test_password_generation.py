# import unittest
# from unittest.mock import patch
# from io import StringIO
# import sys
#
# from passwordGenerator.cli.main import main as cli_main
#
# class TestPasswordGenerator(unittest.TestCase):
#     @patch('sys.argv', ['cli.main', '-t', 'd{4}L{2}l{2}', '-c', '1'])
#     @patch('sys.stdout', new_callable=StringIO)
#     def test_pattern_password_generation(self, mocked_stdout):
#         cli_main()
#         output = mocked_stdout.getvalue().strip()
#         self.assertTrue(len(output) > 0)
#         self.assertTrue(any(char.isdigit() for char in output))  # Проверка на наличие цифр
#         self.assertTrue(any(char.islower() for char in output))  # Проверка на наличие строчных букв
#         self.assertTrue(any(char.isupper() for char in output))  # Проверка на наличие заглавных букв
#
#     @patch('sys.argv', ['cli.main', '-S', 'abcd1234', '-n', '10', '-c', '2'])
#     @patch('sys.stdout', new_callable=StringIO)
#     def test_custom_charset_password_generation(self, mocked_stdout):
#         cli_main()
#         output = mocked_stdout.getvalue().strip().split('\n')
#         self.assertEqual(len(output), 2)  # Должно быть сгенерировано 2 пароля
#         for password in output:
#             self.assertTrue(all(char in 'abcd1234' for char in password))  # Пароли должны состоять только из указанных символов
#
#     @patch('logging.FileHandler')
#     def test_logging_to_file(self, mocked_file_handler):
#         with patch('sys.argv', ['cli.main', '-vvv', '-w']):
#             cli_main()
#             mocked_file_handler.assert_called_with('/path/to/logs.txt')
#
# if __name__ == '__main__':
#     unittest.main()
