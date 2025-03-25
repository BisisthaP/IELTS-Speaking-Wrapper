import google.generativeai as genai
import json
from textblob import TextBlob
from collections import Counter

genai.configure(api_key="AIzaSyCpub0vmpxya0Inpho5VHvkl5UX2e_z8vw")

def analyze_transcript(transcript, speaker_data, audio_path):
    """Processes the transcript to extract IELTS and speech metrics, then uses Gemini for feedback."""
    metrics = extract_speech_metrics(transcript)
    ielts_metrics = get_ielts_band_scores(transcript)
    gemini_feedback = get_gemini_feedback(transcript, ielts_metrics, metrics)
    
    return {"ielts_metrics": ielts_metrics, "speech_metrics": metrics, "gemini_feedback": gemini_feedback}

def extract_speech_metrics(transcript):
    """Extracts speech features such as filler words, lexical diversity, sentiment, etc."""
    words = transcript.split()
    unique_words = set(words)
    
    # Calculate speech rate (words per minute)
    # Assuming average speaking time of 2-3 words per second
    speech_rate = len(words) / (len(words) * 0.4 / 60)  # words per minute
    
    # Calculate filler words percentage
    filler_words = {"uh", "um", "like", "you know", "so", "actually", "basically", "right"}
    filler_count = sum(1 for word in words if word.lower() in filler_words)
    filler_percentage = (filler_count / len(words)) * 100 if words else 0
    
    # Calculate vocabulary diversity
    vocabulary_diversity = len(unique_words) / len(words) if words else 0
    
    # Calculate confidence score based on various factors
    # Using a combination of vocabulary diversity and lack of filler words
    confidence_score = (
        (1 - (filler_percentage / 100)) * 0.6 +  # Lower filler words = higher confidence
        (vocabulary_diversity * 0.4)  # Higher vocabulary diversity = higher confidence
    ) * 100  # Convert to percentage
    
    return {
        "speech_rate": speech_rate,
        "filler_words": filler_percentage,
        "vocabulary_diversity": vocabulary_diversity * 10,  # Scale to 0-10
        "confidence_score": confidence_score
    }

def get_ielts_band_scores(transcript):
    """Uses Gemini API to calculate IELTS band scores for Fluency, Grammar, Pronunciation, and Vocabulary."""
    prompt = f"""
    Analyze the following IELTS speaking transcript and provide band scores as a strict JSON output with the following structure:
    
    {{
        "Fluency & Coherence": <score from 1 to 9, rounded to 0.5 or whole number>,
        "Lexical Resource": <score from 1 to 9, rounded to 0.5 or whole number>,
        "Grammatical Range & Accuracy": <score from 1 to 9, rounded to 0.5 or whole number>,
        "Pronunciation": <score from 1 to 9, rounded to 0.5 or whole number>,
        "Final Band Score": <average of the four scores, rounded to 0.5 or whole number>
    }}
    
    Ensure the response is **only** a valid JSON object, with no extra text before or after.
    
    Transcript:
    {transcript}
    """
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    
    if response and response.text:
        try:
            json_start = response.text.find('{')
            json_end = response.text.rfind('}')
            json_str = response.text[json_start:json_end + 1]
            return json.loads(json_str)
        except json.JSONDecodeError:
            return {"error": "Failed to parse response from Gemini"}
    
    return {"error": "No response from Gemini"}

def get_gemini_feedback(transcript, ielts_metrics, speech_metrics):
    """Uses Gemini API to generate detailed feedback based on IELTS metrics."""
    prompt = f"""Based on the following IELTS speaking test transcript and metrics, provide detailed feedback and suggestions for improvement. 
    Format your response in the following sections:

    Focus Area:
    Identify the single most important area that needs improvement based on the metrics and transcript. Be specific and concise.

    Quick Tip:
    Provide one immediate, practical action the candidate can take right now to improve their speaking. This should be a specific technique or exercise.

    Strength:
    Highlight one notable strength demonstrated in the speaking test.

    Next Step:
    Suggest one specific, actionable next step for the candidate's IELTS preparation journey. This should be different from the quick tip and focus on long-term improvement.

    Detailed Analysis:
    Provide a comprehensive analysis of the speaking performance, including:
    - Specific examples from the transcript
    - Areas for improvement
    - Suggestions for practice
    - Tips for IELTS speaking success

    Transcript:
    {transcript}

    Metrics:
    {json.dumps(speech_metrics, indent=2)}
    {json.dumps(ielts_metrics, indent=2)}

    Please ensure each section is distinct and provides unique, valuable information without repetition."""
    model = genai.GenerativeModel("gemini-2.0-flash")
    response = model.generate_content(prompt)
    return response.text if response and response.text else "Error in generating feedback."