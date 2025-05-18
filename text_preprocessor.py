#!/usr/bin/env python
# coding: utf-8

# In[4]:


import string

class TextPreprocessor:
    def __init__(self, lowercase=True, remove_punct=True, remove_stopwords=True):
        self.lowercase = lowercase
        self.remove_punct = remove_punct
        self.remove_stopwords = remove_stopwords

        # You can replace this with a more advanced list if needed
        self.stopwords = {"the", "is", "a", "an", "and", "this", "that", "it", "to", "of", "in"}

    def transform(self, text):
        if self.lowercase:
            text = text.lower()

        if self.remove_punct:
            text = text.translate(str.maketrans("", "", string.punctuation))

        if self.remove_stopwords:
            words = text.split()
            words = [word for word in words if word not in self.stopwords]
            text = " ".join(words)

        return text

