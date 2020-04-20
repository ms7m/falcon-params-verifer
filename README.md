# Falcon Query Parameter Verifier

![Test Python Module](https://github.com/ms7m/falcon-params-verifer/workflows/Test%20Python%20Module/badge.svg?branch=master) ![PyPi Shield](https://img.shields.io/badge/Available-on%20PyPi-blue?logoColor=white&logo=Python)

A simple falcon hook to check if a request contains all required query parameters.

***

## Installation / Requirements

Installation:

**PyPi**

```
pip install falcon-params-verifier
```

**.whl**

A ``.whl`` is provided in the releases tab in Github. 

## Sample Usage

*Sample code*

```python
import falcon
import falcon_params_verifier 
from falcon_params_verifier import ParamVerifier # This can also be used.

class SampleResource(object):
    def __init__(self):
        self._required_params = [
            "userId",
        ]
    # Add the hook
	@falcon.before(falcon_params_verifier.ParamVerifier(self._required_params))
    def on_get(self, req, resp):
        req.media = {
            "message": "Whoo hoo, you made a proper request!"
        }
```

***

If a query parameter is missing, the module will automatically raise an ``falcon.HTTPBadRequest``.

