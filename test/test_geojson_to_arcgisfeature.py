import pytest

from aws_lambda.geojson_to_arcgisfeature import GeoJsonToArcGISFeature


class TestGeoJsonToArcGISFeature():

    @pytest.fixture
    def geojson(self):

        input_geojson = {

            "type": "FeatureCollection",
            "crs": {
                    "type": "name",
                    "properties": {
                        "name": "EPSG:4326"
                    }
            },
            "features": [
                {
                    "type": "Feature",
                    "id": 1,
                    "geometry": {
                            "type": "Polygon",
                            "coordinates": [
                                [
                                    [-0.330057, 51.793631],
                                    [-0.395986, 51.733671],
                                    [-0.332533, 51.695129],
                                    [-0.330057, 51.793631]
                                ]
                            ]
                    },
                    "properties": {
                        "FLOOD_DATETIME": 1729192309000,
                        "FLOOD_COUNTRY": "GB"
                    }
                }
            ]
        }

        return input_geojson

    def test_get_rings_from_coordinates(self, geojson):

        expected_result = [
            [
                [-0.330057, 51.793631],
                [-0.395986, 51.733671],
                [-0.332533, 51.695129],
                [-0.330057, 51.793631]
            ]
        ]

        converter = GeoJsonToArcGISFeature(geojson)
        rings = converter._get_rings_from_coordinates(geojson)

        assert rings == expected_result

    def test_get_attributes_from_properties(self, geojson):

        expected_result = {
            "FLOOD_DATETIME": 1729192309000,
            "FLOOD_COUNTRY": "GB"
        }

        converter = GeoJsonToArcGISFeature(geojson)
        attributes = converter._get_attributes_from_properties(geojson)

        assert attributes == expected_result

    def test_geojson_to_arcgisfeature(self, geojson):

        expected_result = {
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
                "FLOOD_DATETIME": 1729192309000,
                "FLOOD_COUNTRY": "GB"
            }

        }

        arcgisrest = GeoJsonToArcGISFeature(geojson).get_arcgisfeature()

        assert arcgisrest == expected_result
