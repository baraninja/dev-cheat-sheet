import streamlit as st

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