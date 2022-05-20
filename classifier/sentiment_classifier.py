
from torch import nn
import torch

from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification

#NEED TO DISTINGUISH BETWEEk TRAIN AND PREDICT

# TRAIN AND SAVE


class SentimentClassifier(nn.Module):
    def __init__(self, n_classes):
        super(SentimentClassifier, self).__init__()
        self.model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased", num_labels=2)
        self.model.load_state_dict(torch.load('./classifier/sentmodel', map_location=torch.device('cpu')))


    def forward(self, input_ids, attention_mask):
        output = self.model(input_ids=input_ids, attention_mask=attention_mask)
        return output
