from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences = [
    "I love playing cricket",
    "Football is a popular sport",
    "The cat is sleeping on the sofa",
    "Python is a programming language",
    "I enjoy coding in Python",
    "Kittens are very cute",
    "Machine learning is part of AI",
    "Biryani is my favourite food",
]

sentence_embeddings = model.encode(sentences)

query = "I like to write code"
query_embedding = model.encode(query)

scores = util.cos_sim(query_embedding, sentence_embeddings)[0]

top = scores.argsort(descending=True)[:5]
for i in top:
    print(round(float(scores[i]), 3), "→", sentences[i])

# Output:
# 0.662 → I enjoy coding in Python
# 0.394 → Python is a programming language
# 0.267 → I love playing cricket
# 0.206 → Kittens are very cute
# 0.187 → Machine learning is part of AI