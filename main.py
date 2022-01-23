from flask import Flask

app = Flask(__name__)

#Register Blueprints Here
try:
    from blueprints import (
                api,
                docs
            )
    app.register_blueprint(api.app)
    app.register_blueprint(docs.app)
except Exception as e:
    print('could not import blueprints')
    print(e)
