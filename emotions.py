from transformers import pipeline


print("❤️ Loading local emotion model...")

emotion_model = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)


def analyze_emotion(text):
    results = emotion_model(text)

    emotions = sorted(
        results[0],
        key=lambda x: x["score"],
        reverse=True
    )

    return emotions


if __name__ == "__main__":
    test_text = "I finally went for a walk and felt much calmer afterward."

    emotions = analyze_emotion(test_text)

    print("\nDetected emotions:")

    for emotion in emotions[:5]:
        print(
            f"{emotion['label']}: "
            f"{emotion['score']:.2f}"
        )
