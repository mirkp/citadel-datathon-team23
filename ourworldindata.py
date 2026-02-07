import pandas as pd
import matplotlib.pyplot as plt

# 1. Define the file path
file_path = 'figure1.xlsx'

# 2. Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)
    print("DataFrame successfully loaded:")
    print(df.head())
    # --- 2. Read the Excel file using pandas ---


    print("\nDataFrame loaded successfully:")
    print(df.head())

    # --- 3. Generate a line graph using matplotlib/pandas plotting capabilities ---
    plt.figure(figsize=(10, 6))

    # Plot the 'Value' column against the 'Date' column
    # plt.plot(df['Earliest publication year'], df['Patent families'], df['Scientfic publications'],marker='o', linestyle='-', color='b')
    df.plot(x='Earliest publication year', y=['Patent families', 'Scientfic publications'], marker='o', linestyle='-', color=['blue', 'orange'])
    # Add titles and labels
    plt.title('Time Series Line Graph')
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

# # 3. Process data and generate a graph
# # This example assumes your Excel file has 'Category' and 'Sales' columns
# if 'Category' in df.columns and 'Sales' in df.columns:
#     # Group by category and sum sales for plotting
#     category_sales = df.groupby('Category')['Sales'].sum()

#     # Create a bar plot using pandas' built-in plotting functionality (which uses matplotlib internally)
#     category_sales.plot(kind='bar', color='skyblue')

#     # Customize the plot
#     plt.title('Total Sales by Category')
#     plt.xlabel('Category')
#     plt.ylabel('Total Sales')
#     plt.xticks(rotation=45, ha='right') # Rotate x-axis labels for better readability
#     plt.tight_layout() # Adjust layout to prevent labels from being cut off

#     # 4. Display the graph
#     plt.show()

# else:
#     print("DataFrame must contain 'Category' and 'Sales' columns for this example.")

