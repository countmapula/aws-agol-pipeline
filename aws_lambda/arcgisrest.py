
"""

    Send edits to ArcGIS Feature Service via REST API and  
    applyEdits endpoint. 
    

"""

__author__ = "Dan Cronin"
__version__ = "0.1.0"
__license__ = "MIT"

import json
import requests


def apply_edits(
    url: str,
    api_key: str,
    feature: dict,
    headers={'content-type': 'application/x-www-form-urlencoded'}
):
    """

    Add a single feature to an ArcGIS REST API Feature Service via the 
    applyEdits endpoint. 

    ArcGIS JSON feature object spec: 

    https://developers.arcgis.com/rest/services-reference/enterprise/feature-object/

    Args:

        url (str): applyEdits endpoint 
        api_key (str): Key or token for ArcGIS Organisation 
        feature (dict): Dictionary corresponding to ArcGIS Feature object
        headers (dict, optional): http headers 
            Defaults to {'content-type': 'application/x-www-form-urlencoded'}

    Raises:

        e: TODO proper error handling 

    Returns:

        response_content (dict): ArcGIS REST API response 

    """

    body = {
        'f': 'json',
        'token': api_key,
        'useGlobalIds': 'false',
        'async': 'false',
        'adds': feature
    }

    try:

        r = requests.post(url, headers=headers, data=body)

    except Exception as e:

        raise e

    # TODO handle http error codes

    # TODO Parse response for arcgis error messsage

    try:

        response_content = json.loads(r.content)

    except Exception as e:

        raise e

    try:

        if (response_content['addResults'][0]['success']):

            print("APPLY EDIT RESULT:   {}".format(response_content))

            return response_content

    except Exception as e:

        status_success = False
        print("Unexpected result")
        print(response_content)
        return response_content
