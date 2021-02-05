import logging

import elasticapm
from apm_agent_utils.utils import add_instrumentation
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

from example.config import secret_token, server_url, service_name

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

es = ElasticAPM()


def create_app():
    add_instrumentation("example.instrumentations.Test")
    elasticapm.instrument()
    app = Flask(__name__)
    es.init_app(
        app,
        server_url=server_url,
        service_name=service_name,
        secret_token=secret_token,
        debug=True,
    )
    return app


app = create_app()
