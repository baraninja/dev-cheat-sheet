import streamlit as st
import base64

def main():
    st.set_page_config(page_title="Developer's Cheat Sheet", layout="wide")
    
    st.title("Developer's Cheat Sheet")
    st.sidebar.title("Navigation")
    
    sections = [
        "Streamlit Basics",
        "Streamlit Advanced",
        "Python Tips",
        "VS Code Shortcuts",
        "GitHub Commands",
        "Replit Tips",
        "API Integration",
        "GitHub Models",
        "Perplexity API",
        "Advanced Anthropic API",
        "Advanced OpenAI API",
        "Kolada API",
        "Deployment Guide",
        "Data Visualization",
        "Best Practices",
        "GitHub Integration Guide"
    ]
    
    choice = st.sidebar.radio("Go to", sections)
    
    if choice == "Streamlit Basics":
        streamlit_basics()
    elif choice == "Streamlit Advanced":
        streamlit_advanced()
    elif choice == "Python Tips":
        python_tips()
    elif choice == "VS Code Shortcuts":
        vscode_shortcuts()
    elif choice == "GitHub Commands":
        github_commands()
    elif choice == "Replit Tips":
        replit_tips()
    elif choice == "API Integration":
        api_integration()
    elif choice == "GitHub Models":
        github_models()
    elif choice == "Perplexity API":
        perplexity_api()
    elif choice == "Advanced Anthropic API":
        advanced_anthropic_api()
    elif choice == "Advanced OpenAI API":
        advanced_openai_api()
    elif choice == "Kolada API":
        kolada_api()
    elif choice == "Deployment Guide":
        deployment_guide()
    elif choice == "Data Visualization":
        data_visualization()
    elif choice == "Best Practices":
        best_practices()
    elif choice == "GitHub Integration Guide":
        github_integration_guide()
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("Developed by Anders Barane")

def streamlit_basics():
    st.header("Streamlit Basics")
    
    st.subheader("Installation and Import")
    st.code("""
    # Install Streamlit
    $ pip install streamlit

    # Import in your script
    import streamlit as st
    """)
    
    st.subheader("Running Streamlit Apps")
    st.code("""
    # Run a Streamlit app
    $ streamlit run your_script.py

    # Show Streamlit commands
    $ streamlit --help

    # Clear cache
    $ streamlit cache clear

    # View Streamlit version
    $ streamlit --version
    """)
    
    st.subheader("Display Text and Data")
    st.code("""
    # Display text
    st.text('Fixed width text')
    st.markdown('_Markdown_')
    st.caption('Balloons. Hundreds of them...')
    st.latex(r''' e^{i\pi} + 1 = 0 ''')
    st.write('Most objects') # df, err, func, keras!
    st.write(['st', 'is <', 3]) # see *
    st.title('My title')
    st.header('My header')
    st.subheader('My sub')
    st.code('for i in range(8): foo()')

    # Display data
    st.dataframe(my_dataframe)
    st.table(data.iloc[0:10])
    st.json({'foo':'bar','fu':'ba'})
    st.metric(label="Temp", value="273 K", delta="1.2 K")
    """)
    
    st.subheader("Display Media")
    st.code("""
    st.image('./image.png')
    st.audio(data)
    st.video(data)
    """)
    
    st.subheader("Layouts and Containers")
    st.code("""
    # Create columns
    col1, col2 = st.columns(2)
    with col1:
        st.write('Column 1')
    with col2:
        st.write('Column 2')

    # Create tabs
    tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
    with tab1:
        st.write("This is tab 1")
    with tab2:
        st.write("This is tab 2")

    # Create expandable sections
    with st.expander("Click to expand"):
        st.write("This content is hidden by default")
    """)
    
    st.subheader("Input Widgets")
    st.code("""
    st.button('Hit me')
    st.data_editor('Edit data', data)
    st.checkbox('Check me out')
    st.radio('Pick one:', ['nose','ear'])
    st.selectbox('Select', [1,2,3])
    st.multiselect('Multiselect', [1,2,3])
    st.slider('Slide me', min_value=0, max_value=10)
    st.select_slider('Slide to select', options=[1,'2'])
    st.text_input('Enter some text')
    st.number_input('Enter a number')
    st.text_area('Area for textual entry')
    st.date_input('Date input')
    st.time_input('Time entry')
    st.file_uploader('File uploader')
    st.color_picker('Pick a color')
    """)
    
    st.subheader("Control Flow")
    st.code("""
    # Stop execution
    st.stop()

    # Rerun script
    st.experimental_rerun()

    # Group widgets
    with st.form(key='my_form'):
        username = st.text_input('Username')
        password = st.text_input('Password')
        st.form_submit_button('Login')
    """)

def streamlit_advanced():
    st.header("Streamlit Advanced Features")
    
    st.subheader("Caching")
    st.code("""
    # Cache data objects
    @st.cache_data
    def fetch_and_clean_data(url):
        # Fetch data from URL here, and then clean it up.
        return data

    # Cache resource-intensive computations
    @st.cache_resource
    def load_large_file():
        with open("large_file.csv", "r") as f:
            data = f.read()
        return data
    """)
    
    st.subheader("Session State")
    st.code("""
    # Initialize session state
    if 'count' not in st.session_state:
        st.session_state.count = 0

    # Increment counter
    if st.button('Increment'):
        st.session_state.count += 1

    # Display count
    st.write('Count = ', st.session_state.count)
    """)
    
    st.subheader("Custom Components")
    st.code("""
    from streamlit_custom_component import declare_component

    my_component = declare_component("my_component")

    # Use the custom component
    component_value = my_component(greeting="Hello", name="Streamlit")
    """)
    
    st.subheader("Theming")
    st.code("""
    # In your .streamlit/config.toml file:
    [theme]
    primaryColor="#F63366"
    backgroundColor="#FFFFFF"
    secondaryBackgroundColor="#F0F2F6"
    textColor="#262730"
    font="sans serif"
    """)
    
    st.subheader("Performance Optimization")
    st.code("""
    # Use st.empty for dynamic content
    placeholder = st.empty()

    # Update the placeholder
    with placeholder.container():
        st.write("This content can be dynamically updated")

    # Clear the placeholder
    placeholder.empty()
    """)
    
    st.subheader("Error Handling and Debugging")
    st.code("""
    import traceback

    try:
        # Your code here
        result = risky_operation()
    except Exception as e:
        st.error(f"An error occurred: {e}")
        st.text(traceback.format_exc())
    """)
    
    st.subheader("Streamlit Components")
    st.code("""
    # Chat messages
    with st.chat_message("user"):
        st.write("Hello 👋")

    # Chat input
    prompt = st.chat_input("Say something")
    if prompt:
        st.write(f"User said: {prompt}")

    # Progress and status
    with st.spinner('In progress'):
        time.sleep(3)
    st.success('Done!')

    progress_bar = st.progress(0)
    for i in range(100):
        progress_bar.progress(i + 1)
        time.sleep(0.1)

    st.balloons()
    st.snow()
    st.toast('Mr Stay-Puft')
    """)

def python_tips():
    st.header("Python Tips")
    
    st.subheader("Virtual Environments")
    st.code("""
    # Create a virtual environment
    python -m venv myenv

    # Activate the environment
    # On Windows:
    myenv\Scripts\activate
    # On macOS and Linux:
    source myenv/bin/activate

    # Install packages
    pip install package_name

    # Generate requirements.txt
    pip freeze > requirements.txt
    """)
    
    st.subheader("Error Handling")
    st.code("""
    try:
        # Code that might raise an exception
        result = risky_function()
    except SomeSpecificError as e:
        # Handle specific error
        st.error(f"An error occurred: {e}")
    except Exception as e:
        # Handle any other exception
        st.error(f"An unexpected error occurred: {e}")
    else:
        # Code to run if no exception occurs
        st.success("Operation completed successfully!")
    finally:
        # Code that will always run
        cleanup_function()
    """)
    
    st.subheader("List Comprehensions")
    st.code("""
    # Create a list of squares
    squares = [x**2 for x in range(10)]

    # Filter a list
    even_numbers = [x for x in range(20) if x % 2 == 0]

    # Nested list comprehension
    matrix = [[i*j for j in range(5)] for i in range(5)]
    """)

def vscode_shortcuts():
    st.header("VS Code Shortcuts")
    
    shortcuts = [
        ("Ctrl+Shift+P", "Open Command Palette"),
        ("Ctrl+P", "Quick Open, Go to File"),
        ("Ctrl+Shift+N", "New Window/Instance"),
        ("Ctrl+Shift+W", "Close Window/Instance"),
        ("Ctrl+,", "User Settings"),
        ("Ctrl+K Ctrl+S", "Keyboard Shortcuts"),
        ("Ctrl+X", "Cut line"),
        ("Ctrl+C", "Copy line"),
        ("Alt+ ↑ / ↓", "Move line up/down"),
        ("Shift+Alt + ↓ / ↑", "Copy line up/down"),
        ("Ctrl+Shift+K", "Delete line"),
        ("Ctrl+Enter", "Insert line below"),
        ("Ctrl+Shift+Enter", "Insert line above"),
        ("Ctrl+Shift+\\", "Jump to matching bracket"),
        ("Ctrl+] / [", "Indent/outdent line"),
        ("Home / End", "Go to beginning/end of line"),
        ("Ctrl+Home", "Go to beginning of file"),
        ("Ctrl+End", "Go to end of file"),
        ("Ctrl+↑ / ↓", "Scroll line up/down"),
        ("Alt+PgUp / PgDn", "Scroll page up/down"),
        ("Ctrl+Shift+[", "Fold (collapse) region"),
        ("Ctrl+Shift+]", "Unfold (uncollapse) region"),
        ("Ctrl+K Ctrl+[", "Fold (collapse) all subregions"),
        ("Ctrl+K Ctrl+]", "Unfold (uncollapse) all subregions"),
        ("Ctrl+K Ctrl+0", "Fold (collapse) all regions"),
        ("Ctrl+K Ctrl+J", "Unfold (uncollapse) all regions"),
    ]
    
    for shortcut, description in shortcuts:
        st.code(shortcut, language="")
        st.write(description)
        st.write("")

def github_commands():
    st.header("GitHub Commands")
    
    st.subheader("Basic Git Commands")
    st.code("""
    # Initialize a new Git repository
    git init

    # Clone a repository
    git clone <repository-url>

    # Check status of your repository
    git status

    # Add files to staging area
    git add <file-name>
    git add .  # Add all files

    # Commit changes
    git commit -m "Commit message"

    # Push changes to remote repository
    git push origin <branch-name>

    # Pull changes from remote repository
    git pull origin <branch-name>

    # Create and switch to a new branch
    git checkout -b <new-branch-name>

    # Switch to an existing branch
    git checkout <branch-name>

    # Merge branches
    git merge <branch-name>

    # View commit history
    git log
    """)
    
    st.subheader("Advanced Git Commands")
    st.code("""
    # Stash changes
    git stash
    git stash pop

    # Rebase branches
    git rebase <base-branch>

    # Cherry-pick commits
    git cherry-pick <commit-hash>

    # Reset to a specific commit
    git reset --hard <commit-hash>

    # Undo last commit (keeping changes)
    git reset --soft HEAD~1

    # Amend last commit
    git commit --amend
    """)

def replit_tips():
    st.header("Replit Tips")
    
    st.subheader("Getting Started")
    st.markdown("""
    1. Create an account on [Replit](https://replit.com)
    2. Click on "+ New repl" to start a new project
    3. Choose your programming language or start from a template
    """)
    
    st.subheader("Key Features")
    st.markdown("""
    - **Multiplayer Coding**: Collaborate in real-time with other developers
    - **Hosting**: Deploy web apps directly from Replit
    - **Database**: Use Replit's built-in key-value store database
    - **Version Control**: Integrated Git support
    - **Package Management**: Install packages directly from the shell
    """)
    
    st.subheader("Useful Shortcuts")
    st.code("""
    Ctrl + Enter: Run code
    Ctrl + S: Save changes
    Ctrl + /: Toggle comment
    Ctrl + F: Find in file
    Ctrl + Shift + F: Find in all files
    """)
    
    st.subheader("Using Replit for Streamlit")
    st.code("""
    # In the Shell:
    pip install streamlit

    # In your main.py:
    import streamlit as st

    st.write("Hello, Streamlit on Replit!")

    # To run:
    streamlit run main.py
    """)
    
    st.markdown("Remember to set the run command to `streamlit run main.py` in the `.replit` file.")

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

def deployment_guide():
    st.header("Deployment Guide")
    
    st.subheader("Deploying to Streamlit Community Cloud")
    st.markdown("""
    1. Push your code to a GitHub repository
    2. Sign up for [Streamlit Community Cloud](https://streamlit.io/cloud)
    3. Connect your GitHub account
    4. Select the repository and branch to deploy
    5. Configure your app settings (Python version, packages, etc.)
    6. Deploy your app
    """)
    
    st.subheader("Deploying to Heroku")
    st.markdown("""
    1. Sign up for a [Heroku account](https://signup.heroku.com/)
    2. Install the Heroku CLI
    3. Create a `Procfile` in your project root:
       ```
       web: streamlit run app.py
       ```
    4. Create a `requirements.txt` file:
       ```
       pip freeze > requirements.txt
       ```
    5. Initialize a Git repository (if not already done)
    6. Create a new Heroku app:
       ```
       heroku create your-app-name
       ```
    7. Set environment variables:
       ```
       heroku config:set OPENAI_API_KEY=your_api_key_here
       ```
    8. Deploy your app:
       ```
       git push heroku main
       ```
    """)
    
    st.subheader("Managing Environment Variables")
    st.markdown("""
    - For local development, use a `.env` file and `python-dotenv`
    - For Streamlit Community Cloud, use the Secrets Management feature
    - For Heroku, use config vars in the app settings or Heroku CLI
    """)

def github_models():
    st.header("GitHub Models Implementation")
    
    st.subheader("Setting Up")
    st.code("""
    import os
    from openai import OpenAI
    from azure.ai.inference import ChatCompletionsClient
    from azure.ai.inference.models import SystemMessage, UserMessage
    from azure.core.credentials import AzureKeyCredential
    from mistralai import Mistral, UserMessage, SystemMessage

    # Set up environment variables
    os.environ["GITHUB_TOKEN"] = "your-github-token-here"
    ENDPOINT = "https://models.inference.ai.azure.com"
    """)
    
    st.subheader("Using GPT-4 Models")
    st.code("""
    def use_gpt4_model():
        client = OpenAI(
            base_url=ENDPOINT,
            api_key=os.environ["GITHUB_TOKEN"],
        )

        response = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": "What is the capital of France?"}
            ],
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0
        )

        return response.choices[0].message.content
    """)
    
    st.subheader("Using Meta LLaMA Models")
    st.code("""
    def use_llama_model():
        client = ChatCompletionsClient(
            endpoint=ENDPOINT,
            credential=AzureKeyCredential(os.environ["GITHUB_TOKEN"]),
        )

        response = client.complete(
            messages=[
                SystemMessage(content="You are a helpful assistant."),
                UserMessage(content="What is the capital of France?"),
            ],
            model="meta-llama-3.1-70b-instruct",
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0
        )

        return response.choices[0].message.content
    """)
    
    st.subheader("Using Mistral Models")
    st.code("""
    def use_mistral_model():
        client = Mistral(api_key=os.environ["GITHUB_TOKEN"], server_url=ENDPOINT)

        response = client.chat.complete(
            model="Mistral-large-2407",
            messages=[
                SystemMessage(content="You are a helpful assistant."),
                UserMessage(content="What is the capital of France?"),
            ],
            temperature=1.0,
            max_tokens=1000,
            top_p=1.0
        )

        return response.choices[0].message.content
    """)
    
    st.subheader("Handling Multiple Tools")
    st.markdown("""
    When working with GitHub models, you can provide multiple tools in one request. The model will choose which tool to use based on the user's query. This allows for more flexible and context-aware responses.
    """)
    
    st.subheader("Error Handling and Best Practices")
    st.code("""
    def safe_model_call(model_func):
        try:
            return model_func()
        except Exception as e:
            return f"An error occurred: {str(e)}"

    # Usage
    result = safe_model_call(use_gpt4_model)
    """)

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

def advanced_anthropic_api():
    st.header("Advanced Anthropic API Usage")

    st.subheader("Latest Anthropic Models")
    st.markdown("""
    - **Claude 3.5 Sonnet**: 
        - API Model Name: claude-3-5-sonnet-20240620
        - Max Tokens: 200,000
        - Cost: $3.00 / $15.00 per 1M tokens (input/output)
    - **Claude 3 Opus**:
        - API Model Name: claude-3-opus-20240229
        - Max Tokens: 200,000
        - Cost: $15.00 / $75.00 per 1M tokens (input/output)
    - **Claude 3 Sonnet**:
        - API Model Name: claude-3-sonnet-20240229
        - Max Tokens: 200,000
        - Cost: $3.00 / $15.00 per 1M tokens (input/output)
    - **Claude 3 Haiku**:
        - API Model Name: claude-3-haiku-20240307
        - Max Tokens: 200,000
        - Cost: $0.25 / $1.25 per 1M tokens (input/output)
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

def kolada_api():
    st.header("Kolada API Usage Guide")

    st.markdown("""
    The Kolada API provides access to standardized key performance indicators (KPIs) for Swedish municipalities and organizational units. This guide covers how to interact with the Kolada API, handle its data, and apply best practices.
    """)

    st.subheader("API Overview")
    st.markdown("""
    - **Municipal Data**: KPIs for Swedish municipalities (kommuner) and county councils (landsting), covering approximately 6500 KPIs.
    - **Organizational Unit Data**: KPIs for various organizational units (schools, hospitals, etc.), though with a smaller dataset.
    - Each KPI is measured annually and may be divided by gender (female, male, total).
    - Data is structured along four main dimensions: KPI, Municipality/Organizational Unit, Year, and Gender.
    """)

    st.subheader("Common Data Structure")
    st.code("""
    {
        "kpi": "<KPI ID>",
        "municipality": "<Municipality ID>",
        "period": "<Year>",
        "values": [
           {
             "count": <Number of Contributors>,
             "gender": "T|K|F",  // T = Total, K = Male, F = Female
             "status": "<Status>",
             "value": <KPI Value> or null
           }
        ]
    }
    """)

    st.subheader("Example API Calls")
    st.code("""
    import requests

    # KPI data for a specific municipality and year
    url = "http://api.kolada.se/v2/data/kpi/N00945/municipality/1860/year/2009"

    # Municipality metadata
    url = "http://api.kolada.se/v2/municipality?title=Stockholm"

    # Organizational Unit data
    url = "http://api.kolada.se/v2/oudata/kpi/N15033/ou/V15E144001301/year/2009"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data here
    else:
        print(f"Error: {response.status_code}")
    """)

    st.subheader("Handling Paginated Data")
    st.code("""
    def fetch_all_data(url):
        all_data = []
        while url:
            response = requests.get(url)
            if response.status_code == 200:
                json_response = response.json()
                all_data.extend(json_response['values'])
                url = json_response.get('next_page')
            else:
                print(f"Error: {response.status_code}")
                break
        return all_data
    """)

    st.subheader("Best Practices for Data Handling")
    st.markdown("""
    1. **Convert Period Field to Integer**:
    ```python
    data['period'] = data['period'].astype(int)
    ```

    2. **Format Numeric Values to Two Decimal Places**:
    ```python
    formatted_value = f"{value:.2f}"
    ```

    3. **Map Municipality IDs to Human-Readable Names**:
    ```python
    municipality_mapping = {
      "0114": "Upplands Väsby",
      "0180": "Stockholm",
      # Add more mappings as needed
    }
    data['municipality_name'] = data['municipality_id'].map(municipality_mapping)
    ```
    """)

    st.subheader("Data Processing Example")
    st.code("""
    import pandas as pd

    def process_kolada_data(raw_data):
        df = pd.DataFrame(raw_data)
        
        # Convert period to integer
        df['period'] = df['period'].astype(int)
        
        # Format KPI values to 2 decimal places
        df['value'] = df['value'].apply(lambda x: f"{x:.2f}" if x is not None else x)
        
        # Map municipality IDs to names
        municipality_mapping = {
            "1860": "Lund",
            "0180": "Stockholm",
            # Add more mappings as needed
        }
        df['municipality_name'] = df['municipality'].map(municipality_mapping)
        
        return df

    # Usage
    raw_data = fetch_all_data("http://api.kolada.se/v2/data/kpi/N00945/municipality/1860/year/2009")
    processed_data = process_kolada_data(raw_data)
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

def advanced_openai_api():
    st.header("Advanced OpenAI API Usage")

    st.subheader("Latest OpenAI Models")
    st.markdown("""
    - **GPT-4o (2024-08-06)**:
        - API Model Name: gpt-4o-2024-08-06
        - Max Tokens: 128,000
        - Max Output Tokens: 16,384
        - Cost: $2.50 per 1K input tokens, $7.50 per 1K output tokens
    - **GPT-4o (2024-05-13)**:
        - API Model Name: gpt-4o-2024-05-13
        - Max Tokens: 128,000
        - Max Output Tokens: 4,096
        - Cost: $5.00 per 1K input tokens, $15.00 per 1K output tokens
    - **GPT-4o-mini (2024-07-18)**:
        - API Model Name: gpt-4o-mini-2024-07-18
        - Max Tokens: 128,000
        - Cost: $0.15 per 1M input tokens, $0.60 per 1M output tokens
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


def data_visualization():
    st.header("Data Visualization in Streamlit")
    
    st.subheader("Using Matplotlib")
    st.code("""
    import matplotlib.pyplot as plt
    import numpy as np

    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x))
    st.pyplot(fig)
    """)
    
    st.subheader("Using Plotly")
    st.code("""
    import plotly.express as px
    import pandas as pd

    df = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 11, 12, 13]
    })
    fig = px.scatter(df, x='x', y='y')
    st.plotly_chart(fig)
    """)
    
    st.subheader("Using Altair")
    st.code("""
    import altair as alt
    import pandas as pd

    df = pd.DataFrame({
        'x': [1, 2, 3, 4],
        'y': [10, 11, 12, 13]
    })
    chart = alt.Chart(df).mark_circle().encode(
        x='x',
        y='y'
    )
    st.altair_chart(chart)
    """)

def best_practices():
    st.header("Best Practices for Streamlit Development")
    
    st.subheader("Code Organization")
    st.markdown("""
    - Use functions to organize your code
    - Separate data loading, processing, and visualization logic
    - Use config files for app settings
    """)
    
    st.subheader("Performance Optimization")
    st.markdown("""
    - Use caching for expensive computations
    - Optimize data loading and processing
    - Use efficient data structures (e.g., NumPy arrays for numerical computations)
    """)
    
    st.subheader("User Experience")
    st.markdown("""
    - Provide clear instructions and tooltips
    - Use appropriate widgets for input
    - Implement error handling and provide user feedback
    - Design responsive layouts
    """)
    
    st.subheader("Security")
    st.markdown("""
    - Never hardcode sensitive information (use st.secrets or environment variables)
    - Validate and sanitize user inputs
    - Use HTTPS for deployed apps
    """)
    
    st.subheader("Testing")
    st.markdown("""
    - Write unit tests for your functions
    - Perform integration testing for your Streamlit app
    - Test your app on different browsers and devices
    """)

def github_integration_guide():
    st.header("Get It All Into GitHub: A Comprehensive Guide")

    st.markdown("""
    This guide will walk you through the process of getting your Streamlit app and all related files into GitHub, from initial setup to ongoing maintenance.
    """)

    st.subheader("1. Prerequisites")
    st.markdown("""
    - Install Git on your local machine
    - Create a GitHub account
    - Set up SSH key for GitHub (optional but recommended)
    """)

    st.subheader("2. Initialize Local Git Repository")
    st.code("""
    # Navigate to your project directory
    cd path/to/your/streamlit/project

    # Initialize a new Git repository
    git init
    """)

    st.subheader("3. Create .gitignore File")
    st.markdown("Create a `.gitignore` file to exclude unnecessary files from version control.")
    st.code("""
    # .gitignore file content
    *.pyc
    __pycache__
    .env
    venv/
    .streamlit/secrets.toml
    """)

    st.subheader("4. Stage and Commit Files")
    st.code("""
    # Add all files to staging area
    git add .

    # Commit changes
    git commit -m "Initial commit"
    """)

    st.subheader("5. Create GitHub Repository")
    st.markdown("""
    1. Go to GitHub and log in
    2. Click the '+' icon and select 'New repository'
    3. Name your repository and add a description
    4. Choose public or private
    5. Do not initialize with README, .gitignore, or license
    6. Click 'Create repository'
    """)

    st.subheader("6. Link Local Repository to GitHub")
    st.code("""
    # Add the remote repository
    git remote add origin https://github.com/yourusername/your-repo-name.git

    # Push your code to GitHub
    git push -u origin main
    """)

    st.subheader("7. Verify Files on GitHub")
    st.markdown("Check your GitHub repository to ensure all files have been pushed correctly.")

    st.subheader("8. Ongoing Maintenance")
    st.markdown("""
    - Regular commits: Make small, frequent commits with clear messages
    - Push changes: Regularly push your changes to GitHub
    - Pull before working: Always pull the latest changes before starting work
    - Use branches: Create feature branches for new developments
    """)

    st.subheader("9. Collaborating with Others")
    st.markdown("""
    - Invite collaborators in GitHub repository settings
    - Use Pull Requests for code reviews
    - Resolve merge conflicts when they arise
    """)

    st.subheader("10. GitHub Actions for Streamlit")
    st.markdown("""
    Consider setting up GitHub Actions for continuous integration and deployment of your Streamlit app.
    """)
    st.code("""
    # Example .github/workflows/streamlit_app.yml
    name: Streamlit App CI/CD

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:
        runs-on: ubuntu-latest
        steps:
        - uses: actions/checkout@v2
        - name: Set up Python
          uses: actions/setup-python@v2
          with:
            python-version: 3.8
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Run tests
          run: python -m unittest discover tests
    """)

    st.subheader("11. Managing Secrets")
    st.markdown("""
    - Never commit sensitive information (API keys, passwords) to GitHub
    - Use environment variables or Streamlit's secrets management for local development
    - For deployment, use the platform's secret management system (e.g., GitHub Secrets for GitHub Actions)
    """)

    st.subheader("12. Documentation")
    st.markdown("""
    - Create a README.md file with:
      - Project description
      - Installation instructions
      - Usage guide
      - Contribution guidelines
    - Keep documentation up-to-date as your project evolves
    """)

    st.subheader("13. Versioning")
    st.markdown("""
    - Use semantic versioning for releases (MAJOR.MINOR.PATCH)
    - Create Git tags for important releases
    - Maintain a CHANGELOG.md to track changes
    """)

    st.markdown("""
    By following this guide, you'll have a robust GitHub workflow for your Streamlit project, 
    enabling effective version control, collaboration, and potentially automated deployment.
    """)

if __name__ == "__main__":
    main()