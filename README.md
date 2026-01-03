# NL to SQL Chatbot - Bollywood Movies Database

A natural language to SQL converter powered by AI, allowing you to query a Bollywood movies database using plain English questions.

## Overview

This project converts natural language questions into SQL queries using an LLM (Large Language Model) via OpenRouter API. It provides both a command-line interface and an interactive Streamlit web application for querying a SQLite database of Bollywood movies.

## Features

- **Natural Language Processing**: Convert English questions to SQL queries automatically
- **Interactive Web Interface**: User-friendly Streamlit app for easy querying
- **SQLite Database**: Pre-loaded with Bollywood movie data
- **OpenRouter Integration**: Uses OpenRouter's API for LLM access
- **CSV to Database**: Automated conversion of CSV data to SQLite

## Project Structure

```
SQL_Chat/
├── main.py                 # Entry point / Configuration test
├── sqldata.py              # CSV -> SQLite database conversion
├── nlttosql_display.py     # Streamlit web app (main interface)
├── view_data.sql           # SQL queries to view database content
├── bollywood_movie.csv     # Source data file
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (API keys, DO NOT commit)
```

## Requirements

- Python 3.8+
- pip (Python package manager)
- OpenRouter API key

## Installation

### 1. Clone/Setup the Project
```bash
cd SQL_Chat
```

### 2. Create Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Setup Environment Variables
Create a `.env` file in the project root:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Get your OpenRouter API key from: https://openrouter.ai/

## Usage

### Option 1: Streamlit Web App (Recommended)
```bash
python -m streamlit run nlttosql_display.py
```
Then open your browser to: `http://localhost:8501`

### Option 2: Command-Line Interface
```bash
python nlttosql.py
```

### Option 3: Initialize/Reset Database
```bash
python sqldata.py
```

## Database Setup

### First-Time Setup
1. Ensure `bollywood_movie.csv` is in the project directory
2. Run `python sqldata.py` to create/populate the SQLite database
3. The database will be created as `bollywood_movies1.db`

### View Database Content
Open `bollywood_movies1.db` with VS Code SQLite extension or run:
```bash
# View sample queries in view_data.sql
```

## Database Schema

The `movies` table contains:
- **Title**: Movie/Series name
- **Type**: "Movie" or "Web Series"
- **Release_Year**: Year of release
- **Genre**: Action, Drama, Comedy, Thriller, Fantasy, Historical, Biography, Sci-Fi, Romance
- **Director**: Director name
- **Production_House**: Production company
- **Lead_Actors**: Main actors (comma-separated)
- **Language**: Hindi, English, Marathi, Tamil, Telugu
- **Budget_Millions**: Production budget in millions
- **Box_Office_Millions**: Box office revenue in millions
- **OTT_Platform**: Netflix, Amazon Prime, Disney+ Hotstar, Sony LIV, Zee5
- **Runtime_Minutes**: Duration (movies)
- **No_of_Episodes**: Episode count (web series)
- **IMDb_Rating**: Rating out of 10
- **Audience_Score**: Audience score percentage
- **Critics_Score**: Critics score percentage
- **Awards_Nominations**: Total nominations
- **Awards_Won**: Total wins
- **Social_Media_Mentions**: Social media mentions count
- **User_Reviews_Count**: Total user reviews
- **Viewership_Hours_Million**: Total viewership hours in millions

## Example Queries

Try asking the chatbot:
- "Total number of unique movies"
- "Top 10 movies by IMDb rating"
- "List all Bollywood movies released after 2019"
- "Find movies with budget over 100 million"
- "Count movies by genre"
- "Show all movies directed by Rajkumar Hirani"

## Configuration

### LLM Model
The project uses `mistralai/mistral-7b-instruct` via OpenRouter. To change the model:

1. Edit `nlttosql_display.py` or `nlttosql.py`
2. Change the `model` parameter in ChatOpenAI initialization
3. Available OpenRouter models: https://openrouter.ai/models

### Temperature
Adjust the `temperature` parameter (0-1) for more/less creative responses:
- `temperature=0`: Deterministic (recommended for SQL)
- `temperature=1`: More creative/random

## Troubleshooting

### Issue: "OPENROUTER_API_KEY not found"
- Create `.env` file with your API key
- Restart the application

### Issue: "No module named X"
- Run `pip install -r requirements.txt` again
- Check Python version (3.8+)

### Issue: Database file not found
- Run `python sqldata.py` to create the database
- Ensure `bollywood_movie.csv` is in the project directory

### Issue: SQL query not generated
- Check API key is valid
- Ensure OpenRouter service is working
- Try rephrasing your question more clearly

## Dependencies

- **pandas**: Data manipulation and SQL operations
- **python-dotenv**: Environment variable management
- **streamlit**: Web app framework
- **langchain**: LLM orchestration
- **langchain-openai**: OpenAI API integration
- **openai**: OpenAI client library
- **sqlite3**: Database (built-in)

## File Descriptions

| File | Purpose |
|------|---------|
| `main.py` | Configuration test and entry point |
| `sqldata.py` | Loads CSV and creates SQLite database |
| `nlttosql.py` | CLI tool for NL to SQL conversion |
| `nlttosql_display.py` | Streamlit web application |
| `view_data.sql` | Sample SQL queries for verification |
| `bollywood_movie.csv` | Source dataset |
| `requirements.txt` | Python package dependencies |
| `.env` | API keys and credentials (not in repo) |

## Notes

- The app requires an active internet connection for OpenRouter API calls
- OpenRouter may have usage limits on free tier
- Database is created locally and doesn't require external storage
- SQL queries are generated automatically - verify complex results

## Support

For issues with:
- **OpenRouter**: Visit https://openrouter.ai/
- **Streamlit**: Visit https://docs.streamlit.io/
- **LangChain**: Visit https://python.langchain.com/

## License

This project is open source and available under the MIT License.

## Version

- Version: 1.0.0
- Last Updated: January 2026
