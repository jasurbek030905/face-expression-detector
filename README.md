# 🎭 Face Expression Detector

A full-stack web application that detects human emotions in real time using a webcam and AI.

---

## 🚀 Live

- Frontend: https://vercel.com/jasurbek030905s-projects/face-expression-frontend  
- Backend: [https://your-backend.onrender.com](https://face-expression-backend-2.onrender.com/)  

---

## 🧠 Features

- Real-time webcam emotion detection
- AI-powered backend (FER)
- FastAPI + React integration
- Fully deployed (Vercel + Render)

---

## 🛠️ Tech Stack

- **Frontend:** React (Vite)
- **Backend:** FastAPI, Python
- **AI:** FER, OpenCV
- **Deployment:** Vercel, Render

---

## ⚙️ How It Works

1. Camera captures frames
2. Frames are sent to backend
3. AI detects emotion
4. Result is shown instantly

---

## 💻 Run Locally

### Backend
```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
