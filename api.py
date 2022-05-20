from typing import List

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from classifier.model import Model, get_model

app = FastAPI()


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
	sentiment: int
	probabilities: List[float]



@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest, model: Model = Depends(get_model)):
    sentiment, probabilities = model.predict(request.text)
    return SentimentResponse(
        sentiment=sentiment, probabilities=probabilities
    )
