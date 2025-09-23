import os
from flask import Flask, Response, send_from_directory
from dotenv import load_dotenv

#Load env globals
load_dotenv()

LOADER_ID = os.getenv('LOADER_ID')
LOADER_DOWNLOAD = os.getenv('LOADER_DOWNLOAD')
LOADER_NAME = os.getenv('LOADER_NAME')

#Init Flask
app = Flask(__name__)

@app.route("/meta")
def metadata():
    response_body = f"{LOADER_ID}\n{LOADER_DOWNLOAD}\n{LOADER_NAME}\n"

    for item in os.listdir("./mods"):
        if os.path.isfile("./mods/" + item):
            response_body += f"{item}\n"
    
    return Response(response_body, mimetype="text/plain")

@app.route("/mods/<path:modname>")
def static_mods(modname):
    return send_from_directory("mods", modname)

if __name__ == "__main__":
    app.run(debug=True)

