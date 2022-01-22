from flask import Flask

app = Flask(__name__)

#Register Blueprints Here
try:
    from blueprints import (
                api
            )
    app.register_blueprint(api.app)
except:
    print('could not import blueprints')
