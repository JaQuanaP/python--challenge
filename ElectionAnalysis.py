import csv
import os
from typing import Dict, List, Tuple
 
def analyze_election_data(file_path: str) -> Dict[str, any]:
    """
    Analyzes election data from a CSV file and returns a dictionary of results.
 
    :param file_path: Path to the CSV file containing election data
    :return: Dictionary containing election analysis results
    """
    # Initialize variables to store election data
    total_votes: int = 0
    candidates: Dict[str, int] = {}
 
    # Read data from CSV file
    with open(file_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader)  # Skip the header row
        for row in csvreader:
            total_votes += 1
            candidate = row[2]  # Assuming candidate name is in the third column
            candidates[candidate] = candidates.get(candidate, 0) + 1
 
    # Calculate percentage of votes each candidate won
    percentages: Dict[str, float] = {
        candidate: (votes / total_votes) * 100
        for candidate, votes in candidates.items()
    }
 
    # Determine the winner
    winner: str = max(candidates, key=candidates.get)
 
    # Return results as a dictionary
    return {
        "Total Votes": total_votes,
        "Candidates": candidates,
        "Percentages": percentages,
        "Winner": winner
    }
 
def display_results(results: Dict[str, any]) -> str:
    """
    Formats the election analysis results into a string for display.
 
    :param results: Dictionary containing election analysis results
    :return: Formatted string of results
    """
    output = f"""
Election Results
-------------------------
Total Votes: {results['Total Votes']}
-------------------------
"""
    for candidate, votes in results['Candidates'].items():
        percentage = results['Percentages'][candidate]
        output += f"{candidate}: {percentage:.3f}% ({votes})\n"
 
    output += f"""-------------------------
Winner: {results['Winner']}
-------------------------
"""
    return output
 
if __name__ == "__main__":
    # Set file paths
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(current_dir, "Resources", "election_data.csv")
    output_file = os.path.join(current_dir, "analysis", "election_analysis.txt")
 
    # Ensure the analysis directory exists
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
 
    # Analyze the election data
    results = analyze_election_data(input_file)
 
    # Format the results
    formatted_results = display_results(results)
 
    # Print results to console
    print(formatted_results)
 
    # Save results to file
    with open(output_file, "w") as f:
        f.write(formatted_results)
 
    print(f"Results have been saved to {output_file}")