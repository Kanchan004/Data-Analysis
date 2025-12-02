import pandas as pd
df = pd.read_csv(r"D:\Basic_tasks_DA\First_task\global_freelancer_raw.csv")
print(df.head())

print("\n***dataset info***")
print(df.info())

print("\n***missing values***")
print(df.isnull().sum())

#remove missing rows
df = df.dropna()

print("\n***missing values after cleaning***")
print(df.isnull().sum())

#remove duplicate rows
df = df.drop_duplicates()

print("\n***after removing duplicates***")
print(df.shape)
#standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n***Cleaned Columns***")
print(df.columns)
#standardizing gender column
df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].replace({'m':'male', 'male':'male', 'f': 'female', 'female': 'female'})
#standardizing hourly_rate column
df['hourly_rate'] = (
    df['hourly_rate']
    .astype(str)
    .str.replace('usd', '', case=False)
    .str.replace('$', '', regex=False)
    .str.replace(' ', '')
)

df['hourly_rate'] = pd.to_numeric(df['hourly_rate'], errors='coerce')
#standardizing is_active column
df['is_active'] = df['is_active'].astype(str).str.lower()

df['is_active'] = df['is_active'].replace({
    '1': True,
    '0': False,
    'true': True,
    'false': False,
    'yes': True,
    'y': True,
    'n': False
})

df['is_active'] = df['is_active'].astype(bool)

#standardizing client_satisfaction column
df['client_satisfaction'] = (
    df['client_satisfaction']
    .astype(str)
    .str.replace('%', '')
)

df['client_satisfaction'] = pd.to_numeric(df['client_satisfaction'], errors='coerce')

df.to_csv("D:/Basic_Tasks_DA/First_task/global_freelancer_cleaned.csv", index=False)
print("Task one completed successfully!")