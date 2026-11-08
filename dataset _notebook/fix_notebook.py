import json
notebook_path = "dataset _notebook/Movie_Revenue_Prediction_2.ipynb"
with open(notebook_path, 'r') as f:
    notebook = json.load(f)
if 'metadata' in notebook and 'widgets' in notebook['metadata']:
    del notebook['metadata']['widgets']
    print("Removed widgets key from metadata")
with open(notebook_path, 'w') as f:
    json.dump(notebook, f, indent=1)
print(f"Notebook saved to {notebook_path}")