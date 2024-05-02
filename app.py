import streamlit as st
from agents.opener_agent import setup_opener_chain
from agents.escalator_agent import setup_escalator_chain

# Title of the application
st.title('AI Email Generator')

# Navigation bar setup
option = st.sidebar.selectbox(
    'Choose the agent:',
    ('Opener Agent', 'Escalator Agent')
)

# Processing for the Opener Agent
if option == 'Opener Agent':
    chain = setup_opener_chain()
    lead_name = st.text_input("Lead Name", "John Doe")
    lead_role = st.text_input("Lead Role", "Project Manager")
    lead_company_name = st.text_input("Company Name", "Example Corp")
    industry = st.text_input("Industry", "Technology")
    lead_company_information = st.text_area("Company Information", "Example Corp is a leading provider in the tech industry known for its innovative solutions.")
    
    if st.button('Generate Email with Opener Agent'):
        # Assuming 'predict' method accepts these as arguments and returns JSON
        email = chain.predict(
            lead_name=lead_name, 
            lead_role=lead_role, 
            lead_company_name=lead_company_name,
            industry=industry, 
            lead_company_information=lead_company_information
        )
        st.write(email)

# Processing for the Escalator Agent
elif option == 'Escalator Agent':
    chain = setup_escalator_chain()
    lead_name = st.text_input("Lead Name", "Jane Smith")
    lead_role = st.text_input("Lead Role", "Director")
    lead_company_name = st.text_input("Company Name", "Global Tech")
    lead_company_information = st.text_area("Company Information", "Global Tech specializes in high-tech innovations and solutions.")
    project_title = st.text_input("Project Title", "Innovate AI")
    department = st.text_input("Department", "Research and Development")
    looking_for = st.text_area("Project Scope", "Looking to develop an AI-driven solution to optimize our operations.")
    lead_response = st.text_area("Lead Response", "Thanks for reaching out. Please provide more details.")

    if st.button('Generate Email with Escalator Agent'):
        # Assuming 'predict' method accepts these as arguments and returns JSON
        email = chain.predict(
            lead_name=lead_name, 
            lead_role=lead_role, 
            lead_company_name=lead_company_name, 
            lead_company_information=lead_company_information,
            project_title=project_title, 
            department=department,
            looking_for=looking_for, 
            lead_response=lead_response
        )
        st.write(email)

