import boto3
import json

# Initialize the Boto3 clients
emr_client = boto3.client('emr')
sfn_client = boto3.client('stepfunctions')

# Step 1: Define the EMR cluster configuration (simplified for brevity)
# Note: Modify the configurations according to your requirements
emr_cluster_config = {
    'Name': 'MyEMRCluster',
    'ReleaseLabel': 'emr-6.2.0',
    'Instances': {
        'MasterInstanceType': 'm5.xlarge',
        'SlaveInstanceType': 'm5.xlarge',
        'InstanceCount': 3,
        'KeepJobFlowAliveWhenNoSteps': False,
        'TerminationProtected': False,
    },
    'Applications': [{'Name': 'Spark'}, {'Name': 'Hadoop'}],
    'JobFlowRole': 'EMR_EC2_DefaultRole',
    'ServiceRole': 'EMR_DefaultRole',
    'VisibleToAllUsers': True
}

# Step 2: Define a Step Function state machine with a task to run the EMR cluster
# Note: Replace 'your-state-machine-arn' with your actual Step Function state machine ARN
# and 'your-role-arn' with the IAM role ARN that Step Functions can assume to execute the state machine
state_machine_definition = {
    "Comment": "Run an EMR Job",
    "StartAt": "RunEMRJob",
    "States": {
        "RunEMRJob": {
            "Type": "Task",
            "Resource": "arn:aws:states:::elasticmapreduce:createCluster.sync",
            "Parameters": emr_cluster_config,
            "End": True
        }
    }
}

# Create or update the state machine (this example assumes it's being created)
try:
    state_machine_response = sfn_client.create_state_machine(
        name='MyStateMachineForEMR',
        definition=json.dumps(state_machine_definition),
        roleArn='your-role-arn'  # Replace with your actual IAM role ARN
    )
except sfn_client.exceptions.StateMachineAlreadyExists:
    print("State machine already exists. Update it instead of creating a new one.")

# Step 3: Execute the Step Function
execution_response = sfn_client.start_execution(
    stateMachineArn=state_machine_response['stateMachineArn'],
    input=json.dumps({})  # Pass input data if your state machine requires it
)

print(f"Started state machine execution: {execution_response['executionArn']}")
