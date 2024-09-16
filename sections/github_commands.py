import streamlit as st

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