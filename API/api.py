from fastapi import FastAPI, UploadFile, File, HTTPException
import pandas as pd
from math import ceil, floor
from io import StringIO

app = FastAPI()

def adjustment(baseline, actual, current, weight):
    ans = 0
    if actual == baseline:
        return int(current)
    if actual > baseline:
        den = ceil(actual / 100)
        den2 = baseline / 100
        ans = current - abs(den - den2) * weight
    elif actual < baseline:
        den = floor(actual / 100)
        den2 = baseline / 100
        ans = current + abs(den - den2) * weight
    return max(5, int(ans))  # Ensure frequency doesn't go below a minimum threshold and is integer

@app.post("/adjust-frequencies/")
async def adjust_frequencies(file: UploadFile = File(...)):
    if file.content_type != 'text/csv':
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    
    # Read the CSV file
    contents = await file.read()
    df = pd.read_csv(StringIO(contents.decode('utf-8')))
    
    if 'No. of Buses' not in df.columns or 'Density' not in df.columns or 'Frequency' not in df.columns:
        raise HTTPException(status_code=400, detail="CSV file must contain 'No. of Buses', 'Density', and 'Frequency' columns.")
    
    baseline_density = df['Density'].mean()

    # Weights for each of the 9 time slots
    weights = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25]

    for i in range(9):
        df[f'Adjusted_Frequency_{i+1}'] = df.apply(lambda row: int(adjustment(baseline_density, row['Density'], row['Frequency'], weights[i])), axis=1)
        df[f'Bus_Requirement_{i+1}'] = df[f'Adjusted_Frequency_{i+1}'] * df['No. of Buses']

    # Return the adjusted DataFrame as a CSV string
    adjusted_csv = df.to_csv(index=False)
    return {"filename": file.filename, "adjusted_data": adjusted_csv}
