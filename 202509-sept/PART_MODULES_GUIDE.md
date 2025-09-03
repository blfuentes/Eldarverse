# Part Modules Import Guide

## Super Simple Import Solution

With the refactored `shared_utils.py`, you only need **3 lines of code** in each part file to access all utilities:

```python
import os
import sys

# Add the parent directory (202509-sept) to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all utilities directly
import shared_utils
```

## Creating New Part Modules

### Step 1: Create your folder structure
```
202509-sept/
├── shared_utils.py           # ALL utilities in one file
├── part_template.py          # Template to copy from
├── main.py                   # Runs all parts
├── 01 - Your Name, Your Discount/
│   └── part01.py
├── 02 - Your New Part/       # Just create a new folder
│   └── part02.py             # Copy from template
└── 03 - Another Part/
    └── part03.py
```

### Step 2: Copy the template
1. Copy `part_template.py`
2. Rename it to `part02.py` (or whatever number)
3. Move it to your new folder: `02 - Your New Part/`

### Step 3: Customize your part
```python
"""
Part 02 module - My New Feature
"""

import os
import sys

# Add the parent directory (202509-sept) to the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import all utilities directly
import shared_utils

def my_awesome_function():
    """My new functionality."""
    # Use any function directly:
    price = 99.99
    formatted = shared_utils.format_currency(price)
    tax = shared_utils.calculate_tax(price)
    
    print(f"Price: {formatted}")
    print(f"Tax: {shared_utils.format_currency(tax)}")
    
    # Read files easily:
    data = shared_utils.read_file_to_array("myfile.txt")
    
    # Use calculator:
    calc = shared_utils.Calculator()
    result = calc.add(10, 20)
    multiply_result = calc.multiply(5, 6)

def execute():
    """Main execution function for this module."""
    print("=== Part 02 - My New Feature ===")
    my_awesome_function()

if __name__ == "__main__":
    print("Running part02.py directly...")
    execute()
```

### Step 4: Add to main.py (optional)
If you want your part to run automatically when running `main.py`, just add it to the parts list:

```python
parts = [
    ("01 - Your Name, Your Discount", "part01.py"),
    ("02 - Your New Part", "part02.py"),  # Add this line
]
```

## Available Functions

All these functions are available directly via `shared_utils`:

### File Operations
- `shared_utils.read_file_to_array(filepath)` - Read file into array of lines
- `shared_utils.read_file_to_array_with_strip(filepath)` - Read with whitespace stripped
- `shared_utils.read_file_to_array_no_empty(filepath)` - Read excluding empty lines

### Formatting
- `shared_utils.format_currency(amount)` - Format number as currency ($123.45)
- `shared_utils.validate_percentage(percentage)` - Validate percentage (0-100)
- `shared_utils.calculate_tax(amount, rate=8.5)` - Calculate tax

### Calculator
- `shared_utils.Calculator()` - Create calculator instance
  - `calc.add(a, b)` - Addition with history
  - `calc.subtract(a, b)` - Subtraction with history
  - `calc.multiply(a, b)` - Multiplication with history
  - `calc.divide(a, b)` - Division with history
  - `calc.get_history()` - Get calculation history
  - `calc.clear_history()` - Clear calculation history

### Utility Functions
- `shared_utils.get_project_root()` - Get the 202509-sept directory path

## Testing

Each part can be run independently:
```bash
cd "02 - Your New Part"
python part02.py
```

Or run all parts at once:
```bash
python main.py
```

## Benefits

✅ **Even simpler imports** - Just `import shared_utils`  
✅ **All utilities in one place** - No more multiple files to manage  
✅ **No complex import logic** - Everything is in the same file  
✅ **Enhanced calculator** - Now includes multiply, divide, and clear history  
✅ **Clean and fast** - Direct function calls, no wrapper layers  
✅ **Zero warnings** - All imports are clean and PEP 8 compliant  
✅ **Easy to extend** - Add new functions directly to shared_utils.py  

## What Changed

- **Before**: `from shared_utils import custom_utils` then `custom_utils.function()`
- **After**: `import shared_utils` then `shared_utils.function()`

This eliminates the wrapper layer and makes everything more direct and easier to understand!
