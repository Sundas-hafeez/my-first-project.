
# My First Project

Python projects collection:

1. **Currency Rate Checker** (`currency.py`): finds the latest USD to PKR rate using the Groq API.
2. **Semantic Search** (`semantic_search.py`): finds the most similar sentence by meaning using `sentence-transformers`.

## Currency Rate Checker

A Python script that uses the Groq API and web search to find the latest USD to PKR (Pakistani rupee) exchange rate.

## Requirements
- Python 3
- Libraries: `groq`, `python-dotenv`, `sentence-transformers`
- A Groq API key

## Setup
1. Install the libraries: `pip install groq python-dotenv sentence-transformers`
2. Create a `.env` file and add your key: `GROQ_API_KEY=your_key_here`

## Usage
- Currency checker: `python currency.py`
- Semantic search: `python semantic_search.py`

## Note
Never upload your `.env` file or API key to GitHub.