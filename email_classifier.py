from transformers import pipeline

def classify_email(text):
    classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
    
    labels = ["Work", "Personal", "Finance", "Promotions", "Spam", "Urgent", "Social", "Shopping"]
    
    result = classifier(text, labels)
    top_label = result['labels'][0]
    score = result['scores'][0]
    
    return top_label, round(score * 100, 2)

if __name__ == "__main__":
    email_text = input("Enter the email text:\n")
    label, confidence = classify_email(email_text)
    print(f"\nPredicted Category: {label} ({confidence}%)")
