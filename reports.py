#!/usr/bin/env python3
"""
Report functions for analyzing badge access data using pandas.
These functions can be imported and used in building-access.py
"""

import sqlite3
import pandas as pd
from datetime import datetime
from pathlib import Path
import io
import sys

try:
    from reportlab.lib import colors
    from reportlab.lib.pagesizes import letter, A4
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, PageBreak
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.units import inch
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    REPORTLAB_AVAILABLE = True
except ImportError:
    REPORTLAB_AVAILABLE = False
    print("Warning: reportlab not installed. PDF export will not be available.")
    print("Install with: pip install reportlab")

# Import DB_PATH from Schema_exec to use same connection pattern
from Schema_exec import DB_PATH

def Schema_conn():
    """Get database connection using Schema_exec pattern."""
    return sqlite3.connect(DB_PATH)

def most_checkins_by_date():
    """Report showing dates with the most check-ins using pandas."""
    conn = Schema_conn()
    
    # Load check-in data into DataFrame
    query = """
    SELECT 
        DATE(tstamp) as check_date,
        tstamp,
        AccessGranted
    FROM Check_in
    """
    
    df = pd.read_sql_query(query, conn, parse_dates=['tstamp'])
    conn.close()
    
    # Convert check_date to datetime
    df['check_date'] = pd.to_datetime(df['check_date'])
    
    # Add day of week
    df['day_of_week'] = df['check_date'].dt.day_name()
    
    # Group by date and calculate statistics
    daily_stats = df.groupby(['check_date', 'day_of_week']).agg(
        total_checkins=('AccessGranted', 'count'),
        successful=('AccessGranted', 'sum'),
        denied=('AccessGranted', lambda x: len(x) - x.sum())
    ).reset_index()
    
    # Calculate success rate
    daily_stats['success_rate'] = (daily_stats['successful'] / daily_stats['total_checkins'] * 100).round(2)
    
    # Sort by total check-ins and get top 10
    top_days = daily_stats.nlargest(10, 'total_checkins')
    
    print("\n" + "="*80)
    print("TOP 10 DAYS WITH MOST CHECK-INS")
    print("="*80)
    print(top_days.to_string(index=False))
    print("-"*80)
    
    # Get peak hours for the busiest day
    if not top_days.empty:
        busiest_date = top_days.iloc[0]['check_date']
        
        # Filter for busiest day and extract hour
        busiest_day_df = df[df['check_date'] == busiest_date].copy()
        busiest_day_df['hour'] = busiest_day_df['tstamp'].dt.strftime('%H:00')
        
        # Count check-ins by hour
        hourly_counts = busiest_day_df.groupby('hour').size().reset_index(name='checkins')
        hourly_counts = hourly_counts.nlargest(5, 'checkins')
        
        print(f"\nPeak hours for busiest day ({busiest_date.date()}):")
        for _, row in hourly_counts.iterrows():
            print(f"  {row['hour']} - {row['checkins']} check-ins")
    
    return top_days

def most_checkins_by_building():
    """Report showing buildings with the most check-ins using pandas."""
    conn = Schema_conn()
    
    # Load data with building information
    query = """
    SELECT 
        b.name as building_name,
        c.check_id,
        c.AccessGranted,
        c.card_uid,
        c.ap_id,
        ap.ap_name
    FROM Check_in c
    JOIN Buildings b ON c.building_id = b.building_id
    JOIN AccessPoints ap ON c.building_id = ap.building_id AND c.ap_id = ap.ap_id
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    # Calculate building statistics
    building_stats = df.groupby('building_name').agg(
        total_checkins=('check_id', 'count'),
        successful=('AccessGranted', 'sum'),
        denied=('AccessGranted', lambda x: len(x) - x.sum()),
        unique_visitors=('card_uid', 'nunique')
    ).reset_index()
    
    # Calculate success rate
    building_stats['success_rate'] = (building_stats['successful'] / building_stats['total_checkins'] * 100).round(2)
    
    # Sort by total check-ins
    building_stats = building_stats.sort_values('total_checkins', ascending=False)
    
    print("\n" + "="*80)
    print("BUILDING ACCESS STATISTICS")
    print("="*80)
    print(building_stats.to_string(index=False))
    print("-"*80)
    
    # Show busiest access points for top building
    if not building_stats.empty:
        top_building = building_stats.iloc[0]['building_name']
        
        # Filter for top building and count by access point
        top_building_df = df[df['building_name'] == top_building]
        ap_counts = top_building_df.groupby('ap_name').size().reset_index(name='usage_count')
        ap_counts = ap_counts.nlargest(3, 'usage_count')
        
        print(f"\nMost used access points in {top_building}:")
        for _, row in ap_counts.iterrows():
            print(f"  {row['ap_name']} - {row['usage_count']} uses")
    
    return building_stats

def denial_report():
    """Report analyzing access denial patterns using pandas."""
    conn = Schema_conn()
    
    # Load denial data
    query = """
    SELECT 
        c.card_uid,
        c.building_id,
        c.ap_id,
        c.tstamp,
        b.name as building_name,
        ap.ap_name,
        ap.type as ap_type,
        p.first_name,
        p.last_name,
        CASE 
            WHEN p.card_uid LIKE '1%' THEN 'Student'
            WHEN p.card_uid LIKE '2%' THEN 'Faculty'
            WHEN p.card_uid LIKE '3%' THEN 'Staff'
            ELSE 'Unknown'
        END as user_type
    FROM Check_in c
    JOIN Buildings b ON c.building_id = b.building_id
    JOIN AccessPoints ap ON c.building_id = ap.building_id AND c.ap_id = ap.ap_id
    JOIN Person p ON c.card_uid = p.card_uid
    WHERE c.AccessGranted = 0
    """
    
    df = pd.read_sql_query(query, conn, parse_dates=['tstamp'])
    conn.close()
    
    print("\n" + "="*80)
    print("ACCESS DENIAL ANALYSIS REPORT")
    print("="*80)
    
    if not df.empty:
        # Overall statistics
        total_denials = len(df)
        unique_users = df['card_uid'].nunique()
        buildings_with_denials = df['building_id'].nunique()
        
        print(f"\nOverall Statistics:")
        print(f"  Total Denials: {total_denials}")
        print(f"  Unique Users Denied: {unique_users}")
        print(f"  Buildings with Denials: {buildings_with_denials}")
        
        # Denials by access point
        ap_denials = df.groupby(['building_name', 'ap_name', 'ap_type']).size().reset_index(name='denial_count')
        ap_denials = ap_denials.sort_values('denial_count', ascending=False)
        
        print("\n" + "-"*80)
        print("Denials by Access Point:")
        print(ap_denials.to_string(index=False))
        
        # Denials by user type
        user_denials = df.groupby('user_type').agg(
            unique_users=('card_uid', 'nunique'),
            total_denials=('card_uid', 'count'),
            buildings_denied=('building_name', lambda x: ', '.join(x.unique()))
        ).reset_index()
        
        # Truncate long building lists
        user_denials['buildings_denied'] = user_denials['buildings_denied'].apply(
            lambda x: x[:37] + '...' if len(x) > 40 else x
        )
        
        user_denials = user_denials.sort_values('total_denials', ascending=False)
        
        print("\n" + "-"*80)
        print("Denials by User Type:")
        print(user_denials.to_string(index=False))
        
        # Time patterns for denials
        df['hour'] = df['tstamp'].dt.strftime('%H:00')
        hourly_denials = df.groupby('hour').size().reset_index(name='denial_count')
        hourly_denials = hourly_denials.nlargest(5, 'denial_count')
        
        print("\n" + "-"*80)
        print("Top 5 Hours with Most Denials:")
        for _, row in hourly_denials.iterrows():
            print(f"  {row['hour']} - {row['denial_count']} denials")
        
        stats = pd.DataFrame([{
            'total_denials': total_denials,
            'unique_users_denied': unique_users,
            'buildings_with_denials': buildings_with_denials
        }])
        
    else:
        print("\nNo access denials found in the database.")
        stats = pd.DataFrame()
    
    print("-"*80)
    
    return stats

def create_pdf_from_report(report_data, report_output, report_name, filename=None):
    """
    Create a PDF from report data using reportlab.
    
    Args:
        report_data: DataFrame or data from the report
        report_output: String output from the report
        report_name: Name of the report
        filename: Optional filename for the PDF (without extension)
    
    Returns:
        Path to the generated PDF file or None if reportlab not available
    """
    if not REPORTLAB_AVAILABLE:
        print("\nError: reportlab is not installed. Cannot generate PDF.")
        print("Install with: pip install reportlab")
        return None
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{report_name}_{timestamp}.pdf"
    elif not filename.endswith('.pdf'):
        filename = f"{filename}.pdf"
    
    # Create PDF document
    doc = SimpleDocTemplate(filename, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=18,
        textColor=colors.HexColor('#34495e'),
        spaceAfter=20,
        alignment=TA_CENTER
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=10,
        leading=12
    )
    
    # Add title
    elements.append(Paragraph("Badge Access System Report", title_style))
    elements.append(Paragraph(report_name.replace('_', ' ').title(), subtitle_style))
    elements.append(Paragraph(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
    elements.append(Spacer(1, 0.2*inch))
    
    # Add report output as text
    if report_output:
        # Split output into lines and create paragraphs
        lines = report_output.split('\n')
        for line in lines:
            if line.strip():
                # Escape special characters for reportlab
                line = line.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                elements.append(Paragraph(line, normal_style))
            else:
                elements.append(Spacer(1, 0.1*inch))
    
    # Add DataFrame as table if it exists
    if isinstance(report_data, pd.DataFrame) and not report_data.empty:
        elements.append(Spacer(1, 0.3*inch))
        elements.append(Paragraph("Report Data Table", subtitle_style))
        elements.append(Spacer(1, 0.2*inch))
        
        # Convert DataFrame to list of lists for reportlab Table
        data = [report_data.columns.tolist()]  # Header
        for _, row in report_data.iterrows():
            data.append([str(val) for val in row.values])
        
        # Create table
        t = Table(data, repeatRows=1)
        
        # Add style to table
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c3e50')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('ALIGN', (0, 1), (-1, -1), 'LEFT'),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f8f9fa')]),
        ]))
        
        elements.append(t)
    
    # Build PDF
    doc.build(elements)
    
    print(f"\n✓ Report exported to PDF: {filename}")
    return Path(filename)

def ask_pdf_export(report_name, report_data, report_output):
    """
    Ask user if they want to export the report to PDF.
    
    Args:
        report_name: Name of the report
        report_data: DataFrame or data from the report
        report_output: String output from the report
    """
    if not REPORTLAB_AVAILABLE:
        return
    response = input("\nDo you want to export this report to PDF? (y/n): ").strip().lower()
    if response == 'y' or response == 'yes':
        custom_name = input("Enter filename (press Enter for auto-generated name): ").strip()
        if custom_name and not custom_name.endswith('.pdf'):
            custom_name = f"{custom_name}.pdf"
        elif not custom_name:
            custom_name = None
        
        create_pdf_from_report(report_data, report_output, report_name, custom_name)
        print("PDF export completed.")
    
def most_checkins_by_date_with_prompt():
    """
    Run most_checkins_by_date report and prompt for PDF export.
    """
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    try:
        df_result = most_checkins_by_date()
        report_output = buffer.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Print the output to console
    print(report_output)
    
    # Ask for PDF export
    ask_pdf_export('most_checkins_by_date', df_result, report_output)
    
    return df_result

def most_checkins_by_building_with_prompt():
    """
    Run most_checkins_by_building report and prompt for PDF export.
    """
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    try:
        df_result = most_checkins_by_building()
        report_output = buffer.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Print the output to console
    print(report_output)
    
    # Ask for PDF export
    ask_pdf_export('most_checkins_by_building', df_result, report_output)
    
    return df_result

def denial_report_with_prompt():
    """
    Run denial_report and prompt for PDF export.
    """
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = buffer = io.StringIO()
    
    try:
        df_result = denial_report()
        report_output = buffer.getvalue()
    finally:
        sys.stdout = old_stdout
    
    # Print the output to console
    print(report_output)
    
    # Ask for PDF export
    ask_pdf_export('denial_report', df_result, report_output)
    
    return df_result

def run_all_reports():
    """Run all three reports and return DataFrames."""
    print("\n" + "="*80)
    print(" BADGE ACCESS SYSTEM - ANALYSIS REPORTS ")
    print(" Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("="*80)
    
    date_df = most_checkins_by_date()
    building_df = most_checkins_by_building()
    denial_df = denial_report()
    
    print("\n" + "="*80)
    print(" END OF REPORTS ")
    print("="*80)
    
    return {
        'date_report': date_df,
        'building_report': building_df,
        'denial_report': denial_df
    }

def interactive_reports_menu():
    """
    Interactive menu for running reports with PDF export option.
    """
    while True:
        print("\n" + "="*50)
        print(" BADGE ACCESS REPORTS MENU")
        print("="*50)
        print("1. Most Check-ins by Date")
        print("2. Most Check-ins by Building")
        print("3. Access Denial Report")
        print("4. Run All Reports")
        print("5. Exit")
        print("-"*50)
        
        choice = input("Select report (1-5): ").strip()
        
        if choice == '1':
            most_checkins_by_date_with_prompt()
        elif choice == '2':
            most_checkins_by_building_with_prompt()
        elif choice == '3':
            denial_report_with_prompt()
        elif choice == '4':
            # Run all reports without prompts
            results = run_all_reports()
            
            # Ask if user wants to export all to PDF
            if REPORTLAB_AVAILABLE:
                response = input("\nDo you want to export all reports to PDF? (y/n): ").strip().lower()
                if response == 'y' or response == 'yes':
                    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                    filename = f"all_reports_{timestamp}.pdf"
                    
                    # Capture all outputs
                    old_stdout = sys.stdout
                    sys.stdout = buffer = io.StringIO()
                    
                    try:
                        run_all_reports()
                        all_output = buffer.getvalue()
                    finally:
                        sys.stdout = old_stdout
                    
                    # Create combined PDF
                    create_pdf_from_report(None, all_output, 'all_reports', filename)
        elif choice == '5':
            print("Exiting reports...")
            break
        else:
            print("Invalid choice. Please select 1-5.")
        
        if choice != '5':
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # If run directly, show interactive menu
    interactive_reports_menu()
