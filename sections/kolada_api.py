import streamlit as st

def kolada_api():
    st.header("Kolada API Usage Guide")

    st.markdown("""
    The Kolada API provides access to standardized key performance indicators (KPIs) for Swedish municipalities and organizational units. This guide covers how to interact with the Kolada API, handle its data, and apply best practices.
    """)

    st.subheader("API Overview")
    st.markdown("""
    - **Municipal Data**: KPIs for Swedish municipalities (kommuner) and county councils (landsting), covering approximately 6500 KPIs.
    - **Organizational Unit Data**: KPIs for various organizational units (schools, hospitals, etc.), though with a smaller dataset.
    - Each KPI is measured annually and may be divided by gender (female, male, total).
    - Data is structured along four main dimensions: KPI, Municipality/Organizational Unit, Year, and Gender.
    """)

    st.subheader("Common Data Structure")
    st.code("""
    {
        "kpi": "<KPI ID>",
        "municipality": "<Municipality ID>",
        "period": "<Year>",
        "values": [
           {
             "count": <Number of Contributors>,
             "gender": "T|K|F",  // T = Total, K = Male, F = Female
             "status": "<Status>",
             "value": <KPI Value> or null
           }
        ]
    }
    """)

    st.subheader("Example API Calls")
    st.code("""
    import requests

    # KPI data for a specific municipality and year
    url = "http://api.kolada.se/v2/data/kpi/N00945/municipality/1860/year/2009"

    # Municipality metadata
    url = "http://api.kolada.se/v2/municipality?title=Stockholm"

    # Organizational Unit data
    url = "http://api.kolada.se/v2/oudata/kpi/N15033/ou/V15E144001301/year/2009"

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Process the data here
    else:
        print(f"Error: {response.status_code}")
    """)

    st.subheader("Handling Paginated Data")
    st.code("""
    def fetch_all_data(url):
        all_data = []
        while url:
            response = requests.get(url)
            if response.status_code == 200:
                json_response = response.json()
                all_data.extend(json_response['values'])
                url = json_response.get('next_page')
            else:
                print(f"Error: {response.status_code}")
                break
        return all_data
    """)

    st.subheader("Best Practices for Data Handling")
    st.markdown("""
    1. **Convert Period Field to Integer**:
    ```python
    data['period'] = data['period'].astype(int)
    ```

    2. **Format Numeric Values to Two Decimal Places**:
    ```python
    formatted_value = f"{value:.2f}"
    ```

    3. **Map Municipality IDs to Human-Readable Names**:
    ```python
    municipality_mapping = {
      "0114": "Upplands Väsby",
      "0180": "Stockholm",
      # Add more mappings as needed
    }
    data['municipality_name'] = data['municipality_id'].map(municipality_mapping)
    ```
    """)

    st.subheader("Data Processing Example")
    st.code("""
    import pandas as pd

    def process_kolada_data(raw_data):
        df = pd.DataFrame(raw_data)
        
        # Convert period to integer
        df['period'] = df['period'].astype(int)
        
        # Format KPI values to 2 decimal places
        df['value'] = df['value'].apply(lambda x: f"{x:.2f}" if x is not None else x)
        
        # Map municipality IDs to names
        municipality_mapping = {
            "1860": "Lund",
            "0180": "Stockholm",
            # Add more mappings as needed
        }
        df['municipality_name'] = df['municipality'].map(municipality_mapping)
        
        return df

    # Usage
    raw_data = fetch_all_data("http://api.kolada.se/v2/data/kpi/N00945/municipality/1860/year/2009")
    processed_data = process_kolada_data(raw_data)
    """)

    st.subheader("Visualization Example")
    st.code("""
    import matplotlib.pyplot as plt

    def plot_kpi_data(data, title="KPI Over Time"):
        plt.figure(figsize=(10, 6))
        plt.bar(data['period'], data['value'])
        plt.title(title)
        plt.xlabel("Year")
        plt.ylabel("KPI Value")
        plt.xticks(rotation=45)
        plt.tight_layout()
        st.pyplot(plt)

    # Usage
    plot_kpi_data(processed_data, "Population Growth in Lund")
    """)

    st.subheader("Best Practices")
    st.markdown("""
    1. Always handle API errors and implement proper error handling.
    2. Use appropriate data types (e.g., integers for years, floats for KPI values).
    3. Implement caching for frequently accessed data to reduce API calls.
    4. Respect API rate limits and implement backoff strategies if necessary.
    5. Keep your municipality and KPI mappings up-to-date.
    6. Use pandas for efficient data manipulation and analysis.
    7. Provide clear visualizations to make the data more accessible.
    """)