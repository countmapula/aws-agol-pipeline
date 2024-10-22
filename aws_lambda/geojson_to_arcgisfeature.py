
"""

    Convert a GeoJSON feature to an ArcGIS feature. 
    

"""

__author__ = "Dan Cronin"
__version__ = "0.1.0"
__license__ = "MIT"

import json


'''

ArcGIS REST API Feature: 

{
    "geometry": {
        "spatialReference": {
            "wkid": 4326
        },
        "rings": [
            [
              [
                -0.3450368316073593,
                51.773582329966075
              ],
              [
                -0.3707377781971104,
                51.744589425746454
              ],
              [
                -0.3443626087902203,
                51.733681155445225
              ],
              [
                -0.3450368316073593,
                51.773582329966075
              ]
            ]
          ]
    },
    "attributes": {
        "FLOOD_DATETIME": 1729192309000,
        "FLOOD_COUNTRY": "GB"
    }
}
'''


class GeoJsonToArcGISFeature:

    def __init__(self, geojsondata: dict):

        self.geojsondata = geojsondata

    def get_arcgisfeature(self):
        """

        Parse ArcGIS Feature object from GeoJSON object. 

        https://developers.arcgis.com/rest/services-reference/enterprise/feature-object/

        https://geojson.org/ 

        Raises:

            e: TODO error handling 

        Returns:

            arcgisrest (dict): ArcGIS REST API feature object

        """

        arcgisrest = {}

        try:

            rings = self._get_rings_from_coordinates(self.geojsondata)

        except Exception as e:

            print(e)
            raise e

        try:

            attributes = self._get_attributes_from_properties(self.geojsondata)

        except Exception as e:

            print(e)
            raise e

        arcgisrest.update({
            'geometry': {
                "spatialReference": {
                    "wkid": 4326
                },
                "rings": rings
            },
            "attributes": attributes
        }
        )

        return arcgisrest

    def _get_rings_from_coordinates(self, geojsondata: dict):
        """

        Internal class method invoked by get_arcgisfeature. 

        Args:
            geojsondata (dict): Input GeoJSON object. 

        Raises:
            e: TODO error handling. 

        Returns:
            _type_: _description_
        """

        try:

            geojson_feature = geojsondata['features'][0]
            geojson_coordinates = geojson_feature['geometry']['coordinates']

        except Exception as e:
            print(e)
            raise ValueError("Unexpected GeoJSON content...")

        arcgis_rings = geojson_coordinates

        return arcgis_rings

    def _get_attributes_from_properties(self, geojsondata):
        """

        Internal class method invoked by get_arcgisfeature. 

        Args:
            geojsondata (dict): Input GeoJSON object. 

        Raises:
            ValueError: _description_

        Returns:
            _type_: _description_

        """

        try:

            geojson_feature = geojsondata['features'][0]
            geojson_properties = geojson_feature['properties']

        except Exception as e:
            print(e)
            raise ValueError("Unexpected GeoJSON content...")

        attributes = geojson_properties

        return attributes
