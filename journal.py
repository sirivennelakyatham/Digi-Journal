from datetime import datetime
from pathlib import Path


JOURNAL_FOLDER = Path("journal")


def save_entry(transcription):
    JOURNAL_FOLDER.mkdir(exist_ok=True)

    today = datetime.now().strftime("%Y-%m-%d")
    filename = JOURNAL_FOLDER / f"{today}.md"

    time = datetime.now().strftime("%H:%M")

    entry = f"""
## Voice Journal — {time}

{transcription.strip()}

"""

    with open(filename, "a", encoding="utf-8") as file:
        file.write(entry)

    print(f"📝 Journal entry saved to {filename}")
