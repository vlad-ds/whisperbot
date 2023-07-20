from abc import ABC
from log import logger
import json
import os

import boto3


class FileConnector(ABC):
    def read(self, file_name: str):
        pass

    def write(self, file_name: str, data: dict):
        pass


class S3Connector(FileConnector):

    def __init__(self, bucket_name: str):
        self.bucket_name = bucket_name
        self.s3 = boto3.client('s3')

    def read(self, file_name: str):

        try:
            obj = self.s3.get_object(Bucket=self.bucket_name, Key=file_name)
            file_content = obj['Body'].read().decode('utf-8')
            return json.loads(file_content)
        except Exception as e:
            logger.info(f"Unable to download the file. Reason: {str(e)}")
            return None

    def write(self, file_name: str, data: dict):
        json_data = json.dumps(data)
        self.s3.put_object(Bucket=self.bucket_name, Key=file_name, Body=json_data)
        logger.info(f"Successfully uploaded data to {self.bucket_name}/{file_name}")


class LocalConnector(FileConnector):

    def read(self, file_name: str):
        try:
            with open(file_name, 'r') as f:
                return json.load(f)
        except Exception as e:
            logger.info(f"Unable to download the file. Reason: {str(e)}")
            return None

    def write(self, file_name: str, data: dict):
        # create the directory if it doesn't exist
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w') as f:
            json.dump(data, f)
        logger.info(f"Successfully uploaded data to {file_name}")


def get_connector(connector_name: str, bucket_name: str = None):
    if connector_name == 'local':
        return LocalConnector()
    elif connector_name == 's3':
        if not bucket_name:
            raise ValueError("bucket_name must be provided for S3 connector.")
        return S3Connector(bucket_name)
    else:
        # raise not implemented error
        raise NotImplementedError(f"Connector {connector_name} is not implemented. Supported: local, s3."
                                  f"Check the STORAGE configuration.")
