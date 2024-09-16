import streamlit as st

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
