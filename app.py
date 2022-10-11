import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")



prompt = '''
I am given the problem of a finite square well in QM defined as follows
V(x) = -Vo -a<x<a, 0 elsewhere. What base knowledge do I need to solve for boundry conditions?
'''

response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)


print("Response1: "+str(response.choices[0].text))


response = openai.Completion.create(
  model="text-davinci-002",
  prompt=prompt,
  temperature=0,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.5,
  presence_penalty=0.0,
  stop=["You:"]
)

print('Response2: '+str(response.choices[0].text))



# Internal math test


