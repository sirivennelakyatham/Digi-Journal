from pathlib import Path
from datetime import datetime, timedelta

from insights import analyze_insights, display_insights


JOURNAL_FOLDER = Path("journal")


def get_last_7_days_entries():
    """Read journal entries from the last 7 days."""

    if not JOURNAL_FOLDER.exists():
        print("📂 No journal folder found.")
        return ""

    today = datetime.now().date()
    start_date = today - timedelta(days=6)

    entries = []

    for file in JOURNAL_FOLDER.glob("*.md"):

        try:
            file_date = datetime.strptime(
                file.stem,
                "%Y-%m-%d"
            ).date()

        except ValueError:
            continue

        if start_date <= file_date <= today:

            text = file.read_text(encoding="utf-8")

            entries.append(
                f"\n--- {file_date} ---\n{text}"
            )

    return "\n".join(entries)


def generate_weekly_reflection():

    print("\n📅 Reading your last 7 days of journaling...")

    journal_text = get_last_7_days_entries()

    if not journal_text.strip():
        print("\nNo journal entries found for the last 7 days.")
        return

    print("\n🧠 Analyzing your journal...\n")

    insights = analyze_insights(journal_text)

    display_insights(insights)


if __name__ == "__main__":
    generate_weekly_reflection()
