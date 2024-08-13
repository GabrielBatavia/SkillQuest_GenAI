from datasets import load_dataset
import pandas as pd

# Load the dataset
ds = load_dataset("koutch/stackoverflow_python")

# Convert the dataset to a pandas DataFrame
df = pd.DataFrame(ds['train'])

# Save the DataFrame to a CSV file
csv_filename = "stackoverflow_python.csv"
df.to_csv(csv_filename, index=False)

print(f"Dataset has been saved as {csv_filename}.")
