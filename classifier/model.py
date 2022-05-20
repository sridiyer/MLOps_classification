import json

import torch
import torch.nn.functional as F

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from .sentiment_classifier import SentimentClassifier

class Model:
    def __init__(self):

        self.device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

        classifier = SentimentClassifier(2)
        classifier = classifier.eval()
        self.classifier = classifier.to(self.device)

    def predict(self, text):
        encoded_text = self.tokenizer.encode_plus(
            text,
            max_length=510,
            add_special_tokens=True,
            return_token_type_ids=False,
            pad_to_max_length=True,
            return_attention_mask=True,
            return_tensors="pt",
        )
        input_ids = encoded_text["input_ids"].to(self.device)
        attention_mask = encoded_text["attention_mask"].to(self.device)

        with torch.no_grad():
            probabilities = F.softmax(self.classifier(input_ids, attention_mask)['logits'], dim=1)
        confidence, predicted_class = torch.max(probabilities, dim=1)
        probabilities = probabilities.flatten().cpu().numpy().tolist()
        return (predicted_class, probabilities)


model = Model()


def get_model():
    return model
