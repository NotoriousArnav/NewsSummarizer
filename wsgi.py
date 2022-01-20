from main import app
import json

with open('env.json') as env_file: env = json.loads(env_file.read())

if __name__ == "__main__": app.run(**env)
