#!/bin/bash
# Installation script for Badge Access System

echo "========================================="
echo "Badge Access System - Installation Script"
echo "========================================="

# Check Python version
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | grep -Po '(?<=Python )\d+\.\d+')
required_version="3.8"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then 
    echo "Error: Python 3.8 or higher is required. Found: Python $python_version"
    exit 1
fi
echo "✓ Python $python_version found"

# Create virtual environment
echo ""
echo "Creating virtual environment..."
if [ -d "venv" ]; then
    echo "Virtual environment already exists. Skipping..."
else
    python3 -m venv venv
    echo "✓ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
source venv/bin/activate
echo "✓ Virtual environment activated"

# Upgrade pip
echo ""
echo "Upgrading pip..."
pip install --upgrade pip --quiet
echo "✓ pip upgraded"

# Install requirements
echo ""
echo "Installing required packages..."
pip install -r requirements.txt
echo "✓ All packages installed"

# Initialize database
echo ""
echo "Initializing database..."
python3 -c "from Schema_exec import extend_schema; extend_schema()" 2>/dev/null || true
echo "✓ Database initialized"

# Check if seed data should be loaded
echo ""
read -p "Do you want to load sample data? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [ -f "accesdb_seed_data.sql" ]; then
        sqlite3 accessdb.db < accesdb_seed_data.sql 2>/dev/null || echo "Note: Some sample data may already exist"
    fi
    if [ -f "check_in_seed_data.sql" ]; then
        sqlite3 accessdb.db < check_in_seed_data.sql 2>/dev/null || echo "Note: Some check-in data may already exist"
    fi
    echo "✓ Sample data loaded"
fi

echo ""
echo "========================================="
echo "Installation Complete!"
echo "========================================="
echo ""
echo "To run the application:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Run the application: python building-access.py"
echo ""
echo "For Windows users, use: venv\\Scripts\\activate"