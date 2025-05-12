# IELTS Speaking Analyzer

A web application designed to evaluate and analyze IELTS speaking samples, providing comprehensive feedback and band scores.

## Project Overview

The **IELTS Speaking Analyzer** is a web-based tool built to assess IELTS speaking samples. It transcribes uploaded audio, analyzes the content, and delivers detailed feedback, including band scores, key metrics, and actionable suggestions for improvement.

This project leverages:

* **Backend:** FastAPI for efficient server-side operations.
* **Frontend:** HTML and HTMX for a dynamic and responsive user interface.
* **Audio Processing:** Python scripts for transcribing audio and performing linguistic analysis.
* **Output:** Detailed band scores, feedback based on IELTS criteria, and practical improvement tips.

## Features

* **Audio Upload & Transcription:**
    * Allows users to upload audio files in `.mp3`, `.wav`, or `.m4a` formats.
    * Utilizes the `transcription.py` script to convert audio to text for analysis.
* **Automated Band Score Calculation:**
    * Provides an **overall band score**.
    * Generates individual scores for the four IELTS speaking criteria:
        * Fluency & Coherence
        * Lexical Resource
        * Grammatical Range & Accuracy
        * Pronunciation
* **Advanced Speech Analysis:**
    * Extracts and presents valuable speech metrics:
        * **Speech Rate (WPM):** Measures the number of words spoken per minute.
        * **Filler Words Frequency:** Identifies and quantifies the use of filler words.
        * **Vocabulary Diversity:** Assesses the range and variety of vocabulary used.
        * **Confidence Score:** Provides an indication of the speaker's confidence level (based on linguistic cues).
* **Detailed Feedback:**
    * **Suggestions for Improvement:** Offers actionable advice tailored to the analysis results.
    * **Strengths & Weaknesses:** Highlights key areas of proficiency and areas needing focus.
    * **Recommended Resources:** Includes links to relevant YouTube videos offering IELTS Band 8+ speaking tips and strategies.
* **Dynamic User Interface:**
    * **Landing Page:** Features a clean, scroll-based design with an engaging gradient background.
    * **Analysis Page:** Clearly displays scores, metrics, the transcribed text, and detailed feedback.
    * **Responsive Design:** Ensures optimal viewing and functionality across various devices.

## Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** HTML5, CSS, HTMX
* **Audio Processing:** Python scripts (custom)
* **UI Styling:** CSS with modern gradient and blur effects

## File Structure
ielts-speaking-analyzer/
├── backend/
│   ├── main.py         # Main FastAPI application
│   ├── transcription.py# Audio transcription script
│   └── processing.py   # Analysis, scoring, and feedback generation
├── frontend/
│   ├── landing.html    # Main landing page
│   └── output.html     # Results display page
└── requirements.txt  # Project dependencies

## Installation & Usage

1.  **Clone the Repository:**
    ```bash
    git clone <your-repository-url>
    cd ielts-speaking-analyzer
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux & macOS
    venv\Scripts\activate       # Windows
    ```

3.  **Install Dependencies:**
    Install the necessary Python packages:
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the Application:**
    ```bash
    uvicorn backend.main:app --reload
    ```
    The application will be accessible at `http://127.0.0.1:8000`. Navigate to this address in your web browser.

## API Endpoints

* **`POST /upload`**
    * **Description:** Uploads an audio file for processing.
    * **Request Body:** Accepts `.mp3`, `.wav` files.

* **`GET /data`**
    * **Description:** Fetches the results of the most recent analysis.
    * **Response (JSON):** Contains the same data structure as the `/upload` response.

## How It Works

1.  **User Flow:**
    * **Upload Audio:** Users upload their speaking sample via the landing page.
    * **Transcription:** The `transcription.py` script processes the uploaded audio.
    * **Processing & Analysis:** The `processing.py` script analyzes the transcribed text, calculates band scores and metrics, and generates feedback.
    * **Result Display:** The `output.html` page presents the calculated scores, metrics, the full transcript, and actionable improvement suggestions, including relevant YouTube resources.

## Future Enhancements

* Real-time feedback: Providing live analysis and feedback as the user speaks.
* Future Expansion: Extending support to other language proficiency exams like TOEFL and IELTS Listening.
* More detailed metrics: Incorporating analysis of pauses, intonation patterns, and tone variations.
* Multi-language support: Enabling the system to process and analyze audio in multiple languages.
* User History: Allowing users to save and review their past analysis results for progress tracking.

## Contributions

We welcome contributions to this project! Please feel free to submit pull requests or open issues to discuss potential improvements or report bugs.

## License

This project is licensed under the MIT License. 
## Author & Contributors

* **Author:** Bisistha Patra
* **Co-Authors:** Ayush Gharat, Niyati Sardana

## Contact
patrabisistha@gmail.com

## Links

* **GitHub (Author):** [https://github.com/BisisthaP]
* **GitHub (Co-Author - Ayush Gharat and Niyati Sardana):** [https://github.com/ayushgharat234]

## Show Your Support
If you find this project valuable, please consider giving it a star on GitHub! Thank you!
