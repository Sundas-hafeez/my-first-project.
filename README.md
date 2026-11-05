# Currency Rate Checker

A Python script that uses the Groq API and web search to find the latest USD to PKR (Pakistani rupee) exchange rate.

## Requirements
- Python 3
- Libraries: `groq`, `python-dotenv`
- A Groq API key

## Setup
1. Install the libraries:
   `pip install groq python-dotenv`
2. Create a `.env` file and add your key:
   `GROQ_API_KEY=your_key_here`

## Usage
Run the script:
`python currency.py`

It prints the current rate along with its source.

## Note
Never upload your `.env` file or API key to GitHub.