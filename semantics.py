from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


print("🧠 Loading local semantic model...")

model = SentenceTransformer("all-MiniLM-L6-v2")


def find_similar_sentences(sentences, threshold=0.65):
    """
    Finds sentences that have similar meanings,
    even when they use different words.
    """

    if len(sentences) < 2:
        return []

    embeddings = model.encode(sentences)

    similarity_matrix = cosine_similarity(embeddings)

    similar_pairs = []

    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):

            similarity = similarity_matrix[i][j]

            if similarity >= threshold:
                similar_pairs.append({
                    "sentence_1": sentences[i],
                    "sentence_2": sentences[j],
                    "similarity": float(similarity)
                })

    return similar_pairs


if __name__ == "__main__":

    test_sentences = [
        "I want to start exercising again.",
        "I really need to get back into working out.",
        "I had pasta for dinner.",
        "Tomorrow I am going to exercise."
    ]

    pairs = find_similar_sentences(test_sentences)

    print("\n🔁 Semantically similar statements:\n")

    for pair in pairs:
        print(
            f"Similarity: {pair['similarity']:.2f}\n"
            f"  → {pair['sentence_1']}\n"
            f"  → {pair['sentence_2']}\n"
        )
