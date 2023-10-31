import json
import boto3

region = 'us-east-1'

ec2 = boto3.client('ec2')

instance_id = []

response = ec2.describe_instances()
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        if instance['State']['Name'] == 'running':
            if 'Tags' in instance:
                for tag in instance['Tags']:
                    if tag['Value'] == 'Dev':
                        instance_id.append(instance['InstanceId'])


def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instance_id)