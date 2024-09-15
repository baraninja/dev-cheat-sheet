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
        "Deployment Guide",
        "Data Visualization",
        "Best Practices"
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
    elif choice == "Deployment Guide":
        deployment_guide()
    elif choice == "Data Visualization":
        data_visualization()
    elif choice == "Best Practices":
        best_practices()
    
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

if __name__ == "__main__":
    main()