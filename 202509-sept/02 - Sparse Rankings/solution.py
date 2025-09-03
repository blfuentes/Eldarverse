"""
Solution module - Sparse Rankings
"""

import os
import sys
import bisect

# Add the parent directory (202509-sept) to the path so we can import shared_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the shared utilities directly
import shared_utils
from collections import Counter

def parse_data(filepath):
    """Reads a file and returns its content as a list of lines."""
    data = shared_utils.read_file_to_array(filepath)
    return int(data[0]), [list(map(int, line.split(" "))) for line in data[1:]]

def calculate_point_differences(T):
    """
    Calculates the point difference between the first and last team
    for every possible win-loss combination using dynamic programming.
    """
    if T < 2:
        return []

    teams = list(range(T))  # Use 0-indexed teams for easier list access
    games = []
    for home_team in teams:
        for away_team in teams:
            if home_team != away_team:
                games.append((home_team, away_team))

    # DP state: dp[points_tuple] = count_of_ways
    # Initialize with zero points for all teams, with 1 way to achieve this (before any games)
    initial_points = tuple([0] * T)
    dp = {initial_points: 1}

    num_games = len(games)
    # Iterate through each game, updating the DP table
    for i, (home_team, away_team) in enumerate(games):
        print(f"    Processing game {i + 1}/{num_games} for T={T}. DP states: {len(dp)}")
        new_dp = Counter()
        for points_tuple, count in dp.items():
            points = list(points_tuple)

            # Case 1: Home team wins
            points[home_team] += 1
            new_dp[tuple(points)] += count
            points[home_team] -= 1  # Backtrack

            # Case 2: Away team wins
            points[away_team] += 1
            new_dp[tuple(points)] += count
            points[away_team] -= 1  # Backtrack
        dp = new_dp

    # After all games, dp holds the final distributions.
    # Now, calculate the differences from the final point distributions.
    differences = []
    for points_tuple, count in dp.items():
        diff = max(points_tuple) - min(points_tuple)
        # Add the difference 'count' times to the results list
        differences.extend([diff] * count)
        
    return differences


def execute():
    """Main execution function for this module."""
    # Pre-calculate differences for T from 2 to 6
    print("Pre-calculating point differences...")
    precalculated_differences = {}
    for T in range(2, 7):
        print(f"  Calculating for {T} teams...")
        differences = calculate_point_differences(T)
        differences.sort()  # Sort the list for binary search
        precalculated_differences[T] = differences
    print("Pre-calculation complete.")

    # filepath = os.path.join(os.path.dirname(__file__), "sample01.txt")
    filepath = os.path.join(os.path.dirname(__file__), "problem-sep-25-long-B-input.txt")
    input_size, file_data = parse_data(filepath)
    output_filepath = os.path.join(os.path.dirname(__file__), "problem-sep-25-long-B-output.txt")
    
    print(f"Processing data from {filepath}...")
    with open(output_filepath, "w") as output_file:
        for idx in range(input_size):
            if (idx + 1) % 1000 == 0:
                print(f"  Processing case {idx + 1}/{input_size}...")
            try:
                # file_data is already a list of [T, min_diff] pairs
                T = file_data[idx][0]
                min_diff = file_data[idx][1]
                
                # Retrieve the pre-calculated, sorted list of differences
                differences = precalculated_differences.get(T, [])
                
                # Use binary search to find the count of numbers greater than min_diff
                count = len(differences) - bisect.bisect_right(differences, min_diff)
                
                output_file.write(f"Case #{idx+1}: {count}\n")

            except (ValueError, IndexError):
                output_file.write(f"Case #{idx+1}: Invalid input\n")
    
    print(f"Output successfully written to {output_filepath}")
    
    # print(f"File data from {filepath}:")
    # with open(output_filepath, "w") as output_file:
    #     for idx in range(0, input_size):
    #         char_counts = Counter((file_data[idx][0].lower() + file_data[idx][1:]))
    #         output_file.write(f"Case #{idx+1}: {100 - (len(char_counts) * 5)}\n")


if __name__ == "__main__":
    # This code runs only when the file is executed directly
    print("Running solution.py directly...")
    execute()
