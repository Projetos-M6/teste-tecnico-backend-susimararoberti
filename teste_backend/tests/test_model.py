from django.test import TestCase

from teste_backend.models import Campos


class CamposModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.cnab = (
            "3201903010000019200845152540736777****1313172712MARCOS PEREIRAMERCADO DA AVENIDA")

        cls.data = {
            "tipo": cls.cnab[:1],
            "data": cls.cnab[1:9],
            "valor": float(cls.cnab[9:19])/100,
            "cpf": cls.cnab[19:30],
            "cartao": cls.cnab[30:42],
            "hora": cls.cnab[42:48],
            "dono_loja": cls.cnab[48:62],
            "nome_loja": cls.cnab[62:81],
        }

        cls.campos = Campos.objects.create(**cls.data)

    def test_campos_max_length(self):
        tipo = self.campos._meta.get_field("tipo").max_length
        data = self.campos._meta.get_field("data").max_length
        valor = self.campos._meta.get_field("valor").max_length
        cpf = self.campos._meta.get_field("cpf").max_length
        cartao = self.campos._meta.get_field("cartao").max_length
        hora = self.campos._meta.get_field("hora").max_length
        dono_loja = self.campos._meta.get_field("dono_loja").max_length
        nome_loja = self.campos._meta.get_field("nome_loja").max_length

        self.assertEqual(tipo, 2)
        self.assertEqual(data, 9)
        self.assertEqual(valor, 11)
        self.assertEqual(cpf, 12)
        self.assertEqual(cartao, 13)
        self.assertEqual(hora, 7)
        self.assertEqual(dono_loja, 15)
        self.assertEqual(nome_loja, 20)

    def test_campos_fields(self):
        self.assertEqual(self.campos.tipo, self.data["tipo"])
        self.assertEqual(self.campos.data, self.data["data"])
        self.assertEqual(self.campos.valor, self.data["valor"])
        self.assertEqual(self.campos.cpf, self.data["cpf"])
        self.assertEqual(self.campos.cartao, self.data["cartao"])
        self.assertEqual(self.campos.hora, self.data["hora"])
        self.assertEqual(self.campos.dono_loja, self.data["dono_loja"])
        self.assertEqual(self.campos.nome_loja, self.data["nome_loja"])
