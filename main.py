import os

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from google import genai

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import create_learning_path


load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-3.5-flash-lite"

client = genai.Client(api_key=API_KEY) if API_KEY else None

app = FastAPI(
    title="EduGenie AI",
    description="AI Powered Personal Learning Assistant",
    version="1.0.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


class PromptRequest(BaseModel):
    prompt: str


class ExplainRequest(BaseModel):
    topic: str
    level: str = "Beginner"


class QuizRequest(BaseModel):
    topic: str
    number_of_questions: int = 5
    difficulty: str = "Medium"


class SummaryRequest(BaseModel):
    text: str


class LearningRequest(BaseModel):
    topic: str
    level: str = "Beginner"
    duration: str = "4 weeks"


def check_client():
    if client is None:
        raise HTTPException(
            status_code=500,
            detail="Gemini API key is not configured."
        )


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/health")
async def health():
    return {
        "status": "ok",
        "gemini_configured": bool(API_KEY),
        "model": MODEL
    }


@app.post("/qa")
async def qa(request: PromptRequest):

    if not request.prompt.strip():
        raise HTTPException(
            status_code=400,
            detail="Question cannot be empty."
        )

    check_client()

    try:
        result = answer_question(
            client,
            MODEL,
            request.prompt
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/explain")
async def explain(request: ExplainRequest):

    if not request.topic.strip():
        raise HTTPException(
            status_code=400,
            detail="Topic cannot be empty."
        )

    check_client()

    try:
        result = explain_topic(
            client,
            MODEL,
            request.topic,
            request.level
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/quiz")
async def quiz(request: QuizRequest):

    if not request.topic.strip():
        raise HTTPException(
            status_code=400,
            detail="Quiz topic cannot be empty."
        )

    check_client()

    try:
        result = generate_quiz(
            client,
            MODEL,
            request.topic,
            request.number_of_questions,
            request.difficulty
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/summarize")
async def summarize(request: SummaryRequest):

    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty."
        )

    check_client()

    try:
        result = summarize_text(
            client,
            MODEL,
            request.text
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/learn/recommendations")
async def learning_path(request: LearningRequest):

    if not request.topic.strip():
        raise HTTPException(
            status_code=400,
            detail="Learning topic cannot be empty."
        )

    check_client()

    try:
        result = create_learning_path(
            client,
            MODEL,
            request.topic,
            request.level,
            request.duration
        )

        return {
            "success": True,
            "result": result
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )