import boto3
import json
import base64
import os
import random

prompt = input("\n" + "Hi, what should I generate for you?: \n\n")

payload = {
    "text_prompts" : [{"text": prompt}],
    "cgf_scale" : 12,
    "seed" : 0,
    "steps" : 80
}

modelId = "stability.stable-diffusion-xl-v0"
contentType = "application/json"
accept = "application/json"
body = json.dumps(payload)

bedrock = boto3.client(service_name="bedrock-runtime")

response = bedrock.invoke_model(
    body = body,
    modelId = modelId,
    accept = accept,
    contentType = contentType
)

response_body = json.loads(response.get("body").read())
artifact = response_body.get("artifacts")[0]
image_encoded = artifact.get("base64").encode("utf-8")
image_bytes = base64.b64decode(image_encoded)

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

code = random.randint(1000, 9999)
file_name = f"{output_dir}/generated-{code}.png"

with open(file_name, "wb") as f:
    f.write(image_bytes)

print("\nYour image is ready in " + file_name)