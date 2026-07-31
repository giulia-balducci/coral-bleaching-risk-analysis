import os
import boto3
import sagemaker
from sagemaker.sklearn import SKLearnModel

DEPLOY_DIR = os.path.dirname(os.path.abspath(__file__))

REGION = 'us-east-1'
ACCOUNT_ID = '685850484811'
ROLE = f'arn:aws:iam::{ACCOUNT_ID}:role/LabRole'
BUCKET = f'coral-bleaching-{ACCOUNT_ID}'
MODEL_S3_KEY = 'coral-bleaching/model.tar.gz'

session = boto3.Session(region_name=REGION)
sm_session = sagemaker.Session(boto_session=session)

model = SKLearnModel(
    model_data=f's3://{BUCKET}/{MODEL_S3_KEY}',
    role=ROLE,
    entry_point='inference.py',
    source_dir=os.path.join(DEPLOY_DIR, 'code'),
    framework_version='1.4-2',
    py_version='py3',
    sagemaker_session=sm_session
)

predictor = model.deploy(
    initial_instance_count=1,
    instance_type='ml.m5.large'
)

print(f'Endpoint name: {predictor.endpoint_name}')
print('Done! Save this endpoint name, you will need it.')
