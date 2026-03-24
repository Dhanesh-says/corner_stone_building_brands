import pandas as pd
import numpy as np

def generate_demand_data():
    dates_hist = pd.date_range(start="2025-01-01", end="2025-12-31", freq="ME")
    dates_proj = pd.date_range(start="2026-04-01", end="2026-12-31", freq="ME")
    
    # Historical
    hist_demand = np.random.normal(loc=1000, scale=150, size=len(dates_hist)).astype(int)
    hist_crm = np.random.normal(loc=1200, scale=100, size=len(dates_hist)).astype(int)
    
    # Projected
    proj_demand = np.random.normal(loc=1100, scale=100, size=len(dates_proj)).astype(int)
    proj_crm = np.random.normal(loc=1250, scale=150, size=len(dates_proj)).astype(int)
    proj_lower = proj_demand * 0.9
    proj_upper = proj_demand * 1.1
    
    df_hist = pd.DataFrame({"Date": dates_hist, "Demand": hist_demand, "CRM Pipeline": hist_crm, "Type": "Historical"})
    df_proj = pd.DataFrame({
        "Date": dates_proj, 
        "Demand": proj_demand, 
        "CRM Pipeline": proj_crm,
        "Lower Bound": proj_lower, 
        "Upper Bound": proj_upper,
        "Type": "Projected"
    })
    
    return pd.concat([df_hist, df_proj], ignore_index=True)

def generate_demand_by_region():
    data = {
        "Region": ["North America", "North America", "Canada", "Canada", "Mexico", "Mexico"],
        "Product": ["Vinyl Windows", "Metal Roofing", "Vinyl Windows", "Metal Roofing", "Vinyl Windows", "Metal Roofing"],
        "Revenue Impact ($M)": [45.2, 38.1, 12.4, 18.5, 8.7, 14.2],
        "DCs": [45, 20, 15, 10, 8, 8]
    }
    return pd.DataFrame(data)

def generate_install_time_data():
    data = {
        "Method": ["Traditional Framing", "Traditional Framing", "IMP / Hypersteel", "IMP / Hypersteel"],
        "Stage": ["Prep & Framing", "Finishing", "Prep & Framing", "Finishing"],
        "Time (Days)": [12, 8, 4, 3],
        "Install Labor Cost": [85, 85, 42, 42]
    }
    return pd.DataFrame(data)

def generate_install_revenue_data():
    data = {
        "Product Line": ["Ply Gem Siding", "Simonton Windows", "Mueller Metal", "ClipStone"],
        "Revenue Impact (USD)": [1250000, 850000, 2100000, 650000],
        "Labor Saved (USD)": [450000, 250000, 850000, 150000]
    }
    return pd.DataFrame(data)

def generate_system_flow_data():
    labels = ["SAP ECC (ERP)", "Salesforce (CRM)", "Brightly (OT)", "Design++ (Eng)", "Google Cloud (Ext)", "Pi Unify Core"]
    source = [0, 1, 2, 3, 4]
    target = [5, 5, 5, 5, 5]
    value = [100, 80, 60, 40, 50] 
    return labels, source, target, value

def generate_sensor_data():
    return {
        "OEE": np.random.uniform(65, 85),
        "Mfg Downtime": np.random.uniform(5, 15),
        "Cycle Time": np.random.uniform(2.0, 3.5),
        "Defect Rate": np.random.uniform(0.5, 2.5),
        "Energy Efficiency": np.random.uniform(85, 99)
    }

def generate_manufacturing_plants_data():
    data = {
        "Plant ID": ["PL-101", "PL-102", "PL-201", "PL-205"],
        "Machine ID": ["EXT-A1", "ROB-C4", "EXT-B2", "ASM-F1"],
        "Defect Rate (%)": [1.2, 3.5, 0.8, 2.1],
        "OEE (%)": [88, 72, 91, 78],
        "Output Volume": [15000, 8000, 18000, 11000]
    }
    return pd.DataFrame(data)

def get_parts_library_sample():
    data = {
        "Part Name": ["SunSteel Solar Roof", "ClipStone Mortarless", "Ply Gem Vinyl Siding", "Simonton Window 5500", "Hypersteel Cold-Formed"],
        "Category": ["Roofing", "Stone Veneer", "Siding", "Windows", "Metal Buildings"],
        "Availability": ["High", "Medium", "High", "High", "Low"],
        "BIM Downloads": [120, 85, 300, 215, 610],
        "Supplier Risk": ["Low", "Low", "Medium", "Low", "High"],
        "Avg Lead Time (Days)": [14, 7, 5, 10, 21],
        "Technical Material": ["Available", "Available", "Pending", "Available", "Available"],
        "Standard Drawings": ["Available", "Available", "Available", "Available", "Pending Review"]
    }
    return pd.DataFrame(data)

def generate_workforce_data():
    data = {
        "Shift": ["Morning (6AM-2PM)", "Afternoon (2PM-10PM)", "Night (10PM-6AM)"],
        "Fatigue Rate (%)": [12, 18, 28],
        "Man-Power Hours": [3200, 3150, 2800],
        "Efficiency Rate (%)": [92, 88, 76],
        "Workers on Leave": [5, 3, 8]
    }
    return pd.DataFrame(data)
