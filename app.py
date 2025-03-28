import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Set up OpenAI API Key
openai.api_key = "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"

@app.route("/transcribe", methods=["POST"])
def transcribe_audio():
    if "audio" not in request.files:
        return jsonify({"error": "No audio file uploaded"}), 400
    
    audio_file = request.files["audio"]
    
    # Transcribe using Whisper
    transcript = openai.Audio.transcribe("whisper-1", audio_file)

    user_text = transcript["text"]

    # Get feedback using GPT-4
    feedback_prompt = f"""
    Analyze the following French sentence for grammar, pronunciation, and vocabulary:
    "{user_text}"
    Provide corrections and suggestions for improvement.
    """
    
    feedback_response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a French language tutor."},
                  {"role": "user", "content": feedback_prompt}]
    )

    feedback = feedback_response["choices"][0]["message"]["content"]

    return jsonify({"transcription": user_text, "feedback": feedback})

@app.route("/exercise", methods=["GET"])
def generate_exercise():
    prompt = """
    Create a French language exercise for a beginner. It should include:
    - A short dialogue in French
    - A fill-in-the-blank exercise
    - A multiple-choice question
    Provide the answer key as well.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a French language tutor."},
                  {"role": "user", "content": prompt}]
    )

    exercise = response["choices"][0]["message"]["content"]

    return jsonify({"exercise": exercise})

if __name__ == "__main__":
    app.run(debug=True)
