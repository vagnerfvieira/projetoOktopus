import os

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projeto_oktopus.settings")
django.setup()

import string
import timeit
from random import choice, randint, random

from produtos.models import Produto


class Utils:
    ''' Métodos genéricos. '''
    @staticmethod
    def gen_digits(max_length):
        return str(''.join(choice(string.digits) for i in range(max_length)))


class ProdutoClass:

    @staticmethod
    def criar_produtos(produtos):
        Produto.objects.all().delete()
        aux = []
        for valorUn in valorUns:
            data = dict(
                produto=produtos,
                importado=choice((True, False)),
                #ncm=Utils.gen_digits(8),
                valorUn=valorUn,
                qtde = random() * randint(10,50),
                estoque=randint(10, 200),
            )
            obj = Produto(**data)
            aux.append(obj)
        Produto.objects.bulk_create(aux)


valorUns = (
    1,
    2,
    3,
)

produtos = (
   1
)

tic = timeit.default_timer()

ProdutoClass.criar_produtos(produtos)


toc = timeit.default_timer()

print('Tempo:', toc - tic)