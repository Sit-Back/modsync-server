import os
from flask import Flask, Response, send_from_directory
from dotenv import load_dotenv

#Load env globals
load_dotenv()

LOADER_ID = os.getenv('LOADER_ID')
LOADER_CMD = os.getenv('LOADER_CMD')

#Init Flask
app = Flask(__name__)

@app.route("/meta")
def metadata():
    response_body = f"LID{LOADER_ID}\nCMD{LOADER_CMD}\n"

    for item in os.listdir("./mods"):
        if item[0] == '!':
            print(item + "ignored!")
        elif os.path.isfile("./mods/" + item):
            response_body += f"{item}\n"
    
    return Response(response_body, mimetype="text/plain")

@app.route("/mods/<path:modname>")
def static_mods(modname):
    return send_from_directory("mods", modname)

@app.route("/app")
def app_win():
    return send_from_directory("static", "modsync.zip")

@app.route("/loader.jar")
def loader():
    return send_from_directory("static", "loader.jar")

if __name__ == "__main__":
    app.run(host='0.0.0.0')

