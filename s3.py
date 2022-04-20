import pickle
import boto3
from pickle_load import *
aws_access_key_id = 'AKIASECCF5ETZBMRYYQW'
aws_secret_access_key = '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'
bucket = 'goldstockProject'
key = 'coupon_codes'
local_key = 'local_coupon'
file_name = 'coupons/coupon_codes'
source_bucket='goldstockProject'


client = boto3.client(
    's3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name='ap-south-1'
)

s3 = boto3.resource('s3',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name='ap-south-1')

# upload to s3
def upload_to_s3(file_name):
    with open(file_name, 'rb') as f:
        response = client.put_object(
            Body=f,
            Bucket=source_bucket,
            Key=key)

# read back from s3
def read_s3_file():
    response = s3.Bucket(source_bucket).Object(key).get()
    body_string = response['Body'].read()
    loaded_pickle = pickle.loads(body_string)
    # print(loaded_pickle)

    print('s3 current data is', (loaded_pickle))
    # print('current local file', (load_file(file_name)))

    print('current local file', len(load_file(file_name)))
    print('s3 current data is', len(loaded_pickle))

    return loaded_pickle

# generate coupon code
def g_c_c(plan, stop):
    i = 0
    stop = stop
    new_list = read_s3_file()
    while i < stop:
        code = plan + get_transaction_id()
        new_list.append(code)
        dump_file(new_list, file_name)
        upload_to_s3(file_name)
        i += 1

    return new_list

# validate user copon code
def s3_update(code):

    s3_file = read_s3_file()

    if code in s3_file:
        # remove the item and save
        print('Removing {} coupon...'.format(code))
        s3_file.remove(code)
        print('Dumping coupon...')
        dump_file(s3_file, file_name)
        s3_file = load_file(file_name)

        print(s3_file)
        print('Current coupon', len(s3_file))

        print('Saving new coupon file to s3')
        with open(file_name, 'rb') as f:
          response = client.put_object(
              Body=f,
              Bucket=source_bucket,
              Key=key)

        print('Saved new', len(s3_file), 'files.')
        return True
    else:
        print('Invalid coupon code')

#
# load_file(file_name)
# dump_file([], file_name)
# upload_to_s3(file_name)
# g_c_c('5kc', 100)
# read_s3_file()



