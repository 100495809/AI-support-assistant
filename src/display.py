def display_results(df):
    """Classification results and category counter"""

    print("\n#### Classification Results ####")
    print(df[["message", "category", "sentiment"]].to_string(index=False))
    print("\n#### Category Counts ####")
    print(df["category"].value_counts().to_string())
