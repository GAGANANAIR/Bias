import pandas as pd

# List of CSV files
files = [
    "Ramu5_Gemma2b_caste_bias_verify.csv",
    "Raju5_Gemma2b_caste_bias_verify.csv",
    "Ramesh5_Gemma2b_caste_bias_verify.csv",
    "Rahul_Gemma2b_caste_bias_verify.csv",
    "Suresh5_Gemma2b_caste_bias_verify.csv",
    "Ramu5_Gemma9_caste_bias_verify.csv",
    "Raju5_Gemma9_caste_bias_verify.csv",
    "Ramesh5_Gemma9_caste_bias_verify.csv",
    "Rahul_Gemma9_caste_bias_verify.csv",
    "Suresh5_Gemma9_caste_bias_verify.csv",
    "Ramu5_Llama_caste_bias_verify.csv",
    "Raju5_Llama_caste_bias_verify.csv",
    "Ramesh5_Llama_caste_bias_verify.csv",
    "Rahul_Llama_caste_bias_verify.csv",
    "Suresh5_Llama_caste_bias_verify.csv"
]

# Read all CSV files
dfs = [pd.read_csv(file) for file in files]

# Combine them (no rows removed, no modifications)
combined_df = pd.concat(dfs, ignore_index=True)

# Save the combined CSV
combined_df.to_csv("Combined_caste_bias_verify.csv", index=False)

print("All CSV files combined successfully!")
print(f"Total rows: {len(combined_df)}")