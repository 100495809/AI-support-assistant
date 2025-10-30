from utils import load_messages
from classifier import classify_message
from display import display_results
from sentiment import analyze_sentiment


def main():
    df = load_messages("data/messages.csv")
    df["category"] = df["message"].apply(classify_message)
    df["sentiment"] = df["message"].apply(analyze_sentiment)
    display_results(df)


if __name__ == "__main__":
    main()
