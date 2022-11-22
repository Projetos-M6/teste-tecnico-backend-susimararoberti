from rest_framework.views import APIView, Response
from rest_framework import status
from rest_framework.parsers import FileUploadParser

from drf_spectacular.utils import extend_schema

from .models import Campos
from .serializers import CamposSerializers, CamposUploadSerializer, CamposListSerializer


@extend_schema(methods=['GET'], exclude=True)
class UploadView(APIView):
    parser_classes = [FileUploadParser]
    queryset = Campos
    serializer_class = CamposUploadSerializer

    def post(self,  request,  filename, format=None):

        arquivo = request.FILES["file"].read().decode().split("\n")
        arquivo.pop()

        dados = []

        for item in arquivo:
            serializer = CamposSerializers(
                data={
                    "tipo": item[:1],
                    "data": item[1:9],
                    "valor": float(item[9:19])/100,
                    "cpf": item[19:30],
                    "cartao": item[30:42],
                    "hora": item[42:48],
                    "dono_loja": item[48:62],
                    "nome_loja": item[62:81],
                }
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            dados = [serializer.data] + dados

        return Response(data=dados, status=status.HTTP_201_CREATED)


@extend_schema(methods=['POST'], exclude=True)
class ListView(APIView):
    queryset = Campos
    serializer_class = CamposListSerializer

    def get(self, request, nome_loja):
        loja = Campos.objects.filter(nome_loja__icontains=nome_loja)

        somar = 0
        subtrair = 0
        saldo = 0

        loja_saldo = []

        calculo = {}

        for item in loja:
            calculo = dict(
                loja=item.nome_loja, tipo=item.tipo, valor=(
                    int(float(item.valor)))
            )
            loja_saldo = loja_saldo + [calculo]

            if(
                item.tipo == "2"
                or item.tipo == "3"
                or item.tipo == "9"
            ):
                subtrair -= int(float(item.valor))
            else:
                somar += int(float(item.valor))
        saldo = somar + subtrair

        return Response({"Operações da Loja": loja_saldo, "Saldo da Loja": saldo})
