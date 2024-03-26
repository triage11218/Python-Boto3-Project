import time
import boto3

# Create a new EC2 client
ec2 = boto3.client('ec2',region_name='us-east-1')


response = ec2.run_instances(
    ImageId='ami-0fe630eb857a6ec83',      # RHEL AMI id
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='ubuntu_key',     # Replace with your actual key pair name
)

# Retrieve the instance ID as you will need the id to give instance a name and to terminate the instance
instance_id = response['Instances'][0]['InstanceId']
print("Successfully launched RHEL EC2 instance with Instance ID: " + instance_id)

# give instance a name
ec2.create_tags(
    Resources=[instance_id], 
    Tags=[{'Key':'Name', 'Value':'RHEL-Linux-Machine'}]
)

time.sleep(20) # Sleep

# Terminate the instance
response = ec2.terminate_instances(InstanceIds=[instance_id])
state = response['TerminatingInstances'][0]['CurrentState']['Name']
print("Instance " + instance_id + " is now " + state)
