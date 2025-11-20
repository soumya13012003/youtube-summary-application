
# YouTube Study Video → One-Glance Revision Notes
This project converts a YouTube (or other) study video into a concise, exam-ready summary.
It includes:
- Frontend (HTML/CSS/JS)
- Backend (Flask) skeleton that downloads audio, transcribes (Whisper), and summarizes (OpenAI GPT)
- Example images illustrating Overfitting and Underfitting included in `/static/images/`

## Quick start (development)
1. Create and activate a Python virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate    # Windows
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Set your OpenAI API key as an environment variable (if using GPT summarization):
   ```
   export OPENAI_API_KEY="your_api_key"    # Linux/macOS
   set OPENAI_API_KEY="your_api_key"       # Windows (cmd)
   ```
4. Run the Flask app:
   ```
   python app.py
   ```
5. Open your browser at http://127.0.0.1:5000

## Notes
- This repository provides a fully working skeleton. You'll need to install the speech-to-text model (e.g., Whisper/faster-whisper) separately.
- For production deployment, follow a hosting guide (Heroku, Render, or similar) and secure your API keys.
- Example images included in `/static/images/` were generated earlier and copied from the workspace file paths:
  - /mnt/data/A_2D_Cartesian_coordinate_system_graph_in_the_imag.png
  - /mnt/data/A_two-dimensional_digital_graph_illustrates_underf.png

## Project Structure
- app.py                     : Flask entrypoint
- summarize.py               : helper functions (download audio, transcribe, summarize)
- requirements.txt           : Python packages
- templates/index.html       : Frontend UI
- static/css/style.css       : Styles
- static/js/main.js          : Frontend logic
- static/images/*            : Example images (overfitting & underfitting)
- README.md
