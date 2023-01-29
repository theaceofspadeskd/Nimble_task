import json
from flask import Flask
import boto3
import os

app = Flask(__name__)

# Usually local stored (~/.aws/) credentials of Amazon S3 bucket. Adding raw keys is unsafe.
s3 = boto3.client('s3', aws_access_key_id='#',
                  aws_secret_access_key='#')


@app.route('/')
def index():
    """
    Testing route
    """
    return "Добрий день, everybody!"


@app.route('/api/v1/add_data/<key>/<value>', methods=['PUT', 'GET'])
def put_data(key, value):
    """
    Method PUT, GET.
    key: Input key, that also would be the name of file.
    value: Input value to store in file.
    """
    data = {key: value}
    with open(f'{key}', 'w', encoding='utf8') as fp:
        json.dump(data, fp)
    sz = os.path.getsize(f'{key}')
    # Checking size (f.e. 10 mb) to avoid abusing and program stucking during upload too big files
    if sz <= 10 * 1024 ** 2:
        file = open(f'{key}', 'rb')
        try:
            # Upload to bucket
            s3.put_object(Body=file, Bucket='theaceofspadeskd', Key=f'{key}')
            return {f'{key}': data}, 201
        except:
            return "Error, try again"
    else:
        return "File size limited to 10 MB"


@app.route('/api/v1/<key>', methods=['GET'])
def get_data(key):
    """
    Method GET.
    key: Input previously PUT'ed key to get 'key: value' pair.
    """
    try:
        obj = s3.get_object(Bucket='theaceofspadeskd', Key=f'{key}')
        data = obj['Body'].read()
        return data, 200
    except:
        return "Error, try again"


if __name__ == '__main__':
    app.run(debug=True)
