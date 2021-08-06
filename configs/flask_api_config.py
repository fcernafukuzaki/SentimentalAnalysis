from .flask_config import api
from controller.sentimental_analysis_controller import *

api.add_resource(SentimentalAnalysisController,
    '/v1/sentimental_analysis')