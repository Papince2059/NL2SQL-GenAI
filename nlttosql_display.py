import sqlite3
import os
import pandas as pd
import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

# Load environment variables
load_dotenv()

# Initialize LLM via OpenRouter
llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct",
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    temperature=0
)

# Updated prompt template to ensure only SQL query is returned
prompt_template = """
You are an intelligent assistant that helps convert natural language queries into SQL queries. 
Your task is to take a natural language question and return only the SQL query. Do not provide any explanations, just return the query.

IMPORTANT:
- Only return the SQL query.
- Do not include any text, explanations, or commentary before or after the SQL query.
- Ensure the SQL query is clean and without any additional symbols, text, or commentary.

The table you are working with is named `movies`. Here are the details of the table and its columns:

Table Name: movies

1. Title: String. The exact name of the Bollywood movie or web series (e.g., "Padmaavat", "Dangal").
2. Type: String. Specifies whether the entry is a movie or a web series. Possible values: "Movie", "Web Series".
3. Release_Year: Integer. The year the movie or series was released (e.g., 2015, 2019).
4. Genre: String. The main genre or category of the movie or series. Possible values: "Action", "Drama", "Comedy", "Thriller", "Fantasy", "Historical", "Biography", "Sci-Fi", "Romance".
5. Director: String. Name of the director who directed the movie or series (e.g., "Kabir Khan", "Zoya Akhtar").
6. Production_House: String. The name of the production company that produced the movie or series (e.g., "Yash Raj Films", "Excel Entertainment").
7. Lead_Actors: String. Names of the lead actors, separated by commas (e.g., "Ranveer Singh, Alia Bhatt").
8. Language: String. Primary language in which the movie or series was released. Possible values: "Hindi", "English", "Marathi", "Tamil", "Telugu".
9. Budget_Millions: Float. Production budget in millions of INR, representing the investment made in the movie or series (e.g., 70.0, 150.5).
10. Box_Office_Millions: Float. Box office revenue in millions of INR for movies. For web series, this may be an estimate based on views (e.g., 238.0, 915.0).
11. OTT_Platform: String. The OTT platform where the movie or series is available for streaming. Possible values: "Netflix", "Amazon Prime", "Disney+ Hotstar", "Sony LIV", "Zee5".
12. Runtime_Minutes: Integer. Total runtime in minutes. Applicable to movies only (e.g., 120, 153).
13. No_of_Episodes: Integer. Number of episodes in the series. Applicable to web series only (e.g., 10, 12).
14. IMDb_Rating: Float. The IMDb rating out of 10, representing public reception and popularity (e.g., 8.4, 7.5).
15. Audience_Score: Integer. Average audience score percentage based on reviews (e.g., 85, 92).
16. Critics_Score: Integer. Average critics score percentage based on reviews from critics (e.g., 80, 88).
17. Awards_Nominations: Integer. Total number of award nominations the movie or series received (e.g., 14, 20).
18. Awards_Won: Integer. Total number of awards won (e.g., 5, 7).
19. Social_Media_Mentions: Integer. The number of mentions across social media platforms within the first six months post-release (e.g., 78000, 92000).
20. User_Reviews_Count: Integer. The total number of user reviews available on platforms like IMDb (e.g., 22000, 15000).
21. Viewership_Hours_Million: Float. Total viewership hours in millions within the first month post-release, indicative of popularity (e.g., 150.0, 200.5).

Now, based on the information provided, convert the following natural language question into an SQL query.

Ensure that you return ONLY the SQL query as plain text, nothing else. Start with SELECT and end with the semicolon.

Question: {question}

SQL Query:"""

# Define the prompt template using Langchain's PromptTemplate class
prompt = PromptTemplate(
    input_variables=["question"],
    template=prompt_template
)

# Create a Langchain pipeline that takes a natural language query and converts it to SQL
nl_to_sql_chain = prompt | llm

# Streamlit App Setup
st.title("NL to SQL Chatbot")

# User input for natural language question
user_input = st.text_input("Ask a question to generate an SQL query:", "")

# Connect to SQLite database
db_conn = sqlite3.connect('bollywood_movies1.db')

# Function to execute SQL and return results in a Pandas DataFrame
def execute_sql_and_return_df(sql_query, db_conn):
    try:
        # Execute the SQL query and fetch data into DataFrame
        result = pd.read_sql_query(sql_query, db_conn)
        return result
    except Exception as e:
        st.error(f"Error executing SQL query: {e}")
        return None

# Generate SQL query and execute if there is user input
if user_input:
    # Generate SQL from natural language input
    try:
        response = nl_to_sql_chain.invoke({"question": user_input})
        sql_query = response.content.strip() if response.content else ""
        
        if not sql_query:
            st.error("Failed to generate SQL query. Response was empty.")
        else:
            st.subheader("Generated SQL Query")
            st.code(sql_query, language="sql")  # Display SQL query

            # Execute SQL query and display results in a table format
            st.subheader("Query Results")
            result_df = execute_sql_and_return_df(sql_query, db_conn)
            if result_df is not None:
                st.dataframe(result_df)  # Display DataFrame as a table with Streamlit's built-in styling
    except Exception as e:
        st.error(f"Error generating SQL query: {str(e)}")
