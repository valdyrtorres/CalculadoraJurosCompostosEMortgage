def juros_compostos(principal, taxa, periodo):
    """
    Função para calcular juros compostos
    Juros compostos = P (1 + R / 100)t
    Onde,
    P é a quantidade do principal
    R é a taxa e
    T é o período de tempo
    :param principal: float
    :param taxa: inteiro/float
    :param periodo: inteiro
    :return: float (resultado)
    """
    calculo_juros = principal * (pow((1 + taxa / 100), periodo))
    return calculo_juros