import pandas as pd
import sqlite3

# Load the CSV file into a DataFrame
csv_file_path = 'C:/Users/papin/Desktop/SQL_Chat/bollywood_movie.csv'  # Replace with the actual path
df = pd.read_csv(csv_file_path)

# Connect to SQLite (creates a new database file if it doesn't exist)
conn = sqlite3.connect('bollywood_movies1.db')
cursor = conn.cursor()

# Insert data from DataFrame into the SQLite table
df.to_sql('movies', conn, if_exists='replace', index=False)

# Commit changes
conn.commit()

# Verify: Check total number of records
count_query = 'SELECT COUNT(*) FROM movies'
count_result = cursor.execute(count_query).fetchone()
print(f"Total records inserted: {count_result[0]}")

# Sample Query: Retrieve top 5 movies with the highest IMDb rating
sample_query = '''
SELECT Title, IMDb_Rating, Audience_Score, Box_Office_Millions
FROM movies
ORDER BY IMDb_Rating DESC
LIMIT 5
'''
# Execute the sample query
result = cursor.execute(sample_query).fetchall()

# Display the result
print("\nTop 5 Movies by IMDb Rating:")
for row in result:
    print(row)

# Close the connection
conn.close()
