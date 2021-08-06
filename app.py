import os
from configs.flask_config import app
from configs.flask_api_config import api

port = int(os.environ.get("PORT", 5000))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, threaded=True)