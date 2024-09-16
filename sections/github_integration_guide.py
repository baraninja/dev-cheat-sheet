import streamlit as st

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