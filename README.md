# Digi-Journal
Digi-Journal : Offline Voice Journal & Local NLP Reflection

Digi-Journal is a privacy-focused voice journaling system that converts spoken reflections into written journal entries and performs local NLP analysis to identify emotions, recurring themes, intentions, and behavioral patterns.

The project is designed around one core idea:

> **Your personal journal should remain yours.**

Instead of sending journal recordings or text to a cloud AI service, Digi-Journal performs transcription and analysis locally using open-source machine learning models.

-  Features

1.   Voice Recording
Record a short voice journal directly from the computer microphone.

- Local audio recording
- WAV format
- No cloud upload
- Configurable recording duration

2.  Local Speech-to-Text

The recorded audio is transcribed using **Faster-Whisper** running locally.

This converts spoken reflections into text without sending the recording to an external API.

3.  Emotion Detection

The journal text is analyzed using a locally loaded transformer-based emotion classification model.

The system detects emotional signals such as:

- Joy
- Sadness
- Anger
- Fear
- Disgust
- Surprise

4.  Semantic Pattern Detection

Instead of relying only on exact keyword matching, Digi-Journal uses **sentence embeddings** to compare the meaning of different statements.

For example:

> "I need to start exercising again."

and

> "I really want to get back into working out."

can be recognized as semantically similar even though they use different words.

5.  Intention Detection

The system identifies statements that express intentions or plans, such as:

- "I want to..."
- "I need to..."
- "I should..."
- "I plan to..."
- "I'm going to..."

6.  Recurring Theme Detection

Semantically similar statements are grouped together to identify themes that repeatedly appear in journal entries.

7.  Behavioral Pattern Detection

The system also looks for potential recurring behavioral signals such as:

- procrastination
- repeatedly checking social media
- avoiding tasks
- delaying work
- poor sleep patterns
- repeatedly postponing goals

 8. Journal Storage

Journal entries are automatically saved as dated Markdown files.


Project Screenshots : 
1.Recording



<img width="702" height="94" alt="IMG-20260910-WA0006" src="https://github.com/user-attachments/assets/3edaa607-62f6-420a-a6f6-3ed51cade234" />


2. Analysis and Insights


<img width="592" height="467" alt="IMG-20260910-WA0007" src="https://github.com/user-attachments/assets/266922e0-990c-40e5-808f-3b169401e84d" />

<img width="628" height="513" alt="IMG-20260910-WA0008" src="https://github.com/user-attachments/assets/f4805cec-87a4-4b5c-8f40-6207d746de03" />


Digi-Journal is a prototype focused on demonstrating local speech processing and NLP rather than being a production-ready mental health or journaling application.
Current limitations include:
Emotion classification is not a clinical assessment.
Behavioral detection uses heuristic rules.
Semantic grouping depends on similarity thresholds.
Speech recognition quality depends on microphone/audio quality.
The current implementation is primarily command-line based.
Weekly insights are exploratory rather than personalized psychological advice.
The system should therefore be viewed as a personal reflection and NLP demonstration tool, not a diagnostic system.



Future Improvements
Possible future development includes:
Browser-based interface
Journal analytics dashboard
Emotion trends over time
Improved semantic clustering
Searchable journal history
Longer and configurable recordings
Additional local privacy controls
Mobile-friendly interface
More advanced local language models
Integrating claude API ( erases the local and privacy concept) for accurate reading.

Tech Stack : 
Python · Faster-Whisper · Hugging Face Transformers · PyTorch · Sentence Transformers · Scikit-learn · SoundDevice · Git & GitHub
