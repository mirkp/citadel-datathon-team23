import pandas as pd
import matplotlib.pyplot as plt

# 1. Define the file path
file_path = 'figure1.xlsx'

# 2. Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)
    print("DataFrame successfully loaded:")
    print(df.head())
    # Read the Excel file using pandas


    print("\nDataFrame loaded successfully:")
    print(df.head())

    # Generate a line graph using matplotlib/pandas plotting capabilities 
    plt.figure(figsize=(10, 6))

    # Plot the 'Value' column against the 'Date' column
    # plt.plot(df['Earliest publication year'], df['Patent families'], df['Scientfic publications'],marker='o', linestyle='-', color='b')
    df.plot(x='Earliest publication year', y=['Patent families', 'Scientfic publications'], marker='o', linestyle='-', color=['blue', 'orange'])
    # Add titles and labels
    plt.title('Increase in AI Innovation Over Time (Patents vs Publications')
    plt.xlabel('Earliest publication year')
    plt.ylabel('Patent families and publications')
    plt.grid(True)

    # Optional: Format the x-axis dates for better readability
    plt.xticks(rotation=45)
    plt.tight_layout() # Adjust layout to make room for x-axis labels

    # Display the plot
    plt.grid(True)
    plt.show()
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()