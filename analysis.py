import pandas as pd

# Load the data for each country
ethiopia = pd.read_csv('ethiopia.csv').replace(-999, pd.NA)
kenya = pd.read_csv('kenya.csv').replace(-999, pd.NA)

# Calculate the average temperature (T2M)
eth_avg_temp = ethiopia['T2M'].mean()
ken_avg_temp = kenya['T2M'].mean()

print(f"Average Temp in Ethiopia: {eth_avg_temp:.2°C}")
print(f"Average Temp in Kenya: {ken_avg_temp:.2°C}")

if eth_avg_temp < ken_avg_temp:
    print("Ethiopia is cooler on average.")
else:
    print("Kenya is cooler on average.")