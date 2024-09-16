import streamlit as st

def advanced_openai_api():
    st.header("Advanced OpenAI API Usage")

    st.subheader("Latest OpenAI Models (cost in USD)")
    st.markdown("""
    - **GPT-4o (2024-08-06)**:
        - API Model Name: gpt-4o-2024-08-06
        - Max Tokens: 128,000
        - Max Output Tokens: 16,384
        - Cost: 2.50 per 1K input tokens, 7.50 per 1K output tokens
    - **GPT-4o (2024-05-13)**:
        - API Model Name: gpt-4o-2024-05-13
        - Max Tokens: 128,000
        - Max Output Tokens: 4,096
        - Cost: 5.00 per 1K input tokens, 15.00 per 1K output tokens
    - **GPT-4o-mini (2024-07-18)**:
        - API Model Name: gpt-4o-mini-2024-07-18
        - Max Tokens: 128,000
        - Cost: 0.15 per 1M input tokens, 0.60 per 1M output tokens
    """)

    st.subheader("Basic API Call")
    st.code("""
    from openai import OpenAI

    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the World Series in 2020?"}
        ],
        temperature=0.7,
        max_tokens=150
    )

    print(response.choices[0].message.content)
    """)

    st.subheader("Streaming Responses")
    st.code("""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[...],
        stream=True
    )

    for chunk in response:
        print(chunk.choices[0].delta.content, end='')
    """)

    st.subheader("Function Calling")
    st.code("""
    functions = [
        {
            "name": "get_weather",
            "description": "Get the current weather in a location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA"
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"]
                    }
                },
                "required": ["location"]
            }
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {"role": "user", "content": "What's the weather like in Boston?"}
        ],
        functions=functions,
        function_call="auto"
    )
    """)

    st.subheader("Vision Capabilities")
    st.code("""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "What's in this image?"},
                    {
                        "type": "image",
                        "image_url": {"url": "https://example.com/image.jpg"}
                    }
                ]
            }
        ]
    )
    """)

    st.subheader("Reproducible Outputs (Beta)")
    st.code("""
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",
        messages=[...],
        seed=42
    )
    """)

    st.subheader("Best Practices")
    st.markdown("""
    1. Use the latest models for improved performance and capabilities.
    2. Implement streaming for better user experience with long responses.
    3. Leverage function calling for structured interactions.
    4. Utilize vision capabilities for image-related tasks.
    5. Set a seed for reproducible outputs when needed.
    6. Always handle API errors and implement proper error handling.
    7. Monitor and optimize token usage to control costs.
    """)

    st.subheader("Visualization Example")
    st.code("""
    import matplotlib.pyplot as plt

    def plot_kpi_data(data, title="KPI Over Time"):
        plt.figure(figsize=(10, 6))
        plt.bar(data['period'], data['value'])
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("KPI Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)

    # Usage
    plot_kpi_data(processed_data, "Population Growth in Lund")
    """)

    st.subheader("Best Practices")
    st.markdown("""
    1. Always handle API errors and implement proper error handling.
    2. Use appropriate data types (e.g., integers for years, floats for KPI values).
    3. Implement caching for frequently accessed data to reduce API calls.
    4. Respect API rate limits and implement backoff strategies if necessary.
    5. Keep your municipality and KPI mappings up-to-date.
    6. Use pandas for efficient data manipulation and analysis.
    7. Provide clear visualizations to make the data more accessible.
    """)