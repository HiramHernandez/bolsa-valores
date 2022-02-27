from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Empresa


class EmpresaTestCase(TestCase):
    def set_up(self):
        empresa = Empresa(
            name='Empresa Ejemplo',
            description='Es una empresa para realizar TESTING',
            simbolo='EEJP',
            valores_mercado=['32', '34']
        )
        empresa.save()

    def test_post_empres(self):
        client = APIClient()
        response = client.post(
            '/api/empresas', {
                'name': 'Empresa Ejemplo',
                'description': 'Es una empresa para realizar TESTING',
                'simbolo': 'EEJP',
                'valores_mercado': ['32', '34']

            },
            follow=True
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        result = json.loads(response.content)