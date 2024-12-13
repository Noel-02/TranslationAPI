from fastapi import FastAPI, HTTPException
from googletrans import Translator

# Create a FastAPI app
app = FastAPI()

# Initialize the translator
translator = Translator()

# Define the translation endpoint
@app.post("/translate/")
async def translate_text(text: str, target_language: str):
    """
    Translate Malayalam text to English and vice versa.
    :param text: Input text.
    :param target_language: 'en' for English, 'ml' for Malayalam.
    :return: Translated text.
    """
    if target_language not in ["en", "ml"]:
        raise HTTPException(status_code=400, detail="Invalid target language. Use 'en' or 'ml'.")

    try:
        translated = translator.translate(text, dest=target_language)
        return {"original_text": text, "translated_text": translated.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Translation failed: {str(e)}")
