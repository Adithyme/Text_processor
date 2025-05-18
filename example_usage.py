#!/usr/bin/env python
# coding: utf-8

# In[2]:


from text_preprocessor import TextPreprocessor

text = "This is Adi’s first ML project!!!"

p = TextPreprocessor(lowercase=True, remove_punct=True, remove_stopwords=True)
cleaned = p.transform(text)

print("Cleaned:", cleaned)

