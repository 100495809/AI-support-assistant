from transformers import pipeline

# Load huggingface sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")


def analyze_sentiment(message: str) -> str:
    """Analyzes sentiment of the message using a hugging face model"""

    if not isinstance(message, str) or not message.strip():
        return "Unknown"

    # Run the model
    # This will look sometheing like: {label: POSITIVE, score: 0.998}
    result = sentiment_pipeline(message)[0]

    # save the label
    label = result["label"]

    if "POSITIVE" in label.upper():
        return "Positive"
    elif "NEGATIVE" in label.upper():
        return "Negative"
    else:
        return "Neutral"
