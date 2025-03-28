import openai
import difflib
import os

# Set your OpenAI API key
openai.api_key = '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'


def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
        return transcript['text']


def check_pronunciation(transcribed_text, expected_text):
    expected_words = expected_text.lower().split()
    spoken_words = transcribed_text.lower().split()

    incorrect_words = []
    for spoken_word in spoken_words:
        if spoken_word not in expected_words:
            closest_match = difflib.get_close_matches(spoken_word, expected_words, n=1)
            if closest_match:
                incorrect_words.append((spoken_word, closest_match[0]))
            else:
                incorrect_words.append((spoken_word, "(No close match)"))

    return incorrect_words


def main(audio_file_path, expected_text):
    print("Transcribing audio...")
    transcribed_text = transcribe_audio(audio_file_path)
    print("Transcribed Text:", transcribed_text)

    incorrect_words = check_pronunciation(transcribed_text, expected_text)

    if incorrect_words:
        print("\nPronunciation Feedback:")
        for incorrect, suggestion in incorrect_words:
            print(f"Incorrect: '{incorrect}' | Suggested: '{suggestion}'")
    else:
        print("Great pronunciation! No mistakes found.")


if __name__ == "__main__":
    audio_path = input("Enter the path to the audio file: ")
    expected_sentence = input("Enter the expected sentence: ")
    main(audio_path, expected_sentence)
