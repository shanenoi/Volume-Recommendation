import os


def run_server():
    os.system(
        "cd api/; export FLASK_APP=server.py; flask run"
    )
