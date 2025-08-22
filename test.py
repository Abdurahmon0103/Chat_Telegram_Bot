import requests

url = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"
headers = {"Authorization": "Bearer YOUR_HF_API_TOKEN"}

data = {
    "inputs": "Salom! Qalaysiz?",
    "parameters": {"max_new_tokens": 128}
}

response = requests.post(url, headers=headers, json=data)

print(response.status_code)
print(response.json())
