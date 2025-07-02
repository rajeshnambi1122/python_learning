import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = r'c:\Users\nambi\Downloads\Fold-Transactions-2025-06-29_01-53PM\bank_transactions.csv'
df = pd.read_csv(file_path)

# Convert txn_timestamp to datetime
df['txn_timestamp'] = pd.to_datetime(df['txn_timestamp'])

# Top categories by spend
cat_spend = df[df['type'] == 'DEBIT'].groupby('category')['amount'].sum().sort_values(ascending=False)
print("\nTop Spending Categories:")
print(cat_spend.head(10))

# Top merchants by spend
merchant_spend = df[df['type'] == 'DEBIT'].groupby('merchant')['amount'].sum().sort_values(ascending=False)
print("\nTop Merchants:")
print(merchant_spend.head(10))

# Basic info
print("First 5 rows:")
print(df.head())
print("\nColumns:", df.columns.tolist())
print("\nDate range:", df['txn_timestamp'].min(), "to", df['txn_timestamp'].max())

# --- Descriptive Statistics ---
print("\n--- Descriptive Statistics ---")
print("Debits:")
print(df[df['type'] == 'DEBIT']['amount'].describe())
print("\nCredits:")
print(df[df['type'] == 'CREDIT']['amount'].describe())

# Transaction counts
print("\nTransaction counts by type:")
print(df['type'].value_counts())
print("\nTransaction counts by category:")
print(df['category'].value_counts())
print("\nTransaction counts by merchant:")
print(df['merchant'].value_counts().head(10))

# --- Time-based Analysis ---
print("\n--- Time-based Analysis ---")
df['day'] = df['txn_timestamp'].dt.date
df['week'] = df['txn_timestamp'].dt.to_period('W')
daily_spend = df[df['type'] == 'DEBIT'].groupby('day')['amount'].sum()
weekly_spend = df[df['type'] == 'DEBIT'].groupby('week')['amount'].sum()
print("Highest spend day:", daily_spend.idxmax(), daily_spend.max())
print("Lowest spend day:", daily_spend.idxmin(), daily_spend.min())
print("Average daily spend:", daily_spend.mean())
print("Average weekly spend:", weekly_spend.mean())

# --- Outliers ---
print("\n--- Largest Debits ---")
print(df[df['type'] == 'DEBIT'].sort_values('amount', ascending=False).head(5))
print("\n--- Largest Credits ---")
print(df[df['type'] == 'CREDIT'].sort_values('amount', ascending=False).head(5))

# --- Pie Charts ---
plt.figure()
cat_spend.head(10).plot.pie(autopct='%1.1f%%', title='Top 10 Spending Categories (Pie)')
plt.ylabel('')
plt.tight_layout()
plt.show()

plt.figure()
merchant_spend.head(10).plot.pie(autopct='%1.1f%%', title='Top 10 Merchants (Pie)')
plt.ylabel('')
plt.tight_layout()
plt.show()

# --- Cash Flow ---
df['net_flow'] = df['amount'].where(df['type'] == 'CREDIT', -df['amount'])
df['cum_flow'] = df['net_flow'].cumsum()
plt.figure()
plt.plot(df['txn_timestamp'], df['cum_flow'])
plt.title('Cumulative Net Cash Flow')
plt.xlabel('Date')
plt.ylabel('Net Flow')
plt.tight_layout()
plt.show()

# --- Recurring Payments ---
print("\n--- Potential Recurring Merchants ---")
recurring = df[df['type'] == 'DEBIT'].groupby('merchant').filter(lambda x: len(x) > 3)
print(recurring['merchant'].value_counts().head(10))

# Total debits and credits
debits = df[df['type'] == 'DEBIT']['amount'].sum()
credits = df[df['type'] == 'CREDIT']['amount'].sum()
print(f"\nTotal Debits: {debits}")
print(f"Total Credits: {credits}")

# Current balance (last row)
print(f"\nCurrent Balance: {df.iloc[-1]['current_balance']}")

# Monthly spending trend
df['month'] = df['txn_timestamp'].dt.to_period('M')
monthly = df[df['type'] == 'DEBIT'].groupby('month')['amount'].sum()
monthly.plot(kind='bar', title='Monthly Debit Spending')
plt.ylabel('Amount')
plt.tight_layout()
plt.show()

# Optional: Plot balance over time
df_sorted = df.sort_values('txn_timestamp')
plt.figure()
plt.plot(df_sorted['txn_timestamp'], df_sorted['current_balance'])
plt.title('Balance Over Time')
plt.xlabel('Date')
plt.ylabel('Balance')
plt.tight_layout()
plt.show()