import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

files = [
    "trajectory_data.csv",
    "trajectory_data_extended_1.csv",
    "trajectory_data_extended_2.csv",
]

dfs = [pd.read_csv(os.path.join(script_dir, f)) for f in files]
merged = pd.concat(dfs, ignore_index=True)

output_path = os.path.join(script_dir, "trajectory_data_all.csv")
merged.to_csv(output_path, index=False)

print(f"合并完成：共 {len(merged)} 行，已保存至 {output_path}")
for f, df in zip(files, dfs):
    print(f"  {f}: {len(df)} 行")
