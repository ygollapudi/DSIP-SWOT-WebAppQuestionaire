import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.title("SWOT Factor Questionaire")
st.markdown("Please answer the following questions about your EDD")


conn = st.connection("gsheets", type=GSheetsConnection)

existing_data = conn.read(worksheet="Sheet1", usecols=list(range(19)))

with st.form(key="SWOT_Questionaire"):
    EDD = st.text_input(label="Name of EDD/Region*")
    Key_Economic_Factors = st.text_input(label="What are the key industries, assets, and resources that drive your region’s economy?")
    Key_Educational_Infrastructure = st.text_input(label="Which educational, training, or workforce programs most effectively support economic growth?")
    Key_Connectivity_Infrastructure = st.text_input(label="What infrastructure systems (transportation, broadband, utilities, healthcare, etc.) are major strengths for your region?")
    Major_Geographic_Factors = st.text_input(label="What cultural, natural, or historical assets enhance the region’s attractiveness and identity?")
    Key_Partnerships = st.text_input(label="How do partnerships, collaborations, or civic leadership contribute to regional success?")
    Major_Economic_Limiting_Factors = st.text_input(label="What major gaps or barriers exist that limit economic or community development?")
    Underperforming_Infrastructure = st.text_input(label="Where are infrastructure, services, or facilities underperforming or insufficient?")
    Workforce_Challenges = st.text_input(label="What workforce challenges (skills gaps, demographic trends, labor shortages) impact the region?")
    Key_Orginizational_Challenges = st.text_input(label="What political, regulatory, or organizational issues inhibit progress or create obstacles for growth?")
    Potential_Engagement_Factors = st.text_input(label="Where could collaboration, engagement, or leadership capacity be improved across the region?")
    Key_Emerging_Industries = st.text_input(label="What emerging industries, technologies, or trends offer potential for future growth?")
    Major_Underused_Assets = st.text_input(label="What underused assets (land, buildings, skills, institutions) could be better leveraged for economic development?")
    Key_Innovative_Sectors = st.text_input(label="How can tourism, entrepreneurship, housing, or innovation sectors be expanded or enhanced?")
    Key_Funding_Opportunities = st.text_input(label="What funding sources, grant opportunities, or partnerships could support new initiatives?")
    Potential_Disruption_Prevention = st.text_input(label="How can the region build greater resilience against future disruptions or market shifts?")
    Major_External_Risks = st.text_input(label="What external risks (economic, environmental, demographic, or competitive) could negatively impact the region’s growth?")
    Potential_Changes_to_Key_Industries = st.text_input(label="How might changes in key industries, funding streams, or policies affect the region’s stability and prosperity?")
    Key_Branding_Opportunities = st.text_input(label="What reputational, branding, or marketing challenges could limit the region’s ability to attract investment and talent?")

    st.markdown("**required*")

    submit_button = st.form_submit_button(label = "Submit")

    if submit_button:
        if not EDD:
            st.warning("Ensure all mandatory fields are filled.")
            st.stop()
        else:
            questionaire_data = pd.DataFrame([{"EDD":EDD, 
                                               "Key_Economic_Factors":Key_Economic_Factors, 
                                               "Key_Educational_Infrastructure":Key_Educational_Infrastructure, 
                                               "Key_Connectivity_Infrastructure":Key_Connectivity_Infrastructure, 
                                               "Major_Geographic_Factors":Major_Geographic_Factors, 
                                               "Key_Partnerships":Key_Partnerships, 
                                               "Major_Economic_Limiting_Factors":Major_Economic_Limiting_Factors, 
                                               "Underperforming_Infrastructure":Underperforming_Infrastructure, 
                                               "Workforce_Challenges":Workforce_Challenges, 
                                               "Key_Orginizational_Challenges":Key_Orginizational_Challenges, 
                                               "Potential_Engagement_Factors":Potential_Engagement_Factors, 
                                               "Key_Emerging_Industries":Key_Emerging_Industries,
                                               "Major_Underused_Assets":Major_Underused_Assets,
                                               "Key_Innovative_Sectors":Key_Innovative_Sectors,
                                               "Key_Funding_Opportunities":Key_Funding_Opportunities,
                                               "Potential_Disruption_Prevention":Potential_Disruption_Prevention,
                                               "Major_External_Risks":Major_External_Risks,
                                               "Potential_Changes_to_Key_Industries":Potential_Changes_to_Key_Industries,
                                               "Key_Branding_Opportunities":Key_Branding_Opportunities}])
            

            df_updated = pd.concat([existing_data, questionaire_data], ignore_index = True)

            conn.update(worksheet = "Sheet1", data = df_updated)

            st.success("EDD Information Has Successfully Been Submitted")
