from flask import request
from flask_restful import Resource
from configs.flask_config import app
from service.aws_apigateway_service import AWSAPIGatewayService

aws_apigateway_service = AWSAPIGatewayService()

class SentimentalAnalysisController(Resource):

    def post(self):
        #token = request.headers['Authorization']
        token = ""
        if True:
            json_dict = request.json
            if json_dict is not None:
                if 'text' in json_dict:
                    input_text = request.json['text']
                    flag, respuesta = aws_apigateway_service.sentimental_analysis(token,input_text)
                    if flag:
                        return {'codigo':200,'mensaje': 'OK','respuesta':respuesta}, 200
        return {'codigo':403,'mensaje': 'Operación no valida.'}, 403