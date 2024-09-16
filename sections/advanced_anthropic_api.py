import streamlit as st

def advanced_anthropic_api():
    st.header("Advanced Anthropic API Usage")

    st.subheader("Latest Anthropic Models (cost in USD)")
    st.markdown("""
    - **Claude 3.5 Sonnet**: 
        - API Model Name: claude-3-5-sonnet-20240620
        - Max Tokens: 200,000
        - Cost: 3.00 / 15.00 per 1M tokens (input/output)
    - **Claude 3 Opus**:
        - API Model Name: claude-3-opus-20240229
        - Max Tokens: 200,000
        - Cost: 15.00 / 75.00 per 1M tokens (input/output)
    - **Claude 3 Sonnet**:
        - API Model Name: claude-3-sonnet-20240229
        - Max Tokens: 200,000
        - Cost: 3.00 / 15.00 per 1M tokens (input/output)
    - **Claude 3 Haiku**:
        - API Model Name: claude-3-haiku-20240307
        - Max Tokens: 200,000
        - Cost: 0.25 / 1.25 per 1M tokens (input/output)
    """)

    st.subheader("Basic API Call")
    st.code("""
    import anthropic

    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system="You are a world-class poet. Respond only with short poems.",
        messages=[
            {
                "role": "user",
                "content": "Why is the ocean salty?"
            }
        ]
    )
    print(response.content)
    """)

    st.subheader("Structured Outputs")
    st.markdown("""
    Claude can generate structured outputs adhering to a specified JSON Schema.
    """)
    st.code("""
    from pydantic import BaseModel

    class CalendarEvent(BaseModel):
        name: str
        date: str
        participants: list[str]

    completion = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system="Extract the event information.",
        messages=[
            {
                "role": "user",
                "content": "Alice and Bob are attending a meeting on September 15th."
            }
        ],
        response_format=CalendarEvent.schema_json()
    )

    event = CalendarEvent.parse_raw(completion.content[0].text)
    print(event)
    """)

    st.subheader("Tool Use")
    st.markdown("""
    Claude can be equipped with custom tools to handle specific queries.
    """)
    st.code("""
    weather_tool = {
        "name": "get_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string", "description": "City and state"},
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
            },
            "required": ["location"]
        }
    }

    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system="You are a helpful assistant.",
        messages=[
            {
                "role": "user",
                "content": "What's the weather like in San Francisco?"
            }
        ],
        tools=[weather_tool]
    )
    """)

    st.subheader("Prompt Caching (Beta)")
    st.markdown("""
    Prompt Caching optimizes API usage by storing and reusing sections of your prompt.
    """)
    st.code("""
    response = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=1000,
        system=[
            {
                "type": "text", 
                "text": "You are an AI assistant tasked with analyzing literary works."
            },
            {
                "type": "text", 
                "text": "<the entire contents of Pride and Prejudice>",
                "cache_control": {"type": "ephemeral"}
            }
        ],
        messages=[
            {
                "role": "user",
                "content": "Analyze the major themes in Pride and Prejudice."
            }
        ]
    )
    """)

    st.subheader("Best Practices")
    st.markdown("""
    1. Use structured outputs for consistent data formats.
    2. Leverage tool use for complex, multi-step tasks.
    3. Implement prompt caching for improved performance with large contexts.
    4. Always handle API errors gracefully.
    5. Monitor token usage to control costs.
    """)