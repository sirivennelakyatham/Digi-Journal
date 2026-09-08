from semantic import model
from sklearn.metrics.pairwise import cosine_similarity


def create_embeddings(sentences):
    """Convert sentences into semantic representations."""
    return model.encode(sentences)


def find_recurring_themes(sentences, threshold=0.65):
    """
    Groups statements that have similar meanings.
    """

    if len(sentences) < 2:
        return []

    embeddings = create_embeddings(sentences)

    similarity_matrix = cosine_similarity(embeddings)

    groups = []
    used = set()

    for i in range(len(sentences)):

        if i in used:
            continue

        group = [sentences[i]]
        used.add(i)

        for j in range(i + 1, len(sentences)):

            if j in used:
                continue

            similarity = similarity_matrix[i][j]

            if similarity >= threshold:
                group.append(sentences[j])
                used.add(j)

        if len(group) >= 2:
            groups.append(group)

    return groups


def display_themes(groups):

    print("\n🔁 RECURRING THEMES")
    print("=" * 35)

    if not groups:
        print("No strong recurring themes detected.")
        return

    for number, group in enumerate(groups, start=1):

        print(f"\nTheme {number}")
        print("-" * 20)

        for sentence in group:
            print(f"• {sentence}")


if __name__ == "__main__":

    test_sentences = [

        "I kept checking social media instead of starting my assignment.",

        "I felt overwhelmed by my work and ended up scrolling Instagram.",

        "I went for a walk and felt much calmer afterward.",

        "Walking outside helped me clear my head.",

        "I need to start exercising again.",

        "I really want to get back into working out."

    ]

    themes = find_recurring_themes(test_sentences)

    display_themes(themes)
