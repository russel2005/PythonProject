import json

with open("article.json", "w") as f:
    json.dump(article, f)

# {
#     "author": "xiaoxu",
#     "publication": "Towards data science",
#     "publish_date": "2021-02-14",
#     "topics": [
#         "data science",
#         "programming"
#     ],
#     "word_count": 128,
#     "is_vip": true
# }
