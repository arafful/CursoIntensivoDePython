import unittest
from Cap11_name_function import get_nome_formatado


class NamesTestCase(unittest.TestCase):
    """
    Teste
    """

    def test_first_last_name(self):
        """
        Teste
        :return:
        """
        formatted_name = get_nome_formatado('andre', 'rafful')
        self.assertEqual(formatted_name, 'Andre Rafful  ')
        unittest.main()
