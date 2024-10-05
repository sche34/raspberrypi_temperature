import pandas as pd
import matplotlib.pyplot as plt

def main(path="data/readings.txt"):
    # load & take the average of a minute
    df = pd.read_csv(path)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    grouped_df = df.resample('60min', on='Timestamp').mean()
    grouped_df.reset_index(inplace=True)

    # grouped_df.sort_values(by='Timestamp', inplace=True)
    grouped_df.plot(x='Timestamp', y='Temperature (°C)', kind='line')
    
    # set labels, title and save plot
    plt.xlabel('Time')
    plt.ylabel('Temperature (°C)')
    plt.title('CPU Temperature Readings')
    plt.savefig('data/temp_readings.png')
    print(f'Plot includes {len(df)} readings from {df["Timestamp"].min()} to {df["Timestamp"].max()}')
    

if __name__ == '__main__':
    main()
