import streamlit as st

def api_integration():
    st.header("API Integration")
    
    st.subheader("OpenAI API")
    st.code("""
    import os
    from openai import OpenAI
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv()

    # Set up the OpenAI client
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    # Make an API call
    response = client.chat.completions.create(
        model="gpt-4o-2024-08-06",  # Latest GPT-4o model as of knowledge cutoff
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ],
        max_tokens=150,
        temperature=0.7
    )

    print(response.choices[0].message.content)
    """)
    
    st.subheader("Anthropic API")
    st.code("""
    import os
    from anthropic import Anthropic
    from dotenv import load_dotenv

    # Load environment variables
    load_dotenv()

    # Set up the Anthropic client
    client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

    # Make an API call
    response = client.messages.create(
        model="claude-3.5-sonnet-20240620",  # Latest Claude model as of knowledge cutoff
        max_tokens=1000,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "What is the capital of France?"}
        ]
    )

    print(response.content[0].text)
    """)
    
    st.subheader("Handling API Keys Securely")
    st.markdown("""
    1. Create a `.env` file in your project root
    2. Add your API keys to the `.env` file:
       ```
       OPENAI_API_KEY=your_openai_api_key_here
       ANTHROPIC_API_KEY=your_anthropic_api_key_here
       ```
    3. Use `python-dotenv` to load environment variables
    4. Add `.env` to your `.gitignore` file to prevent committing sensitive information
    """)
    
    st.subheader("Error Handling for API Calls")
    st.code("""
    import os
    from openai import OpenAI
    from anthropic import Anthropic
    from dotenv import load_dotenv

    load_dotenv()

    def make_openai_call():
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        try:
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                messages=[{"role": "user", "content": "Hello, world!"}],
                max_tokens=150
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI API error: {str(e)}"

    def make_anthropic_call():
        client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))
        try:
            response = client.messages.create(
                model="claude-3.5-sonnet-20240620",
                max_tokens=1000,
                messages=[{"role": "user", "content": "Hello, world!"}]
            )
            return response.content[0].text
        except Exception as e:
            return f"Anthropic API error: {str(e)}"
    """)