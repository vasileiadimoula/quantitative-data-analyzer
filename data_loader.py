import pandas as pd
def load_data(filename):
    data = pd.read_csv(filename)
    if "value" not in data.columns:
        raise ValueError("CSV file must contain a 'value' column.")
    try:
        data["value"] = pd.to_numeric(data["value"])
    except ValueError:
        raise ValueError("The 'value' column must contain only numbers.")
    numbers = data["value"].tolist()
    if not numbers:
        raise ValueError("CSV file contains no data.")
    return numbers
