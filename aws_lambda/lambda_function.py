# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import boto3
import json
import logging  # TODO logging
import urllib.parse
import os


from arcgisrest import apply_edits
from geojson_to_arcgisfeature import GeoJsonToArcGISFeature


print('Loading function')


s3 = boto3.client('s3')
api_key = os.environ['ARCGIS_API_KEY']
url = os.environ['ARCGIS_FEATURE_SERVICE']


def lambda_handler(event, context):

    # Get the object from the event and show its content type
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(
        event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    try:

        # Load data from S3 based on event
        response = s3.get_object(Bucket=bucket, Key=key)
        body = response['Body'].read().decode('utf-8')
        json_content = json.loads(body)
        print("GEOJSON CONTENT: {}".format(json_content))

        # Get ArcGIS REST API compliant feature
        converter = GeoJsonToArcGISFeature(json_content)
        arcgis_feature = json.dumps(converter.get_arcgisfeature())
        print("ARCGIS FEATURE: {}".format(arcgis_feature))

        # Update ArcGIS Online feature service
        upload_flood = apply_edits(url, api_key, arcgis_feature)

        return upload_flood

    except Exception as e:
        print(e)
        print('Something went wrong :(')
        raise e
