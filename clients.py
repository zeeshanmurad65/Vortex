import requests
base_url = "https://api.deepseek.com/v1/chat/completions"
api_key="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"

payload = {
    "model": "deepseek-ai/deepseek-coder",  # Use a valid model for DeepSeek
    "messages": [
        {"role": "user", "content": "What is Coding?"}
    ]
}
response = requests.post(base_url, json=payload)
# Process response
if response.status_code == 200:
    print(response.json()["choices"][0]["message"]["content"])
else:
    print(f"Error {response.status_code}: {response.text}")





