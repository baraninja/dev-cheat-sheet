import streamlit as st

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
