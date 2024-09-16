import streamlit as st

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