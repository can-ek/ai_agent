Create a virtual environment at the top level of your project directory:

```
python3 -m venv venv
```

Activate the virtual environment:

```
source venv/bin/activate
```

Install the requirements from requirements.txt

```
pip install -r requirements.txt
```

Copy the API key, then paste it into a new .env file in your project directory. The file should look like this:

```
GEMINI_API_KEY="your_api_key_here"
```

Add the .env file to your .gitignore
