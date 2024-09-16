import streamlit as st

def streamlit_basics():
    st.header("Streamlit Basics")
    
    st.subheader("Installation and Import")
    st.code(r"""
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