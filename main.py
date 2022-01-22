from flask import Flask

app = Flask(__name__)

#Register Blueprints Here
try:
    from blueprints import (
                api,
                docs
            )
    app.register_blueprint(api.app)
    app.r3gister_blueprint(docs.app)
except:
    print('could not import blueprints')
