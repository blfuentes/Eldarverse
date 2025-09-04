#!/usr/bin/env python3
"""
Main program for Eldarverse project.
"""

import os
import importlib.util

def import_part_module(part_name, part_file):
    """Import a part module by name and file path."""
    part_path = os.path.join(os.path.dirname(__file__), part_name, part_file)
    spec = importlib.util.spec_from_file_location(part_file[:-3], part_path)  # Remove .py extension
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    """Eldarproject september 2025"""
    print("=== Eldarverse - September 2025 Project ===\n")

    # Run all parts
    parts = [
        ("A - Your Name, Your Discount", "solution.py"),
        ("B - Sparse Rankings", "solution.py"),
    ]
    
    for part_name, part_file in parts:
        try:
            print(f"Running {part_name}:")
            part_module = import_part_module(part_name, part_file)
            part_module.execute()
            print("-" * 50)
        except Exception as e:
            print(f"Error running {part_name}: {e}")
            print("-" * 50)


if __name__ == "__main__":
    # This ensures main() only runs when this file is executed directly
    main()