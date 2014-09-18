from flask import Flask

DATABASE = "/tmp/collector.db"

app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('EC_SETTINGS', silent=True)

import emailcollector.views

