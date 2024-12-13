from fastapi import FastAPI
from pydantic import BaseModel
from googletrans import Translator  # Make sure you have installed googletrans

# Initialize FastAPI app
app = FastAPI()

# Create a Pydantic model for the input data
class TranslationRequest(BaseModel):
    text: str
    target_language: str

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the Translation API!"}

# Translation endpoint
@app.post("/translate/")
def translate(request: TranslationRequest):
    # Initialize the translator
    translator = Translator()
    
    # Translate the text
    translated = translator.translate(request.text, dest=request.target_language)
    
    # Return the translated text
    return {"original_text": request.text, "translated_text": translated.text, "target_language": request.target_language}
