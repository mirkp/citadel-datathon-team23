import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 1. Prepare your data (a 2D dataset or a Pandas DataFrame)
# Example: Using a sample correlation matrix from a DataFrame
# Let's create some dummy data first
import pandas as pd
import matplotlib.pyplot as plt

# 1. Define the file path
file_path = 'heatmap3.xlsx'

# 2. Read the Excel file into a pandas DataFrame
try:
    df = pd.read_excel(file_path)
    print("DataFrame successfully loaded:")
    print(df.head())
    # Read the Excel file using pandas


    print("\nDataFrame loaded successfully:")
    print(df.head())


    # col1=vertical axis
    # col2=horizontal axis
    # col3 color intensity
    print(df.corr())

    #matrix = df 
    # Calculate the correlation matrix

    # matrix=df
    row_labels = [
        "Telecommunications",
        "Transportation",
        "Personal devices, computing and HCI",
        "Life and medical sciences",
        "Security",
        "Document management and publishing",
        "Business",
        "Industry and manufacturing",
        "Physical sciences and engineering",
        "Networks",
        "Arts and humanities",
        "Education",
        "Cartography",
        "Energy management",
        "Entertainment",
        "Computing in government",
        "Banking and finance",
        "Agriculture",
        "Military",
        "Law, social and behavioral sciences"
        ]
    col_labels = [
        "Machine learning",
        "Computer vision",
        "Natural language processing",
        "Speech processing",
        "Control methods",
        "Planning and scheduling",
        "Robotics",
        "Knowledge representation and reasoning",
        "Predictive analytics",
        "Distributed AI"
        ]

    matrix = pd.DataFrame(df.corr(), index=row_labels, columns=col_labels)
    matrix=df
    # 2. Generate the heatmap
    plt.figure(figsize=(10, 20)) # Optional: Adjust the size of the plot

    sns.heatmap(
        matrix,       # The data to plot
        annot=True,        # Optional: Annotate each cell with the numeric value
        cmap='coolwarm',   # Optional: The color map (e.g., 'viridis', 'plasma', 'coolwarm')
        fmt=".0f",         # Optional: String formatting for annotations (2 decimal places)
        linewidths=.5,     # Optional: Space between cells
        cbar=True,         # Optional: Show the color bar
        square=True        # Optional: Ensure square cells
    )

    # 3. Add titles and labels (using matplotlib)
    plt.title('Correlation Heatmap')
    plt.xlabel('column categories')
    plt.ylabel('row categories')

    # 4. Display the plot
    plt.show()

 
except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found.")
    exit()
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

   