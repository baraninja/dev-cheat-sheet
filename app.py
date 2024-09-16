import streamlit as st
from sections.streamlit_basics import streamlit_basics
from sections.streamlit_advanced import streamlit_advanced
from sections.python_tips import python_tips
from sections.vscode_shortcuts import vscode_shortcuts
from sections.github_commands import github_commands
from sections.replit_tips import replit_tips
from sections.api_integration import api_integration
from sections.github_models import github_models
from sections.perplexity_api import perplexity_api
from sections.advanced_anthropic_api import advanced_anthropic_api
from sections.advanced_openai_api import advanced_openai_api
from sections.kolada_api import kolada_api
from sections.deployment_guide import deployment_guide
from sections.data_visualization import data_visualization
from sections.best_practices import best_practices
from sections.github_integration_guide import github_integration_guide

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

if __name__ == "__main__":
    main()