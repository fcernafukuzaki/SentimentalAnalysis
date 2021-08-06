import json
import ast
import urllib3
from configs.configs import ENDPOINT_AWS_COMPREHEND

class AWSAPIGatewayService():

    def sentimental_analysis(self, token, text):
        try:
            http = urllib3.PoolManager()
            url = ENDPOINT_AWS_COMPREHEND
            encoded_body = json.dumps({
                "text": text
            })
            print(f"{url} {encoded_body}")
            response = http.request('POST',
                                    url,
                                    headers={'Content-Type': 'application/json', 'Authorization': token},
                                    body=encoded_body,
                                    retries=False)
            print(f"Resultado de API: {response.status} {response.data}")
            if response.status == 200:
                print('Respuesta exitosa')
                return True, json.loads(response.data.decode('utf-8'))
            print(f"No se obtuvo respuesta exitosa: {response.status}")
            return False, None
        except Exception as e:
            print(f"Error durante consumo de AWS API Gateway. {e}")
            return False, None