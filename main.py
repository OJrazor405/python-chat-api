import openai
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
from dotenv import load_dotenv
import uvicorn

# Load environment variables from .env file
load_dotenv()
# Load environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/python/prompt")
async def generate_text(request_body: PromptRequest):
    try:
        # Assuming the new approach requires direct use of the `openai` object
        # The actual method to call could differ; check the library documentation
        response = openai.chat.completions.create(
            model="gpt-4",  # Or the specific model you intend to use
            messages=[{"role": "user",
                      "content":request_body.prompt,}],
            temperature=0.7,
            max_tokens=150
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"answer": response.choices[0].message.content}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)