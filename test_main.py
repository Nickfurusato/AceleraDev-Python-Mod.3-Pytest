from main import get_temperature
from unittest.mock import patch
import pytest

# utilizando o mocks, é possível simular uma alteração no retorno da API
# passando os parametros desejados

parametrized_value = [
    (68, '-23,5849', '-46,6098', 20),
    (86, '-15,5849', '-55,5849', 30),
    (62, '14.235004', '51.92528', 16),
]

# através do mark parametrize, é possível passar os parametros desejados


@pytest.mark.parametrize('temperature, lat, lng, expected', parametrized_value)
def test_get_temperature_by_lat_lng(temperature, lat, lng, expected):

    # recebendo o retorno do request
    mock_get_patcher = patch('main.requests.get')

    # alterando o valor de retorno, utilizando como parametro temperature:
    temperature = {
        'currently': {
            'temperature': temperature  # valor da temperatura esperada
        }

    }

    # iniciando o mock
    mock_get = mock_get_patcher.start()

    # retorno será igual ao objeto criado
    mock_get.return_value.json.return_value = temperature

    # o valor de resposta da API será igual ao valor de get_temperature
    response = get_temperature(lat, lng)

    # parando o mock
    mock_get.stop()

    # verificando se a resposta é igual ao solicitado
    assert response == expected
