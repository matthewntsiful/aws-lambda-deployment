#This Python script is an AWS Lambda function designed to handle incoming events, process them, and return a response.

import json

def lambda_handler(event, context):
    
    """
    AWS Lambda handler function.

    Parameters:
    - event (dict): The event data passed to the function.
    - context (object): Provides methods and properties that provide information about the invocation, function, and execution environment.

    Returns:
    - dict: Response containing status code and body.
    """
    # Log the received event (useful for debugging)
    print("Received event:", json.dumps(event))

    # Example processing: Extract a name from the event, if provided
    name = event.get('name', 'World')

    # Create a response message by Constructing a greeting message based on the extracted name
    message = f"Hello, {name}!"

    # Return the response in the expected format (json)
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': message
        })
    }