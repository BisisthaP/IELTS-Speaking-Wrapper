
# 🎯 **IELTS Speaking Analyzer**

## 📌 **Project Overview**
The **IELTS Speaking Analyzer** is a web-based application designed to evaluate and analyze IELTS speaking samples. It transcribes audio files, processes the content, and generates comprehensive feedback with band scores, metrics, and improvement suggestions. The project uses:
- **Backend:** FastAPI for efficient server-side processing.
- **Frontend:** HTML + HTMX for a dynamic and responsive UI.
- **Audio Processing:** Python scripts for transcription and analysis.
- **Output:** Detailed band scores, criteria-based feedback, and improvement suggestions.

---

## 🚀 **Features**
### ✅ **Audio Upload & Transcription**
- Users can upload `.mp3`, `.wav`, or `.m4a` audio files.
- The system transcribes the audio using `transcription.py` and processes the content for evaluation.

### ✅ **Automated Band Score Calculation**
- The app provides **overall band scores** and scores for the four IELTS criteria:
    - **Fluency & Coherence**
    - **Lexical Resource**
    - **Grammatical Range & Accuracy**
    - **Pronunciation**

### ✅ **Advanced Speech Analysis**
- Extracts and displays additional metrics:
    - **Speech Rate (WPM)**: Words per minute spoken.
    - **Filler Words Frequency**
    - **Vocabulary Diversity**
    - **Confidence Score**

### ✅ **Detailed Feedback**
- **Suggestions for Improvement:** Actionable feedback based on the analysis.
- **Strengths & Weaknesses:** Key strengths and focus areas for improvement.
- **Recommended Resources:** YouTube links for IELTS Band 8+ speaking tips and strategies.

### ✅ **Dynamic User Interface**
- **Landing Page:** Sleek, scroll-based navigation with a gradient background.
- **Analysis Page:** Displays scores, metrics, and detailed feedback.
- **Responsive Design:** Ensures compatibility across devices.

---

## 🛠️ **Tech Stack**
- **Backend:** FastAPI (Python)
- **Frontend:** HTML5 + CSS + HTMX
- **Audio Processing:** Python scripts for transcription and analysis
- **UI Styling:** CSS with modern gradient and blur effects

---

## 📁 **File Structure**

### **Backend Files**
- `main.py` → Main FastAPI application, handles routing and data processing.
- `transcription.py` → Transcribes the uploaded audio file.
- `processing.py` → Analyzes transcriptions, generates band scores, and provides feedback.

### **Frontend Files**
- `landing.html` → The main landing page with audio upload functionality.
- `output.html` → Displays the results with band scores, metrics, transcript, and feedback.

---

## 🔥 **Installation & Usage**

### **1️⃣ Clone the Repository**
```bash
git clone <your-repository-url>
cd ielts-speaking-analyzer
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate   # Linux & macOS
venv\Scripts\activate       # Windows
```

### **3️⃣ Install Dependencies**
Install the necessary Python packages from `requirements.txt`:
```bash
pip install -r requirements.txt
```

### **4️⃣ Run the Application**
```bash
uvicorn main:app --reload
```
The application will be available at:
```
http://127.0.0.1:8000
```

---

## ⚙️ **API Endpoints**
### **POST /upload**
- Uploads an audio file for processing.
- **Request:** `.mp3`, `.wav`, `.m4a` files.
- **Response:** 
    - Transcription
    - IELTS band scores
    - Additional metrics
    - Improvement suggestions

### **GET /data**
- Fetches the results of the most recent analysis.
- **Response:** JSON containing:
    - Band scores
    - Metrics
    - Feedback

---

## 🎯 **How It Works**

### **1️⃣ User Flow**
1. **Upload Audio:** Users upload their speaking sample on the landing page.
2. **Transcription:** The `transcription.py` script transcribes the audio.
3. **Processing & Analysis:** 
    - The `processing.py` script analyzes the transcript.
    - Generates band scores, metrics, and suggestions.
4. **Result Display:**
    - The **output.html** page displays the final analysis.
    - Includes band scores, metrics, transcript, and actionable feedback.
    - Suggests **YouTube resources** for IELTS Band 8+ improvement.

---

## 📊 **Screenshots**
### **Landing Page**
- Uploads audio files with a clean, gradient-themed UI.

### **Result Page**
- Displays:
    - Overall Band Score
    - Detailed Metrics (WPM, Filler Words, etc.)
    - Transcript and Suggestions
    - YouTube resources for further improvement

---

## 🔥 **Future Enhancements**
- 🌟 **Real-time feedback:** Displaying live feedback while the audio is being analyzed.
- 🤝 **Future Expansion**: Expand support to include IELTS Listening, TOEFL, and other speaking-specific exams.
- 🔍 **More detailed metrics:** Adding metrics like pauses, intonation, and tone variations.
- 🌐 **Multi-language support:** Expanding the system to support other languages.
- 📈 **User History:** Saving and displaying previous results for comparison.

---

## 🤝 **Contributions**
Contributions are welcome! Feel free to submit pull requests or open issues.

---

## 📄 **License**
This project is licensed under the **MIT License**.

---

✅ **Author:** Bisistha Patra
🤝 **Co-Authors:** Ayush Gharat and Niyati Sardana
📧 **Contact:** patrabisistha@gmail.com  
🔗 **GitHub:** https://github.com/BisisthaP 
📄 **Co-Author Git Hub:** https://github.com/ayushgharat234 

---

💡 **If you find this project helpful, give it a ⭐️ and share it with others!**
