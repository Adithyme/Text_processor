# TextPreprocessor

A simple, class-based text cleaning utility built like a scikit-learn transformer.  
It performs lowercase conversion, punctuation removal, and stopword filtering — useful in NLP and ML pipelines.

---

## Features

- Lowercases text  
- Removes punctuation  
- Removes stopwords  
- Configurable through init arguments  
- .transform() method just like sklearn’s preprocessors

---

## Installation

Just clone the repo and use it in your project — no external dependencies except Python standard libraries.

---

## Usage

example_usage.py:

```python
from text_preprocessor import TextPreprocessor

sample = "This is Adi’s first ML project!!!"

p = TextPreprocessor(lowercase=True, remove_punct=True, remove_stopwords=True)
cleaned = p.transform(sample)

print("Cleaned:", cleaned)


