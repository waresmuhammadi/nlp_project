# nlp_project

A Django-based NLP toolkit for coursework that combines NLTK, spaCy and TextBlob to provide tokenization, sampling, semantic analysis and related NLP utilities.

## Features
- Tokenization (sentence / word)
- Sampling and data preprocessing utilities
- Part-of-speech tagging and lemmatization
- Named Entity Recognition (spaCy)
- Sentiment analysis and simple semantic features (TextBlob)
- Django views / APIs to expose processing endpoints

## Prerequisites
- Python 3.8+ (3.10 or 3.13 recommended)
- pip
- virtualenv or venv or Anaconda
- Git (optional)

## Installation (step-by-step)

1. Clone the repo (or copy project files)
```
git clone <repo-url> nlp_project
cd nlp_project
```

2. Create and activate a virtual environment
- macOS / Linux:
```
python3 -m venv .venv
source .venv/bin/activate
```
- Windows (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

3. Upgrade pip and install project dependencies
```
pip install --upgrade pip
pip install -r requirements.txt
```
If you don't have a requirements.txt, install the common libs:
```
pip install Django nltk spacy textblob
```

4. Install spaCy language model
```
python -m spacy download en_core_web_sm
```

5. Download NLTK and TextBlob corpora
Run in Python shell or a one-liner:
```
python - <<'PY'
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('stopwords')
from textblob import download_corpora
download_corpora.download_all()
PY
```
Alternatively, run `python -m textblob.download_corpora` for TextBlob.

6. Apply Django migrations and create a superuser
```
python manage.py migrate
python manage.py createsuperuser
```

7. Run the development server
```
python manage.py runserver
```
Open http://127.0.0.1:8000/ http://localhost:8000 / http://<LOCAL IP>:8000 (or the configured endpoints) to use the app.

## Usage notes
- The project contains Django apps that expose NLP endpoints (e.g., /api/tokenize, /api/semantic). See the app README or views for exact routes.
- For performance in production, use compiled spaCy models and consider async/background tasks for heavy processing.

## Project layout (typical)
- manage.py
- requirements.txt
- nlp_project/ (Django project)
- apps/nlp/ (NLP app: views, serializers, utilities)
- notebooks/ (examples and experiments)

## Adding new NLP features
- Add processing functions under apps/nlp/utils.py
- Expose via Django REST views in apps/nlp/views.py
- Add tests under apps/nlp/tests.py

## Troubleshooting
- If spaCy model import fails: ensure `en_core_web_sm` is installed and your venv is active.
- If NLTK / TextBlob data missing: rerun the download commands above.

## License
Add your project license and contribution guidelines as appropriate.

If you want, I can generate a sample requirements.txt and example endpoints for tokenization and sentiment. 
