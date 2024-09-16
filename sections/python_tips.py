import streamlit as st

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