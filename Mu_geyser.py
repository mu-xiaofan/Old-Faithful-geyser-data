import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv('geyser.csv', delimiter='\t', skiprows=30)
df[['eruptions', 'waiting']] = df['eruptions,waiting'].str.split(',', n=1, expand=True)

df['eruptions'] = pd.to_numeric(df['eruptions'], errors='coerce')
df['waiting'] = pd.to_numeric(df['waiting'], errors='coerce')
df.dropna(subset=['eruptions', 'waiting'], inplace=True)
df['eruptions'] = df['eruptions'].astype(float)
df['waiting'] = df['waiting'].astype(int)
eruptions = df['eruptions'].tolist()
waiting = df['waiting'].tolist()

#outliers
zEruptions = stats.zscore(df['eruptions'])
zWaiting = stats.zscore(df['waiting'])
zThreshold = 1.5
filtered = df[(abs(zEruptions) < zThreshold) & (abs(zWaiting) < zThreshold)]

plt.figure(figsize=(6,4))
#plt.scatter(df['eruptions'], df['waiting'], label='Eruption vs Waiting')
plt.scatter(filtered['eruptions'], filtered['waiting'], label='Eruption vs Waiting')
plt.xlabel('Eruption (Minutes)', fontsize = 12)
plt.ylabel('Waiting (Minutes)', fontsize = 12)
plt.title('Old Faithfal: Scatter Plot of Eruption minutes vs Waiting minutess', fontsize = 12)
plt.legend(fontsize = 12)
plt.show()

