import pandas as pd

def create_excel(data, file_path):
    # Create a DataFrame from your portfolio data
    df = pd.DataFrame(data)
    print("df" , df)

    # Write the DataFrame to an Excel file
    df.to_excel(file_path, index=False)

# Example usage
portfolio_data = {
    'Project': ['Project A', 'Project B', 'Project C'],
    'Status': ['Completed', 'In Progress', 'Planned'],
    'Budget': [100000, 150000, 80000]
}

create_excel(portfolio_data, "portfolio_report.xlsx")