import boto3
import json

prompt_request = input("Ask me something: \n\n")

bedrock = boto3.client(service_name='bedrock-runtime')

payload = {
    "prompt": f"\n\nHuman:{prompt_request}\n\nAssistant:", 
    "temperature" : 0.8,
    "topP" : 0.,
    "maxTokens" : 200,
}

body        = json.dumps(payload)
model_id    = 'ai21.j2-mid-v1'
accept      = 'application/json'
contentType = 'application/json'

response = bedrock.invoke_model(body=body, modelId=model_id, accept=accept, contentType=contentType)

response_body = json.loads(response.get('body').read())

print("\n", response_body.get("completions")[0].get("data").get("text"))