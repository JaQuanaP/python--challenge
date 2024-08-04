# Import necessary libraries
import csv  # For reading CSV files
import os   # For file path operations
from typing import Dict, List, Tuple  # For type hinting
 
# Define the main function to analyze financial data
def analyze_finances(file_path: str) -> Dict[str, any]:
    """
    Analyzes financial data from a CSV file and returns a dictionary of results.
 
    :param file_path: Path to the CSV file containing financial data
    :return: Dictionary containing financial analysis results
    """
    # Initialize variables to store financial data
    months: List[str] = []
    profit_losses: List[int] = []
 
    # Read data from CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            months.append(row[0])  # Store the date
            profit_losses.append(int(row[1]))  # Store the profit/loss as an integer
 
    # Calculate total number of months
    total_months: int = len(months)
 
    # Calculate net total amount of Profit/Losses
    net_total: int = sum(profit_losses)
 
    # Calculate changes in Profit/Losses
    changes: List[int] = [profit_losses[i+1] - profit_losses[i] for i in range(len(profit_losses)-1)]
 
    # Calculate average change
    average_change: float = sum(changes) / len(changes)
 
    # Find greatest increase in profits
    max_increase: Tuple[str, int] = max(zip(months[1:], changes), key=lambda x: x[1])
 
    # Find greatest decrease in profits
    max_decrease: Tuple[str, int] = min(zip(months[1:], changes), key=lambda x: x[1])
 
    # Return results as a dictionary
    return {
        "Total Months": total_months,
        "Net Total": net_total,
        "Average Change": average_change,
        "Greatest Increase": max_increase,
        "Greatest Decrease": max_decrease
    }
 
# Function to format and display results
def display_results(results: Dict[str, any]) -> str:
    """
    Formats the financial analysis results into a string for display.
 
    :param results: Dictionary containing financial analysis results
    :return: Formatted string of results
    """
    output = f"""
Financial Analysis
----------------------------
Total Months: {results['Total Months']}
Total: ${results['Net Total']}
Average Change: ${results['Average Change']:.2f}
Greatest Increase in Profits: {results['Greatest Increase'][0]} (${results['Greatest Increase'][1]})
Greatest Decrease in Profits: {results['Greatest Decrease'][0]} (${results['Greatest Decrease'][1]})
"""
    return output
 
# Main execution block
if __name__ == "__main__":
    # Set file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "Resources", "budget_data.csv")
    output_file = os.path.join(current_dir, "analysis", "financial_analysis.txt")
 
    # Ensure the analysis directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
 
    # Analyze the financial data
    results = analyze_finances(input_file)
 
    # Format the results
    formatted_results = display_results(results)
 
    # Print results to console
    print(formatted_results)
 
    # Save results to file
    with open(output_file, "w") as f:
        f.write(formatted_results)
 
    print(f"Results have been saved to {output_file}")