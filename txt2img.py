import boto3
from flask import Flask, request

app = Flask(__name__)

# Create a SageMaker runtime client
sagemaker = boto3.client('sagemaker-runtime')

@app.route("/", methods=["POST"])
def chatbot():
    # Get the text message from the user
    message = request.form.get("text")

    # Call the SageMaker endpoint with the user's message
    response = sagemaker.invoke_endpoint(
        EndpointName='<YOUR_ENDPOINT_NAME>',
        ContentType='text/plain',
        Body=message
    )

    # Get the response payload from SageMaker
    payload = response['Body'].read().decode('utf-8')

    # Return the payload as a response to the user
    return {"text": payload}

if __name__ == "__main__":
    app.run(debug=True)
