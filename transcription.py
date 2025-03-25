import requests
import time

def transcribe_audio(audio_path):
    """Transcribes audio using AssemblyAI and returns transcript and speaker data."""
    api_key = "524b82447c6e478abcfd70fb7b00900f"
    headers = {"authorization": api_key}
    
    # Upload audio
    upload_url = "https://api.assemblyai.com/v2/upload"
    with open(audio_path, "rb") as audio_file:
        response = requests.post(upload_url, headers=headers, files={"file": audio_file})
    if response.status_code != 200:
        return "", "Error in uploading audio"
    audio_url = response.json()["upload_url"]
    
    # Request transcription
    transcript_url = "https://api.assemblyai.com/v2/transcript"
    data = {"audio_url": audio_url, "speaker_labels": True}
    response = requests.post(transcript_url, headers={**headers, "content-type": "application/json"}, json=data)
    if response.status_code != 200:
        return "", "Error in requesting transcription"
    transcript_id = response.json()["id"]
    
    # Polling for completion
    while True:
        response = requests.get(f"{transcript_url}/{transcript_id}", headers=headers)
        data = response.json()
        if data["status"] == "completed":
            break
        elif data["status"] == "failed":
            return "", "Transcription failed"
        time.sleep(5)
    
    transcript = "\n".join(f"Speaker {u['speaker']}: {u['text']}" for u in data["utterances"])
    return transcript, data
