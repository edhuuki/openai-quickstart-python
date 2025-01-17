import os
import openai
from flask import Flask, redirect, render_template, request, url_for
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
print(os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")


response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Can you help me understand how to complete the square for ax^2+bx+c=0",
            temperature=0.6,
        )

print("Response: "+str(response))


# @app.route("/", methods=("GET", "POST"))
# def index():
#     if request.method == "POST":
#         animal = request.form["animal"]
#         response = openai.Completion.create(
#             model="text-davinci-002",
#             prompt=generate_prompt(animal),
#             temperature=0.6,
#         )
#         return redirect(url_for("index", result=response.choices[0].text))

#     result = request.args.get("result")
#     return render_template("index.html", result=result)


# def generate_prompt(animal):
#     return """Suggest three names for an animal that is a superhero.

# Animal: Cat
# Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
# Animal: Dog
# Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
# Animal: {}
# Names:""".format(
#         animal.capitalize()
#     )


# Internal math test


