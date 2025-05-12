from fastapi import FastAPI, Request, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
import shutil
import os
from transcription import transcribe_audio
from processing import analyze_transcript
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount the static directory to serve HTML files
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="static")

# Store results globally for demonstration purposes (can use a DB or session in production)
results = {}

# Route for Landing Page (Pages 1-3)
@app.get("/", response_class=HTMLResponse)
async def landing(request: Request):
    return templates.TemplateResponse("landing.html", {"request": request})

# Route for Uploading Audio and Triggering Processing
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded")
    
    audio_path = f"temp/{file.filename}"
    os.makedirs("temp", exist_ok=True)
    
    try:
        logger.info(f"Starting file upload process for {file.filename}")
        
        # Save the uploaded file
        with open(audio_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info("File saved successfully")
        
        # Transcribe audio
        logger.info("Starting transcription")
        transcript, speaker_data = transcribe_audio(audio_path)
        if not transcript:
            raise HTTPException(status_code=500, detail="Transcription failed")
        logger.info("Transcription completed successfully")
        
        # Analyze transcript
        logger.info("Starting transcript analysis")
        analysis = analyze_transcript(transcript, speaker_data, audio_path)
        logger.info("Analysis completed successfully")
        
        # Store results
        global results
        results = {
            "transcript": transcript,
            "ielts_metrics": analysis["ielts_metrics"],
            "speech_metrics": analysis["speech_metrics"],
            "gemini_feedback": analysis["gemini_feedback"]
        }
        
        # Clean up audio file after processing
        os.remove(audio_path)
        logger.info("Temporary file cleaned up")
        
        # Redirect to results page
        return RedirectResponse(url="/results", status_code=303)
        
    except Exception as e:
        logger.error(f"Error processing file: {str(e)}")
        if os.path.exists(audio_path):
            os.remove(audio_path)
        return JSONResponse({"error": str(e)}, status_code=500)

# Route for Final Results Page (Page 4)
@app.get("/results", response_class=HTMLResponse)
async def results_page(request: Request):
    return templates.TemplateResponse("output.html", {"request": request})

# Route to Serve Processed Data to HTML
@app.get("/data")
async def get_data():
    return JSONResponse(results)

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
