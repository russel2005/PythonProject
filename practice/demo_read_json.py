import json

with open("article.json", "r") as f:
    assert json.load(f) == article
