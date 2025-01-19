import sys
import pandas as pd
import numpy as np

def validate_inputs(file_name, weights, impacts, num_columns):
    # Check if file exists
    try:
        data = pd.read_csv('sample-data.csv')
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        sys.exit(1)

    # Check if the file has the correct structure
    if data.shape[1] < 3:
        print("Error: Input file must contain at least three columns.")
        sys.exit(1)

    if not all(data.iloc[:, 1:].applymap(np.isreal).all()):
        print("Error: From 2nd to last columns, all values must be numeric.")
        sys.exit(1)

    # Validate weights and impacts
    if len(weights) != num_columns or len(impacts) != num_columns:
        print("Error: Number of weights and impacts must match the number of criteria (columns from 2nd to last).")
        sys.exit(1)

    if not all(impact in ['+', '-'] for impact in impacts):
        print("Error: Impacts must be either '+' or '-'.")
        sys.exit(1)

    return data

def topsis(data, weights, impacts):
    
    # Step 1: Normalize the decision matrix
    matrix = data.iloc[:, 1:].values.astype(float)
    norm_matrix = matrix / np.sqrt((matrix ** 2).sum(axis=0))

    # Step 2: Apply weights
    weighted_matrix = norm_matrix * weights

    # Step 3: Determine ideal best and worst
    ideal_best = np.max(weighted_matrix, axis=0) if '+' in impacts else np.min(weighted_matrix, axis=0)
    ideal_worst = np.min(weighted_matrix, axis=0) if '+' in impacts else np.max(weighted_matrix, axis=0)

    for i, impact in enumerate(impacts):
        if impact == '-':
            ideal_best[i], ideal_worst[i] = ideal_worst[i], ideal_best[i]

    # Step 4: Calculate distances from ideal best and worst
    dist_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Calculate TOPSIS score
    scores = dist_worst / (dist_best + dist_worst)

    # Step 6: Rank the alternatives
    ranks = scores.argsort()[::-1] + 1

    return scores, ranks

def main():
    if len(sys.argv) != 5:
        print("Usage: python <program.py> <InputDataFile> <Weights> <Impacts> <ResultFileName>")
        sys.exit(1)

    input_file, weights_str, impacts_str, output_file = sys.argv[1:]

    # Parse weights and impacts
    try:
        weights = np.array([float(w) for w in weights_str.split(',')])
    except ValueError:
        print("Error: Weights must be numeric and comma-separated.")
        sys.exit(1)

    impacts = impacts_str.split(',')

    # Validate inputs
    data = validate_inputs(input_file, weights, impacts, len(data.columns) - 1)

    # Perform TOPSIS
    scores, ranks = topsis(data, weights, impacts)

    # Append scores and ranks to data
    data['Topsis Score'] = scores
    data['Rank'] = ranks

    # Save results
    data.to_csv(output_file, index=False)
    print(f"Results saved to '{output_file}'.")

if __name__ == "__main__":
    main()
