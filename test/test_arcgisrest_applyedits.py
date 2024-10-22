import pytest
import requests

from aws_lambda.arcgisrest import apply_edits


class TestArcGISRest():

    def test_apply_edits(self, mocker):

        mocker.patch('requests.post')
        mocker.patch('json.loads')

        url = 'https://arcgis.com'
        api_key = 'myapikey'
        feature = {
            "geometry": {
                "spatialReference": {
                    "wkid": 4326
                },
                "rings": [[
                    [-0.330057, 51.793631],
                    [-0.395986, 51.733671],
                    [-0.332533, 51.695129],
                    [-0.330057, 51.793631]]]

            },
            "attributes": {
                "MY_ATTRIBUTE": 'Hello world!'
            }

        }

        apply_edits(
            url=url,
            api_key=api_key,
            feature=feature
        )

        requests.post.assert_called_once_with(
            url,
            headers={'content-type': 'application/x-www-form-urlencoded'},
            data={
                'f': 'json',
                'token': api_key,
                'useGlobalIds': 'false',
                'async': 'false',
                'adds': feature
            }
        )
