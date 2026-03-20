import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from data_mock import (
    generate_demand_data, 
    generate_demand_by_region,
    generate_install_time_data,
    generate_install_revenue_data,
    generate_system_flow_data,
    generate_sensor_data,
    generate_manufacturing_plants_data,
    get_parts_library_sample,
    generate_workforce_data
)

# ----- Dashboard Configuration -----
st.set_page_config(
    page_title="PiAB | Intelligence Hub",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
def load_css(file_path):
    try:
        with open(file_path) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except Exception as e:
        pass

load_css("style.css")

# --- Session State for Navigation ---
if 'page' not in st.session_state:
    st.session_state.page = 'Main Dashboard'

def set_page(page_name):
    st.session_state.page = page_name

# ----- Left UI Configuration -----
with st.sidebar:
    st.markdown("<h2 style='display:flex; align-items:center; gap: 10px; color:#1E293B;'><span style='background:#3B82F6; padding: 4px; border-radius: 8px;'>✨</span> PiAB</h2>", unsafe_allow_html=True)
    st.markdown("---")
    
    st.markdown("<div class='nav-section'>GEMINI ENTERPRISE</div>", unsafe_allow_html=True)
    
    if st.button("🔵 Pi Decision", use_container_width=True):
        set_page('Main Dashboard')
    st.markdown("<div class='nav-subitem active'>Pi Agent</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='nav-item'>Agentic Platform</div>", unsafe_allow_html=True)
    st.markdown("<div class='nav-item'>MultiModal Live Agent</div>", unsafe_allow_html=True)
    st.markdown("<div class='nav-item'>Pi Semantic</div>", unsafe_allow_html=True)
    
    st.markdown("<div class='nav-section'>DATA CLOUD</div>", unsafe_allow_html=True)
    if st.button("💿 Pi Unify", use_container_width=True):
        set_page('Pi Unify')
    if st.button("🛡️ Pi Shield", use_container_width=True):
        set_page('Pi Shield')

# ----- Main Content Area -----
if st.session_state.page == 'Pi Unify':
    st.title("Pi Unify")
    st.markdown("### Information on Gemini said")
    st.markdown("""
    To maintain its position as a market leader, **Cornerstone Building Brands** relies on a sophisticated "Digital Thread" that connects its 80+ manufacturing plants and 106 distribution centers. They synchronize high-level planning data with real-time shop floor reality to eliminate the "IT vs. OT data disconnect."
    
    Here are the primary data sources and systems they utilize across their global operations:
    
    #### 1. Enterprise Resource Planning (ERP): The Operational Core
    Cornerstone primarily uses SAP ECC (and is transitioning parts of the business toward S/4HANA) as its backbone.
    **Data Extracted**: Bill of Materials (BOM), production schedules, procurement costs, and real-time inventory levels across all DCs.
    **Role**: It acts as the "Single Source of Truth" for financial reporting and order management.
    
    #### 2. Customer Relationship Management (CRM): The Demand Signal
    They utilize Salesforce to capture the "front-end" of the supply chain.
    **Data Extracted**: Sales pipelines, quote-to-order velocity, customer preferences for specific finishes (like the popular black/bronze window frames), and regional demand trends.
    **Role**: This provides the Demand Planning engine with forward-looking signals rather than just relying on historical sales.
    
    #### 3. Operational Technology (OT) & IoT: The Shop Floor Reality
    To achieve Manufacturing Modernization, they pull data directly from the factory floor.
    **Data Sources**: PLC (Programmable Logic Controllers) on robotic assembly lines, IoT sensors on extruders (for vinyl siding), and machine health monitors.
    **Role**: This data is fed into systems like Brightly (maintenance software) to enable Preventive Maintenance and reduce downtime.
    
    #### 4. Specialized Engineering & Design Data
    Since a large portion of their business is "Engineered-to-Order" (especially in the Metal Buildings segment), engineering data is a critical source.
    **Systems**: Design++ (automation platform) and CAD/BIM libraries.
    **Data Extracted**: Structural requirements, parts dimensions, and custom configuration rules.
    **Role**: Feeds the Global Parts Library, allowing for rapid "What-If" scenarios during the design phase.
    
    #### 5. External Market & Macro Signals
    To solve Volatile Lead Times, they augment internal data with external "Big Data."
    **Data Sources**: Housing start statistics, interest rate trends, weather patterns (affecting construction seasons), and geopolitical logistics data.
    **Role**: These are processed in Google Cloud (BigQuery) to refine the Demand Forecast and adjust inventory buffers.
    """)

elif st.session_state.page == 'Pi Shield':
    st.title("Pi Shield")
    st.markdown("### Data Governance & Security")
    st.info("Pi Shield strictly governs data access across the Cornerstone digital thread, ensuring encryption at rest and in transit. Role-based access controls limit sensitive ERP financial data and OT machine telemetry exclusively to authorized supply chain analysts and plant managers.")

else:
    # --- Main Dashboard ---
    df_demand_global_ref = generate_demand_data()
    avg_hist = df_demand_global_ref[df_demand_global_ref['Type'] == 'Historical']['Demand'].mean()
    avg_proj = df_demand_global_ref[df_demand_global_ref['Type'] == 'Projected']['Demand'].mean()
    demand_surge_pct = ((avg_proj - avg_hist) / avg_hist) * 100

    st.markdown("""
        <div style='display: flex; gap: 10px; margin-bottom: 20px; font-size: 0.85rem; font-weight: bold; padding: 10px; background: #F1F5F9; border-radius: 8px;'>
           THEME: <span style='color: #F87171'>IDEATE</span> • <span style='color: #FBBF24'>PLAN</span> • <span style='color: #34D399'>SOURCE</span> • <span style='color: #60A5FA'>MAKE</span> • <span style='color: #818CF8'>DELIVER</span> • <span style='color: #A78BFA'>RETURN</span> • <span style='color: #F472B6'>ENABLE</span> • <span style='color: #9CA3AF'>SUPPORT</span>
        </div>
    """, unsafe_allow_html=True)

    tabs = st.tabs([
        "Digital Twin", 
        "Global Parts Library", 
        "Demand Orchestration", 
        "Installation Cost Reduction", 
        "Manufacturing Modernization",
        "Workforce Management"
    ])

    # Tab 1: Digital Twin
    with tabs[0]:
        st.markdown("<h3 style='color: #F87171'>Digital Twin (Ideate/Plan)</h3>", unsafe_allow_html=True)
        st.markdown("Explains demand, inventory, and supply chain health across Cornerstone operations.")
        
        col1, col2, col3 = st.columns(3)
        col1.metric("Lost Revenue Risk", "$1.8M", "+$0.6M")
        col2.metric("Omni Order Rate", "96.8%", "+2.1%")
        col3.metric("Regional Response Time", "4.2h", "-1.8h")
        
        st.markdown("### System Topology & Data Flow")
        labels, source, target, value = generate_system_flow_data()
        fig1 = go.Figure(data=[go.Sankey(
            node=dict(
                pad=15, thickness=20,
                line=dict(color="black", width=0.5), label=labels,
                color=["#3B82F6", "#10B981", "#F59E0B", "#8B5CF6", "#EC4899", "#D97706"]
            ),
            link=dict(source=source, target=target, value=value, color="rgba(156, 163, 175, 0.3)")
        )])
        fig1.update_layout(height=350, font_family="Inter", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=10, b=10))
        st.plotly_chart(fig1, use_container_width=True)

    # Tab 2: Global Parts Library
    with tabs[1]:
        st.markdown("<h3 style='color: #34D399'>Global Parts Library (Source)</h3>", unsafe_allow_html=True)
        st.markdown("**Also known as Digital Asset Management (DAM)**")
        st.markdown("Provides product details, standard drawings, and supporting technical material for Cornerstone Building Brands.")
        
        df_parts = get_parts_library_sample()
        
        high_risk_parts = df_parts[(df_parts["BIM Downloads"] > 200) & (df_parts["Supplier Risk"] == "High")]
        if not high_risk_parts.empty:
             st.warning(f"**ALERT**: If BIM Downloads are high but Supplier Risk is also high, the Pi Agent alerts the engineering team to find an alternative supplier for that part before it becomes a bottleneck in a major building project.\n\nIdentified Part: {high_risk_parts['Part Name'].iloc[0]}")
        
        st.dataframe(df_parts, use_container_width=True, hide_index=True)
        
        st.markdown("#### Download Technical Assets")
        col_dl1, col_dl2, col_dl3 = st.columns([2, 1, 1])
        selected_part = col_dl1.selectbox("Select Part for Download", df_parts['Part Name'].tolist(), key="dl_part")
        
        col_dl2.markdown("<br>", unsafe_allow_html=True)
        col_dl2.download_button(label="📥 Standard Drawings (CAD/PDF)", data="mock_cad_data", file_name=f"{selected_part.replace(' ', '_')}_drawings.pdf", use_container_width=True)
        
        col_dl3.markdown("<br>", unsafe_allow_html=True)
        col_dl3.download_button(label="📥 Technical Material (Specs)", data="mock_spec_data", file_name=f"{selected_part.replace(' ', '_')}_specs.pdf", use_container_width=True)

    # Tab 3: Demand Orchestration
    with tabs[2]:
        st.markdown("<h3 style='color: #FBBF24'>Demand Orchestration (Plan)</h3>", unsafe_allow_html=True)
        st.info(f"**WORKFORCE ALIGNMENT ALERT**: Projected {demand_surge_pct:.1f}% overall demand surge requires active headcount planning. See Workforce Management tab for localized shift adjustments and labor impact.")
        st.success("**RECOMMENDATION**: Traditional forecasting only looks at history. By adding the CRM Pipeline (future intent) to the Forecast Accuracy (past performance), the AI creates a proactive plan that reduces the Stock-out Risk.")
        
        st.markdown("#### Demand Filters")
        col1, col2, col3 = st.columns(3)
        region_filter = col1.selectbox("Region", ["All", "North America", "Canada", "Mexico"], key="do_region")
        product_filter = col2.selectbox("Product Category", ["All", "Vinyl Windows", "Metal Roofing"], key="do_product")
        horizon_filter = col3.slider("Forecast Horizon (Months)", 3, 24, 12, key="do_horizon")
        
        col_dc, col_rev = st.columns(2)
        col_dc.selectbox("Distribution Center (DC)", ["All", "DC-North", "DC-South", "DC-West"], key="do_dc")
        col_rev.slider("Revenue Impact Range ($M)", 0.0, 50.0, (5.0, 45.0), key="do_rev")
        
        df_demand_region = generate_demand_by_region()
        if region_filter != "All":
            df_demand_region = df_demand_region[df_demand_region["Region"] == region_filter]
        if product_filter != "All":
            df_demand_region = df_demand_region[df_demand_region["Product"] == product_filter]
            
        fig_bar1 = px.bar(df_demand_region, x="Region", y="Revenue Impact ($M)", color="Product", title="Revenue Impact by Product & Region", barmode="group", color_discrete_sequence=["#3B82F6", "#10B981"])
        fig_bar1.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_bar1, use_container_width=True)

        st.markdown("#### Timeline Forecast View")
        df_demand = generate_demand_data()
        fig2 = go.Figure()
        hist_data = df_demand[df_demand['Type'] == 'Historical']
        fig2.add_trace(go.Scatter(x=hist_data['Date'], y=hist_data['Demand'], mode='lines+markers', name='Historical Demand', line=dict(color='#8B5CF6', width=3)))
        proj_data = df_demand[df_demand['Type'] == 'Projected'].head(horizon_filter)
        fig2.add_trace(go.Scatter(x=proj_data['Date'], y=proj_data['Demand'], mode='lines', name='AI Forecast', line=dict(color='#10B981', width=3, dash='dot')))
        fig2.add_trace(go.Scatter(x=proj_data['Date'], y=proj_data['CRM Pipeline'], mode='lines', name='CRM Pipeline (Future Intent)', line=dict(color='#3B82F6', width=2)))
        fig2.update_layout(height=350, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig2, use_container_width=True)

    # Tab 4: Installation Cost Reduction
    with tabs[3]:
        st.markdown("<h3 style='color: #60A5FA'>Installation Cost Reduction (Make/Deliver)</h3>", unsafe_allow_html=True)
        st.info("**INSIGHT**: Cornerstone uses the Install Labor Cost metric to identify which products are 'labor-friendly.' If a specific type of siding reduces labor from $85 to $42 per unit, the sales team uses this data to justify a higher price point for that product.")
        
        st.markdown("#### Cost Reduction Filters")
        col_install1, col_install2 = st.columns(2)
        target_product = col_install1.selectbox("Product Line Focus", ["All", "Ply Gem Siding", "Simonton Windows", "Mueller Metal", "ClipStone"], key="inst_prod")
        min_rev_impact = col_install2.number_input("Min Revenue Impacted (USD)", 0, 5000000, 500000)

        df_install_rev = generate_install_revenue_data()
        if target_product != "All":
            df_install_rev = df_install_rev[df_install_rev["Product Line"] == target_product]
        df_install_rev = df_install_rev[df_install_rev["Revenue Impact (USD)"] >= min_rev_impact]

        col_c1, col_c2 = st.columns(2)
        with col_c1:
            fig3 = px.bar(df_install_rev, x="Product Line", y=["Revenue Impact (USD)", "Labor Saved (USD)"], title="Revenue & Labor Matrix (USD)", barmode="group", color_discrete_sequence=["#F59E0B", "#10B981"])
            fig3.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig3, use_container_width=True)

        with col_c2:
            df_install = generate_install_time_data()
            fig_inst_time = px.bar(df_install, x="Install Labor Cost", y="Method", color="Stage", orientation='h', barmode='stack', color_discrete_sequence=["#D97706", "#3B82F6"], title="Labor Cost vs Method")
            fig_inst_time.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_inst_time, use_container_width=True)

    # Tab 5: Manufacturing Modernization
    with tabs[4]:
        st.markdown("<h3 style='color: #60A5FA'>Manufacturing Modernization (Make)</h3>", unsafe_allow_html=True)
        
        sensors = generate_sensor_data()
        if sensors["OEE"] < 80 and sensors["Mfg Downtime"] > 10:
             st.warning("**ALERT: Hidden Factories Identified**\n\nBy monitoring OEE and Downtime through IoT sensors, the system identifies 'Hidden Factories' — lost capacity that can be reclaimed through Preventive Maintenance rather than buying new machines.")
        else:
             st.success("OEE is optimal. Preventive Maintenance schedule dynamically updated.")
        
        st.markdown("#### Manufacturing Automation Filters")
        col_m1, col_m2, col_m3 = st.columns(3)
        plant_id = col_m1.selectbox("Plant ID", ["All", "PL-101", "PL-102", "PL-201", "PL-205"])
        machine_id = col_m2.selectbox("Machine ID", ["All", "EXT-A1", "ROB-C4", "EXT-B2", "ASM-F1"])
        max_defect = col_m3.slider("Max Defective Rate Tolerance (%)", 0.0, 5.0, 2.0)
        
        df_mfg = generate_manufacturing_plants_data()
        if plant_id != "All":
            df_mfg = df_mfg[df_mfg["Plant ID"] == plant_id]
        if machine_id != "All":
            df_mfg = df_mfg[df_mfg["Machine ID"] == machine_id]
        
        df_mfg = df_mfg[df_mfg["Defect Rate (%)"] <= max_defect]

        fig_mfg_bar = px.bar(df_mfg, x="Machine ID", y="Output Volume", color="Defect Rate (%)", title="Output metrics & Quality by Machine", color_continuous_scale="RdYlGn_r")
        fig_mfg_bar.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
        st.plotly_chart(fig_mfg_bar, use_container_width=True)

        col1, col2 = st.columns([1, 1])
        with col1:
             fig4 = go.Figure()
             fig4.add_trace(go.Indicator(
                 mode="gauge+number", value=sensors["OEE"], title={'text': "Network Average OEE (%)"},
                 domain={'x': [0, 1], 'y': [0, 1]},
                 gauge={'axis': {'range': [0, 100]}, 'bar': {'color': "#10B981" if sensors["OEE"] >= 80 else "#F59E0B"}}
             ))
             fig4.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=30, b=0))
             st.plotly_chart(fig4, use_container_width=True)
             
        with col2:
             fig5 = go.Figure()
             fig5.add_trace(go.Indicator(
                 mode="gauge+number", value=sensors["Mfg Downtime"], title={'text': "Mfg Downtime (Hours)"},
                 domain={'x': [0, 1], 'y': [0, 1]},
                 gauge={'axis': {'range': [0, 30]}, 'bar': {'color': "#F87171" if sensors["Mfg Downtime"] > 10 else "#10B981"}}
             ))
             fig5.update_layout(height=250, paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=30, b=0))
             st.plotly_chart(fig5, use_container_width=True)

    # Tab 6: Workforce Management
    with tabs[5]:
        st.markdown("<h3 style='color: #F472B6'>Workforce Management (Enable)</h3>", unsafe_allow_html=True)
        st.info(f"**FORECAST ALIGNMENT**: To meet the {demand_surge_pct:.1f}% demand surge forecasted in Demand Orchestration, plant-level labor must scale. PL-101 requires +12 headcount adjustment for upcoming shifts.")
        
        col_w1, col_w2 = st.columns(2)
        with col_w1:
            st.warning("**ALERT**: Shift Delta Team (Rocky Mount Plant) reporting consecutive high fatigue rates. Consider load-balancing incoming engineered-to-order manufacturing requests to alternate shifts.")
        with col_w2:
            st.success("**RECOMMENDATION**: Upskill training for 'Hypersteel' assembly correlates with a 15% reduction in defect rate. Action: Allocate 20 hours training for North Region distribution centers.")
        
        st.markdown("#### Workforce Filters & Analytics")
        df_wf = generate_workforce_data()
        
        col_f1, col_f2 = st.columns(2)
        shift_timing = col_f1.selectbox("Shift Timing", ["All"] + df_wf["Shift"].tolist())
        min_eff = col_f2.slider("Minimum Efficiency Rate (%)", 50, 100, 75)

        if shift_timing != "All":
            df_wf = df_wf[df_wf["Shift"] == shift_timing]
        df_wf = df_wf[df_wf["Efficiency Rate (%)"] >= min_eff]

        col_chart1, col_chart2 = st.columns(2)
        with col_chart1:
            fig_wf_pie = px.pie(df_wf, names="Shift", values="Man-Power Hours", title="Man Power Hours by Shift", hole=0.3, color_discrete_sequence=px.colors.sequential.Blues_r)
            fig_wf_pie.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_wf_pie, use_container_width=True)

        with col_chart2:
            fig_wf_bar = px.bar(df_wf, x="Shift", y=["Fatigue Rate (%)", "Workers on Leave"], title="Fatigue & Leave Trends", barmode='group', color_discrete_sequence=["#F87171", "#3B82F6"])
            fig_wf_bar.update_layout(height=300, template="plotly_white", paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)")
            st.plotly_chart(fig_wf_bar, use_container_width=True)

        st.markdown("**Core Workforce Data Tabular View**")
        st.dataframe(df_wf, use_container_width=True, hide_index=True)
