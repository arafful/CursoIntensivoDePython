from Cap11_survey import AnonymousSurvey
# Define uma pergunta e cria uma pesquisa
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)
# Mostra a pergunta e armazena as respostas
my_survey.show_questions()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you for everyone wo participated in survey!")
my_survey.show_results()
