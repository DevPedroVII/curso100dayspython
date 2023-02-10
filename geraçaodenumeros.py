def gerar_telefone():
    """
    Gera um numero de telefone aleatorio
    """
    from random import randint
    numero = str(randint(100000000, 999999999))
    return f'({numero[:2]}) {numero[2:7]}-{numero[7:]}'


def gerar_nome():
    """
    Gera um nome aleatorio
    """
    from random import choice
    nome = choice(['Joao', 'Maria', 'Jose', 'Eduardo', 'Sergio', 'Rafael', 'Paulo', 'Mateus','Lucas', 'Guilherme',
                   'Felipe', 'Arthur', 'Heitor', 'Bernardo', 'Davi', 'Thiago', 'Pedro', 'Gabriel', 'Enzo', 'Lucas',
                   'Matheus', 'Rafael', 'Heitor', 'Enzo Gabriel', 'Felipe', 'Samuel', 'Guilherme', 'Joaquim', 'Nicolas',
                    'Gustavo', 'Lorenzo'])
