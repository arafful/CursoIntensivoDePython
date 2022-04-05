class AnonymousSurvey():
    """
    Coleta respostas anonimas para uma pesquisa
    """

    def __init__(self, question):
        """
        Armazena uma pergunta e sepreparapara armazenar as respostas
        :param question:
        """
        self.question = question
        self.responses = []

    def show_questions(self):
        """
        Mostra a pergunta da pesquisa
        :return:
        """
        print(self.question)

    def store_response(self, new_response):
        """
        Armazena uma única resposta da pesquisa
        :param new_response:
        :return:
        """
        self.responses.append(new_response)

    def show_results(self):
        """
        Mostra todas as respostas dadas
        :return:
        """
        print("Survey results:")
        for response in self.responses:
            print("- " + response)
