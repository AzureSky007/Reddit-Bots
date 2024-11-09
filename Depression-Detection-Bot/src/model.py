from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

model_name = "mental/mental-bert-base-uncased"
model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

def detect_depression(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    label = torch.argmax(probs, dim=1).item()
    return label == 1  # Assuming label 1 indicates "depression"
