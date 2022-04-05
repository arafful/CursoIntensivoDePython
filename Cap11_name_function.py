def get_nome_formatado(nome, sobrenome, meio=''):
    """
    Retorna um nome completo formatado
    :param nome:
    :param sobrenome:
    :return:
    """
    if meio:
        nome_completo = nome + ' ' + meio + ' ' + sobrenome
    else:
        nome_completo = nome + ' ' + sobrenome
    return nome_completo.title()
