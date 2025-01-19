# TOPSIS Implementation in Python

This Python package implements the Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS), a multi-criteria decision-making method, in Python. It helps users rank alternatives based on multiple criteria, considering their relative importance and direction of impact.

## Features
- Calculate TOPSIS scores and rank alternatives.
- Accept input data via CSV files.
- Perform comprehensive validation of inputs for error-free execution.

## Installation
To install the package, run the following command:

```bash
pip install TOPSIS-Tanveer-102216133
```

## Usage
To use the package, follow these steps:

1. Prepare a CSV file containing your dataset.
2. Execute the `topsis` command with the following arguments:

```bash
topsis "<InputDataFile.csv>" "<Weights>" "<Impacts>" "<ResultFile.csv>"
```

### Arguments
1. **InputDataFile**: Name of the CSV file containing the dataset (including `.csv` extension).
2. **Weights**: Comma-separated weights for the criteria (e.g., `1,1,1,1`).
3. **Impacts**: Comma-separated signs indicating the direction of impact for each criterion (`+` for beneficial, `-` for non-beneficial).
4. **ResultFile**: Name of the output CSV file to store results (including `.csv` extension).

### Example
Suppose you have a dataset named `102216133-data.csv` and want to assign equal weights (`1,1,1,1`) to all criteria, with impacts as `+,-,+,+`. To save the result in `result-102216133.csv`, run the following command:

```bash
topsis "102216133-data.csv" "1,1,1,1" "+,-,+,+" "result-102216133.csv"
```

## Output
The output file will contain the following columns:
- The original data.
- A new column, **Topsis Score**, which contains the calculated scores.
- A new column, **Rank**, which ranks the alternatives based on their scores (higher scores indicate better alternatives).

## Example Dataset
An example input dataset might look like this:

| Alternative | C1  | C2  | C3 | C4 |
|-------------|------|------|-----|-----|
| A1          | 0.82 | 0.75 | 7.1 | 40.8 |
| A2          | 0.89 | 0.81 | 6.9 | 30.3 |
| A3          | 0.77 | 0.66 | 5.0 | 44.2 |
| A4          | 0.76 | 0.59 | 6.1 | 41.7 |

The output file will append **Topsis Score** and **Rank** to the dataset:

| Alternative | C1  | C2  | C3 | C4  | Topsis Score | Rank |
|-------------|------|------|-----|------|---------------|------|
| A1          | 0.82 | 0.75 | 7.1 | 40.8 | 0.5768        | 3    |
| A2          | 0.89 | 0.81 | 6.9 | 30.3 | 0.5204        | 4    |
| A3          | 0.77 | 0.66 | 5.0 | 44.2 | 0.4499        | 6    |
| A4          | 0.76 | 0.59 | 6.1 | 41.7 | 0.4848        | 5    |

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Developed by Tanveer Singh
