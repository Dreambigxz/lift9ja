""" For pulling data from AW S3 buckets -Importing the necessary Python Modules"""
import boto3
import sys
import os
import pandas
import csv
import io
import json

aws_access_key_id = 'AKIASECCF5ETZBMRYYQW'
aws_secret_access_key = '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'
bucket = 'goldstockProject'
key = 'coupon_codes'


# Creating the low level functional client
client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='ap-south-1'
)

# Creating the high level object oriented interface
resource = boto3.resource(
    's3',
    aws_access_key_id='AKIA46SFIWN5AMWMDQVB',
    aws_secret_access_key='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',
    region_name='ap-south-1'
)

# Fetch the list of existing buckets
# clientResponse = client.list_buckets()


# Print the bucket names one by one
# print('Printing bucket names...')
# for bucket in clientResponse['Buckets']:
#     print(f'Bucket Name: {bucket["Name"]}')

s3_client = client
s3_object = s3_client.get_object(Bucket=bucket, Key=key)

print(s3_object)
# read the file
# Read data from the S3 object
data = pandas.read_csv(s3_object['Body'])

# Print the data frame
print('Printing the data frame...')
print(data)