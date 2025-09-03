"""
Part 01 module - Your Name, Your Discount
"""

import os
import sys

# Add the parent directory (202509-sept) to the path so we can import shared_utils
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the shared utilities directly
import shared_utils
from collections import Counter

def parse_data(filepath):
    """Reads a file and returns its content as a list of lines."""
    data = shared_utils.read_file_to_array(filepath)
    return int(data[0]), data[1:]


def execute():
    """Main execution function for this module."""
    filepath = os.path.join(os.path.dirname(__file__), "problem-sep-25-long-A-input.txt")
    input_size, file_data = parse_data(filepath)
    output_filepath = os.path.join(os.path.dirname(__file__), "problem-sep-25-long-A-output.txt")
    print(f"File data from {filepath}:")
    with open(output_filepath, "w") as output_file:
        for idx in range(0, input_size):
            char_counts = Counter((file_data[idx][0].lower() + file_data[idx][1:]))
            output_file.write(f"Case #{idx+1}: {100 - (len(char_counts) * 5)}\n")


if __name__ == "__main__":
    # This code runs only when the file is executed directly
    print("Running part01.py directly...")
    execute()
