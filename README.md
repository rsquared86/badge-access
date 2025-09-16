# Badge Access Control System

A comprehensive badge access control system with reporting, data visualization, and PDF export capabilities.

## Features

- **Person Management**: Create, read, update, and delete person records
- **Building Management**: Manage building information and access points
- **Access Control**: Check and grant building access permissions
- **Check-in Logging**: Automatic logging of all access attempts
- **Reports**: 
  - Most check-ins by date
  - Most check-ins by building
  - Access denial analysis
  - PDF export for all reports
- **Data Visualization**:
  - Building access bar charts
  - Access time heatmaps
  - Trend analysis charts
- **Database**: SQLite with proper foreign key constraints

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment (recommended)

### Quick Installation

1. Clone the repository:
```bash
git clone https://github.com/rsquared86/badge-access.git
cd badge-access
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install all required dependencies:
```bash
pip install -r requirements.txt
```

### Alternative Installation Methods

#### Using setup.py:
```bash
pip install .
```

#### For development with extra tools:
```bash
pip install -e ".[dev]"
```

## Required Libraries

The application requires the following Python libraries:

- **pandas** (>=2.0.0) - Data manipulation and analysis
- **numpy** (>=1.24.0) - Numerical computing support
- **reportlab** (>=4.0.0) - PDF generation for reports
- **plotnine** (>=0.12.0) - Grammar of graphics for Python (ggplot2-like)
- **matplotlib** (>=3.7.0) - Plotting library (required by plotnine)
- **python-dateutil** (>=2.8.0) - Date/time utilities

## Database Setup

The application will automatically create the SQLite database (`accessdb.db`) on first run with all necessary tables:

- Person
- Buildings
- AccessPoints
- Check_in
- Person_bldg_access
- Roles
- PersonRoles

To populate with sample data:
```bash
sqlite3 accessdb.db < accesdb_seed_data.sql
sqlite3 accessdb.db < check_in_seed_data.sql
```

## Usage

### Running the Application

```bash
python building-access.py
```

### Main Menu Options

1. **Create Person** - Add new person with card UID
2. **Get Person by Card UID** - Look up person details
3. **Update Person** - Modify person information
4. **Delete Person** - Remove person from system
5. **Create Building** - Add new building
6. **Get Building** - Look up building details
7. **Update Building** - Modify building information
8. **Delete Building** - Remove building from system
9. **Check Building Access** - Verify and log access attempt
10. **Add Building Access** - Grant access permission
11. **Reports & Analytics** - Access reports and charts
12. **Exit** - Close application

### Reports & Analytics Submenu

**Reports (with PDF export):**
1. Most Check-ins by Date
2. Most Check-ins by Building
3. Denial Report

**Charts (PNG export):**
4. Building Access Bar Chart (Last 2 Weeks)
5. Access Time Heatmap
6. Access Trends by Building
7. Generate All Charts

## File Structure

```
badge-access/
├── building-access.py    # Main application entry point
├── Schema_exec.py         # Database schema setup
├── Schema_conn.py         # Database connection utility
├── person.py              # Person CRUD operations
├── buildings.py           # Building CRUD operations
├── access.py              # Access control functions
├── reports.py             # Report generation with PDF export
├── charts.py              # Data visualization functions
├── menu.py                # Menu display utilities
├── requirements.txt       # Python dependencies
├── setup.py               # Installation script
├── accessdb.db            # SQLite database (created on first run)
├── accesdb_seed_data.sql  # Sample data for testing
└── check_in_seed_data.sql # Sample check-in logs
```

## Troubleshooting

### Import Errors

If you encounter import errors, ensure all dependencies are installed:
```bash
pip install --upgrade -r requirements.txt
```

### Database Errors

If database errors occur, you can reset the database:
```bash
rm accessdb.db
python -c "from Schema_exec import extend_schema; extend_schema()"
```

### PDF Export Issues

If PDF export fails, verify reportlab installation:
```bash
pip install --upgrade reportlab
```

### Chart Display Issues

If charts don't display, check plotnine and matplotlib:
```bash
pip install --upgrade plotnine matplotlib
```

## Development

### Running Tests (if implemented)
```bash
pytest tests/
```

### Code Formatting
```bash
black *.py
```

### Linting
```bash
flake8 *.py
```

## License

MIT License - See LICENSE file for details

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Support

For issues, questions, or suggestions, please open an issue on GitHub.