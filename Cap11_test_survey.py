import unittest
from Cap11_survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
    """
    Testa se uma única resposta é armazenada de forma apropriada
    """

    def setUp(self):
        """
        Cria uma pesquisa e um conjunto de respostas que poderão ser usados em todos os métodos de testes
        :return:
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Ingles', 'Frances', 'Alemão']

    def test_store_single_response(self):
        """
        Testa se uma única resposta é armazenada de forma apropriada
        :return:
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """
        Testa se tres respostas são armazenadas corretamente
        :return:
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

    if __name__ == '__main__':
        unittest.main()
