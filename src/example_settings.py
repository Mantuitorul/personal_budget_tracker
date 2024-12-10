"""
Example settings file for Personal Budget Tracker.
Copy this file to settings.py and modify as needed.
"""

from pathlib import Path

# Base directory of the project
# This automatically gets the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Database settings
# The SQLite database will be created in a 'data' directory
DATABASE = {
    'path': BASE_DIR / 'data' / 'budget.db'
}

# Application settings
# Set DEBUG to False in production
DEBUG = True
VERSION = '1.0.0'