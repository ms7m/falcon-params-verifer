
import falcon
from falcon import testing
import pytest


from falcon_params_verifier import ParamVerifier


def create_testing_client():
    class TestResource(object):

        @falcon.before(ParamVerifier(['requiredParam']))
        def on_get(self, req, resp):
            resp.media = {
                "message": "Worked."
            }

    api = falcon.API()
    api.add_route("/test", TestResource())
    return api

@pytest.fixture()
def testing_client():
    return testing.TestClient(create_testing_client())

def test_param_hook(testing_client):
    expected_result = {
        "message": "Worked."
    }
    result = testing_client.simulate_get('/test?requiredParam=Test')
    assert result.json == expected_result

def test_no_provided_param_hook(testing_client):
    expected_result = {
        "title": "400 Bad Request",
        "description": "A required parameter has not been supplied."
    }
    result = testing_client.simulate_get('/test')
    assert result.json == expected_result

def test_blank_param(testing_client):
    expected_result =  {
        "title": "400 Bad Request",
        "description": "A required parameter has not been supplied."
    }
    result = testing_client.simulate_get('/test?requiredParam=""')
    assert result.json == expected_result
