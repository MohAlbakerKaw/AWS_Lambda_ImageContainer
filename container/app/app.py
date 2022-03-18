import os, json, boto3, s3fs
import pandas as pd
#####################################
##### import #### frameworks ########
#####################################


def handler(event, context):
    #####################################
    ## if you are receiving input data ##
    #####################################
    input_data=json.loads(event['body'])
    print(input_data)
    
    #####################################
    ##### your #### code ################
    #####################################
    
    #########################################
    #### edit the body you want to return ###
    #########################################
    message='Hello World!' 
    
    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'body': json.dumps({
            "message": message
        }),
        'headers': {
            'Content-Type': 'application/json'
        }
    }