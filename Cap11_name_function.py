def get_nome_formatado(nome, sobrenome):
    """
    Retorna um nome completo formatado
    :param nome:
    :param sobrenome:
    :return:
    """
    nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()
