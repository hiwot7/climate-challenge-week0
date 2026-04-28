import pandas as pd


def clean_climate_data(filepath):
    """
    Cleans NASA POWER data by handling -999 sentinels and 
    converting Year/DOY to standard datetime objects.
    """

    df = pd.read_csv(filepath)

    df = df.replace(-999, pd.NA)

    # Using format %Y%j (Year + Julian Day)
    df['date'] = pd.to_datetime(
        df['YEAR'].astype(str) + df['DOY'].astype(str).str.zfill(3),
        format='%Y%j'
    )

    df = df.drop(columns=['YEAR', 'DOY'])

    return df


files = {
    "Ethiopia": "data/ethiopia.csv",
    "Kenya": "data/kenya.csv",
    "Sudan": "data/sudan.csv",
    "Nigeria": "data/nigeria.csv",
    "Tanzania": "data/tanzania.csv"
}


dataframes = {}

print("--- Climate Analysis Results ---")

for country, path in files.items():
    try:
        # Process the data
        df = clean_climate_data(path)
        dataframes[country] = df

        avg_temp = df['T2M'].mean()
        print(f"{country}: {avg_temp:.2f}°C")

    except FileNotFoundError:
        print(f"File not found: {path}")


if "Ethiopia" in dataframes and "Kenya" in dataframes:
    eth_temp = dataframes["Ethiopia"]['T2M'].mean()
    ken_temp = dataframes["Kenya"]['T2M'].mean()

    winner = "Ethiopia" if eth_temp < ken_temp else "Kenya"
    print(f"\nResult: {winner} is cooler on average.")
