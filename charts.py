#!/usr/bin/env python3
"""
Chart functions for visualizing badge access data using plotnine.
These functions can be imported and used in building-access.py
"""

import sqlite3
import pandas as pd
from datetime import datetime, timedelta
from pathlib import Path

try:
    from plotnine import *
    import matplotlib.pyplot as plt
    from plotnine.scales import scale_fill_gradient2, scale_fill_cmap
    PLOTNINE_AVAILABLE = True
except ImportError:
    PLOTNINE_AVAILABLE = False
    print("Warning: plotnine not installed. Charts will not be available.")
    print("Install with: pip install plotnine")

# Import DB_PATH from Schema_exec to use same connection pattern
from Schema_exec import DB_PATH

def Schema_conn():
    """Get database connection using Schema_exec pattern."""
    return sqlite3.connect(DB_PATH)

def building_access_bar_chart(save_path=None):
    """
    Create a bar chart showing building access for the last 2 weeks.
    
    Args:
        save_path: Optional path to save the chart (e.g., 'building_access.png')
    
    Returns:
        plotnine chart object
    """
    if not PLOTNINE_AVAILABLE:
        print("Error: plotnine is not installed. Cannot generate charts.")
        print("Install with: pip install plotnine")
        return None
    
    conn = Schema_conn()
    
    # Calculate date range for last 2 weeks
    end_date = datetime(2025,1,31)
    start_date = end_date - timedelta(days=30)
    
    # Query for building access data in the last 2 weeks
    query = """
    SELECT 
        b.name as building_name,
        COUNT(*) as total_access,
        SUM(c.AccessGranted) as successful_access,
        COUNT(*) - SUM(c.AccessGranted) as denied_access
    FROM Check_in c
    JOIN Buildings b ON c.building_id = b.building_id
    WHERE DATE(c.tstamp) >= ? AND DATE(c.tstamp) <= ?
    GROUP BY b.building_id, b.name
    ORDER BY total_access DESC
    """
    
    df = pd.read_sql_query(query, conn, params=(start_date, end_date))
    conn.close()
    
    if df.empty:
        print("No access data found for the last 2 weeks.")
        return None
    
    # Reshape data for stacked bar chart
    df_melted = pd.melt(df, 
                       id_vars=['building_name'], 
                       value_vars=['successful_access', 'denied_access'],
                       var_name='access_type', 
                       value_name='count')
    
    # Create more readable labels
    df_melted['access_type'] = df_melted['access_type'].map({
        'successful_access': 'Granted',
        'denied_access': 'Denied'
    })
    
    # Create the chart
    chart = (ggplot(df_melted, aes(x='building_name', y='count', fill='access_type')) +
             geom_col(position='stack') +
             scale_fill_manual(values=['#e74c3c', '#2ecc71' ]) +
             labs(title='Building Access Summary - Last 2 Weeks',
                  subtitle=f'{start_date} to {end_date}',
                  x='Building',
                  y='Number of Access Attempts',
                  fill='Access Result') +
             theme_minimal() +
             theme(axis_text_x=element_text(rotation=45, hjust=1),
                   plot_title=element_text(size=16, weight='bold'),
                   plot_subtitle=element_text(size=12),
                   legend_position='top') +
             coord_flip())
    
    # Display the chart
    print(chart)
    
    # Save if path provided
    if save_path:
        chart.save(save_path, width=12, height=8, dpi=300)
        print(f"Chart saved to: {save_path}")
    
    return chart

def access_time_heatmap(save_path=None):
    """
    Create a heatmap showing access patterns by day of week and hour.
    
    Args:
        save_path: Optional path to save the chart (e.g., 'access_heatmap.png')
    
    Returns:
        plotnine chart object
    """
    if not PLOTNINE_AVAILABLE:
        print("Error: plotnine is not installed. Cannot generate charts.")
        print("Install with: pip install plotnine")
        return None
    
    conn = Schema_conn()
    
    # Query for all successful access data with time information
    query = """
    SELECT 
        strftime('%w', tstamp) as day_of_week_num,
        strftime('%H', tstamp) as hour,
        COUNT(*) as access_count
    FROM Check_in
    WHERE AccessGranted = 1
    GROUP BY strftime('%w', tstamp), strftime('%H', tstamp)
    ORDER BY day_of_week_num, hour
    """
    
    df = pd.read_sql_query(query, conn)
    conn.close()
    
    if df.empty:
        print("No successful access data found.")
        return None
    
    # Convert to proper types
    df['day_of_week_num'] = df['day_of_week_num'].astype(int)
    df['hour'] = df['hour'].astype(int)
    
    # Map day numbers to names
    day_names = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 
                 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    df['day_of_week'] = df['day_of_week_num'].map(day_names)
    
    # Create ordered factor for days
    df['day_of_week'] = pd.Categorical(df['day_of_week'], 
                                      categories=['Monday', 'Tuesday', 'Wednesday', 
                                                'Thursday', 'Friday', 'Saturday', 'Sunday'], 
                                      ordered=True)
    
    # Create the heatmap
    chart = (ggplot(df, aes(x='hour', y='day_of_week', fill='access_count')) +
             geom_tile(color='white', size=0.5) +
             scale_fill_gradient2(low='#3498db', mid='#f39c12', high='#e74c3c',
                                midpoint=df['access_count'].median()) +
             scale_x_continuous(breaks=range(0, 24, 2),
                              labels=[f"{i}:00" for i in range(0, 24, 2)]) +
             labs(title='Access Patterns by Day and Time',
                  subtitle='Heatmap of successful access attempts',
                  x='Hour of Day',
                  y='Day of Week',
                  fill='Access Count') +
             theme_minimal() +
             theme(axis_text_x=element_text(rotation=45, hjust=1),
                   plot_title=element_text(size=16, weight='bold'),
                   plot_subtitle=element_text(size=12),
                   panel_grid=element_blank()))
    
    # Display the chart
    print(chart)
    
    # Save if path provided
    if save_path:
        chart.save(save_path, width=12, height=6, dpi=300)
        print(f"Heatmap saved to: {save_path}")
    
    return chart

def access_trends_by_building(building_name=None, save_path=None):
    """
    Create a line chart showing access trends over time for a specific building or all buildings.
    
    Args:
        building_name: Optional specific building name to focus on
        save_path: Optional path to save the chart
    
    Returns:
        plotnine chart object
    """
    if not PLOTNINE_AVAILABLE:
        print("Error: plotnine is not installed. Cannot generate charts.")
        return None
    
    conn = Schema_conn()
    
    # Base query for access trends
    if building_name:
        query = """
        SELECT 
            DATE(c.tstamp) as access_date,
            b.name as building_name,
            COUNT(*) as total_access,
            SUM(c.AccessGranted) as successful_access
        FROM Check_in c
        JOIN Buildings b ON c.building_id = b.building_id
        WHERE b.name = ?
        GROUP BY DATE(c.tstamp), b.name
        ORDER BY access_date
        """
        df = pd.read_sql_query(query, conn, params=(building_name,))
    else:
        query = """
        SELECT 
            DATE(c.tstamp) as access_date,
            b.name as building_name,
            COUNT(*) as total_access,
            SUM(c.AccessGranted) as successful_access
        FROM Check_in c
        JOIN Buildings b ON c.building_id = b.building_id
        GROUP BY DATE(c.tstamp), b.name
        ORDER BY access_date, b.name
        """
        df = pd.read_sql_query(query, conn)
    
    conn.close()
    
    if df.empty:
        print(f"No access data found{' for ' + building_name if building_name else ''}.")
        return None
    
    # Convert date column
    df['access_date'] = pd.to_datetime(df['access_date'])
    
    # Create the chart
    if building_name:
        chart = (ggplot(df, aes(x='access_date', y='successful_access')) +
                 geom_line(color='#2ecc71', size=1.2) +
                 geom_point(color='#27ae60', size=2) +
                 labs(title=f'Access Trends - {building_name}',
                      x='Date',
                      y='Successful Access Count'))
    else:
        chart = (ggplot(df, aes(x='access_date', y='successful_access', color='building_name')) +
                 geom_line(size=1) +
                 geom_point(size=1.5) +
                 labs(title='Access Trends by Building',
                      x='Date',
                      y='Successful Access Count',
                      color='Building'))
    
    chart = (chart +
             theme_minimal() +
             theme(axis_text_x=element_text(rotation=45, hjust=1),
                   plot_title=element_text(size=16, weight='bold'),
                   legend_position='right'))
    
    # Display the chart
    print(chart)
    
    # Save if path provided
    if save_path:
        chart.save(save_path, width=12, height=6, dpi=300)
        print(f"Trend chart saved to: {save_path}")
    
    return chart

def create_all_charts(save_charts=True):
    """
    Create all available charts.
    
    Args:
        save_charts: Whether to save charts to files
    
    Returns:
        Dictionary of chart objects
    """
    print("Creating building access visualizations...")
    
    charts = {}
    
    # Create building access bar chart
    print("\n1. Building Access Bar Chart")
    charts['building_bar'] = building_access_bar_chart(
        'building_access_2weeks.png' if save_charts else None
    )
    
    # Create access time heatmap
    print("\n2. Access Time Heatmap")
    charts['time_heatmap'] = access_time_heatmap(
        'access_time_heatmap.png' if save_charts else None
    )
    
    # Create access trends chart
    print("\n3. Access Trends Over Time")
    charts['trends'] = access_trends_by_building(
        save_path='access_trends.png' if save_charts else None
    )
    
    if save_charts:
        print(f"\n✅ All charts created and saved!")
    
    return charts

def interactive_charts_menu():
    """
    Interactive menu for creating charts.
    """
    if not PLOTNINE_AVAILABLE:
        print("Error: plotnine is not installed. Cannot generate charts.")
        print("Install with: pip install plotnine")
        return
    
    while True:
        print("\n" + "="*50)
        print(" BADGE ACCESS CHARTS MENU")
        print("="*50)
        print("1. Building Access Bar Chart (Last 2 Weeks)")
        print("2. Access Time Heatmap")
        print("3. Access Trends by Building")
        print("4. Create All Charts")
        print("5. Exit")
        print("-"*50)
        
        choice = input("Select chart (1-5): ").strip()
        
        if choice == '1':
            save = input("Save chart to file? (y/n): ").strip().lower() == 'y'
            building_access_bar_chart('building_access_2weeks.png' if save else None)
            
        elif choice == '2':
            save = input("Save chart to file? (y/n): ").strip().lower() == 'y'
            access_time_heatmap('access_time_heatmap.png' if save else None)
            
        elif choice == '3':
            building = input("Enter building name (or press Enter for all buildings): ").strip()
            building = building if building else None
            save = input("Save chart to file? (y/n): ").strip().lower() == 'y'
            filename = f"trends_{building.replace(' ', '_').lower()}.png" if save and building else "access_trends.png" if save else None
            access_trends_by_building(building, filename)
            
        elif choice == '4':
            save = input("Save all charts to files? (y/n): ").strip().lower() == 'y'
            create_all_charts(save)
            
        elif choice == '5':
            print("Exiting charts menu...")
            break
            
        else:
            print("Invalid choice. Please select 1-5.")
        
        if choice != '5':
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    # If run directly, show interactive menu
    interactive_charts_menu()