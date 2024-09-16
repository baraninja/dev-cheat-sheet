import streamlit as st

def perplexity_api():
    st.header("Using Perplexity API")
    
    st.markdown("""
    The Perplexity API provides access to advanced language models for chat completions. 
    Here's how to use it in your Python applications.
    """)
    
    st.subheader("Authentication")
    st.code("""
    import requests

    API_KEY = "your-api-key-here"
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    """)
    
    st.subheader("Making a Basic API Call")
    st.code("""
    import requests
    import json

    url = "https://api.perplexity.ai/chat/completions"

    payload = {
        "model": "llama-3.1-sonar-small-128k-online",
        "messages": [
            {
                "role": "system",
                "content": "Be precise and concise."
            },
            {
                "role": "user",
                "content": "What is the capital of France?"
            }
        ],
        "temperature": 0.2,
        "top_p": 0.9,
        "return_citations": True
    }

    response = requests.post(url, json=payload, headers=headers)
    print(json.dumps(response.json(), indent=2))
    """)
    
    st.subheader("Handling Rate Limits")
    st.markdown("""
    Perplexity API has rate limits based on the model used. For example:
    - `llama-3.1-sonar-small-128k-online`: 20 requests/min
    - `llama-3.1-8b-instruct`: 100 requests/min
    
    Implement appropriate error handling and retry mechanisms to manage these limits.
    """)
    
    st.subheader("Streaming Responses")
    st.code("""
    import requests
    import sseclient

    url = "https://api.perplexity.ai/chat/completions"
    payload["stream"] = True

    response = requests.post(url, json=payload, headers=headers, stream=True)
    client = sseclient.SSEClient(response)

    for event in client.events():
        if event.data != "[DONE]":
            print(json.loads(event.data)['choices'][0]['delta'].get('content', ''), end='')
    """)
    
    st.subheader("Best Practices")
    st.markdown("""
    1. Always handle API errors gracefully.
    2. Use environment variables to store your API key.
    3. Implement retry logic for rate limit errors.
    4. Consider using async methods for improved performance in high-volume applications.
    5. Keep your model and API version up-to-date.
    """)