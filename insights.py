from semantic import model
from emotion import analyze_emotion
from sklearn.metrics.pairwise import cosine_similarity
import re


def split_into_sentences(text):
    """Split journal text into individual statements."""

    sentences = re.split(r'(?<=[.!?])\s+', text.strip())

    return [
        sentence.strip()
        for sentence in sentences
        if len(sentence.strip()) > 10
    ]


def get_emotional_signal(sentence):
    """Determine the strongest emotional signal."""

    emotions = analyze_emotion(sentence)

    strongest = emotions[0]

    return {
        "emotion": strongest["label"],
        "score": strongest["score"]
    }


def group_similar_statements(sentences, threshold=0.65):
    """Find statements that appear to describe similar experiences."""

    if len(sentences) < 2:
        return []

    embeddings = model.encode(sentences)

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

            if similarity_matrix[i][j] >= threshold:
                group.append(sentences[j])
                used.add(j)

        if len(group) >= 2:
            groups.append(group)

    return groups


def classify_intentions(sentences):

    intention_phrases = [
        "i want to",
        "i need to",
        "i should",
        "i hope to",
        "i plan to",
        "i'm going to",
        "i am going to",
        "i need",
        "i wish to",
        "i have to"
    ]

    intentions = []

    for sentence in sentences:

        lower = sentence.lower()

        if any(phrase in lower for phrase in intention_phrases):
            intentions.append(sentence)

    return intentions


def classify_behavior_statements(sentences):

    behavior_words = [
        "keep",
        "always",
        "usually",
        "often",
        "again",
        "scroll",
        "procrastinate",
        "avoid",
        "delay",
        "waste",
        "skip",
        "check",
        "watch",
        "sleep",
        "late"
    ]

    behaviors = []

    for sentence in sentences:

        lower = sentence.lower()

        if any(word in lower for word in behavior_words):
            behaviors.append(sentence)

    return behaviors


def analyze_insights(text):

    sentences = split_into_sentences(text)

    if not sentences:
        return {
            "draining": [],
            "energizing": [],
            "intentions": [],
            "behaviors": []
        }

    emotional_sentences = []

    for sentence in sentences:

        emotion = get_emotional_signal(sentence)

        emotional_sentences.append({
            "text": sentence,
            "emotion": emotion["emotion"],
            "score": emotion["score"]
        })

    negative_emotions = {
        "sadness",
        "anger",
        "fear",
        "disgust"
    }

    positive_emotions = {
        "joy",
        "surprise"
    }

    draining = [
        item
        for item in emotional_sentences
        if item["emotion"] in negative_emotions
        and item["score"] >= 0.50
    ]

    energizing = [
        item
        for item in emotional_sentences
        if item["emotion"] in positive_emotions
        and item["score"] >= 0.50
    ]

    intentions = classify_intentions(sentences)

    behaviors = classify_behavior_statements(sentences)

    recurring_groups = group_similar_statements(sentences)

    return {
        "draining": draining,
        "energizing": energizing,
        "intentions": intentions,
        "behaviors": behaviors,
        "recurring_groups": recurring_groups
    }


def display_insights(insights):

    print("\n")
    print("=" * 50)
    print("          WEEKLY JOURNAL REFLECTION")
    print("=" * 50)

    print("\n🔻 WHAT DRAINED YOU")
    print("-" * 30)

    if insights["draining"]:

        for item in insights["draining"]:
            print(
                f"• {item['text']}\n"
                f"  Emotional signal: {item['emotion']} "
                f"({item['score']:.2f})"
            )

    else:
        print("No strong draining signals detected.")

    print("\n⚡ WHAT ENERGIZED YOU")
    print("-" * 30)

    if insights["energizing"]:

        for item in insights["energizing"]:
            print(
                f"• {item['text']}\n"
                f"  Emotional signal: {item['emotion']} "
                f"({item['score']:.2f})"
            )

    else:
        print("No strong energizing signals detected.")

    print("\n🔁 RETURNING INTENTIONS")
    print("-" * 30)

    if insights["intentions"]:

        for intention in insights["intentions"]:
            print(f"• {intention}")

    else:
        print("No clear intentions detected.")

    print("\n🧨 POTENTIAL DESTRUCTIVE PATTERNS")
    print("-" * 30)

    if insights["behaviors"]:

        for behavior in insights["behaviors"]:
            print(f"• {behavior}")

    else:
        print("No obvious recurring behaviors detected.")

    print("\n🔄 SEMANTICALLY RECURRING THEMES")
    print("-" * 30)

    for group in insights.get("recurring_groups", []):

        print("\nPossible recurring theme:")

        for statement in group:
            print(f"  • {statement}")


if __name__ == "__main__":

    sample_text = """
    I kept checking social media instead of starting my assignment.
    I felt overwhelmed by my work and ended up scrolling Instagram.
    I went for a walk and felt much calmer afterward.
    Walking outside helped me clear my head.
    I need to start exercising again.
    I really want to get back into working out.
    I keep telling myself I will exercise tomorrow.
    """

    insights = analyze_insights(sample_text)

    display_insights(insights)
