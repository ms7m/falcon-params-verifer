
import waitress
import falcon

from falcon_params_verifier import ParamVerifier


class TestResource(object):
    
    @falcon.before(ParamVerifier(['userId']))
    def on_get(self, req, resp):
        resp.media = {
            "message": "Worked."
        }

api = falcon.API()
api.add_route("/test", TestResource())

waitress.serve(api, port=4000)