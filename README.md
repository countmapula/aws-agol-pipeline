# aws-agol-pipeline

Proof-of-concept for AWS > ArcGIS data pipeline. 

## Get started 

This application can be deployed by first following the AWS [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html) tutorial. 

### Pre-requisites 

#### ArcGIS Online 

Sign up for a free [ArcGIS Location Services account](https://location.arcgis.com/sign-up/) and [create a new feature layer](https://developers.arcgis.com/documentation/portal-and-data-services/data-services/tutorials/tools/define-new-hosted-feature-layer/) with the following attributes. 

| Column                | Type      |
| ---------             | --------- |
| Shape                 | POLYGON   |
| FLOOD_DATETIME        | DATETIME  |
| FLOOD_COUNTRY         | TEXT(2)   |

Alternatively, use an existing ArcGIS Enterprise deployment or ArcGIS Online subscription. 

You will [create an API key](https://developers.arcgis.com/documentation/security-and-authentication/api-key-authentication/how-to-use-an-api-key/#1-create-api-key-credentials)
for your ArcGIS environment to authenticate requests from Amazon Web Services. 

#### Amazon Web Services (AWS) 

Sign up to the [AWS Free Tier](https://aws.amazon.com/free/). This should provide you with free access to the services you'll need: 

- Simple Storage Service (S3)
- Lambda 

### Complete the AWS tutorial 

After completing the tutorial, overwrite the lambda function created in the tutorial with the contents of this aws_lambda directory. This can be done by zipping the contents of the directory (not the directory itself) and uploading this to Lambda. 

Note that lambda_function.py must remain in the root of the directory when viewed in the AWS web console. 

Create the following [Lambda environment variables](https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html) using the relevant values for your ArcGIS subscription. 

- ARCGIS_API_KEY 
- ARCGIS_FEATURE_SERVICE 

### Upload test data 

Upload the sample dataset st_albans.geojson to the S3 bucket that you created in the tutorial. 

The feature should be created in your ArcGIS Online feature service. 

Note that you can now configure your Lambda test event to use the st_albans.geojson file as a test input. 

## Directories 

### aws_lambda/ 

Lambda application including local copy of the requests library and dependencies. 

Note that requests must be manually installed directly into this directory, in order for it to be available to the Lambda runtime. 

```pip install requests -t ./```

### sample_data/

Sample GeoJSON file with source data schema. You can use this to test your pipeline. 

### scratch/

Initial test scripts. 

### test/

Example unit tests. 

Run pytest: 

```
$ pytest
=========================================== test session starts ===========================================
platform darwin -- Python 3.9.9, pytest-8.3.3, pluggy-1.5.0
rootdir: <dir>
plugins: anyio-3.6.1, mock-3.14.0
collected 4 items                                                                                         

iceye-gisdev/test/test_arcgisrest_applyedits.py .                                                   [ 25%]
iceye-gisdev/test/test_geojson_to_arcgisfeature.py ...                                              [100%]

============================================ 4 passed in 0.27s ============================================
```
