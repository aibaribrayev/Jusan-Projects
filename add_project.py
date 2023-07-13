import streamlit as st
from data import projects_df, project_types


def add_project():
    st.title('Add Project')
    project_name = st.text_input('Project Name')
    project_type = st.selectbox('Type', list(project_types.keys()), index=0)

    if project_type in project_types:
        fields = project_types[project_type]
        with st.expander('Project Details', expanded=True):
            for field in fields:
                if field == 'City':
                    project_city = st.text_input('City')
                elif field == 'Branch':
                    project_branch = st.text_input('Branch')
                elif field == 'Start Date':
                    project_start_date = st.date_input('Start Date')
                elif field == 'End Date':
                    project_end_date = st.date_input('End Date')
                elif field == 'Positioning':
                    positioning_options = ['Creative', 'Smart', 'Eco-friendly', 'Sporty', 'Kind']
                    project_positioning = st.selectbox('Positioning', positioning_options)
                elif field == 'Target Audience':
                    audience_options = ['Children under 10 years old', 'Teenagers 11-16 years old', 'Youth 17-25 years old',
                                        'Adults 26-45', 'Average age 46-59', 'Elderly people 60+']
                    project_target_audience = st.selectbox('Target Audience', audience_options)
                elif field == 'Coverage Plan':
                    project_coverage_plan = st.text_input('Coverage Plan')
                elif field == 'Coverage Fact':
                    project_coverage_fact = st.text_input('Coverage Fact')
                elif field == 'Budget':
                    project_budget = st.text_input('Budget')
                elif field == 'Contract Number':
                    project_contract_number = st.text_input('Contract Number')
                elif field == 'Payment Number':
                    project_payment_number = st.text_input('Payment Number')
                elif field == 'Partner Company':
                    project_partner_company = st.text_input('Partner Company')
                elif field.startswith('KPI'):
                    project_kpi = st.text_input(field)
                elif field == 'Uniqueness':
                    project_uniqueness = st.text_input('Uniqueness')

        if st.button('Add'):
            # Create a dictionary to store the project details
            project_details = {
                'Project Name': project_name,
                'Type': project_type,
                'City': project_city,
                'Branch': project_branch,
                'Start Date': project_start_date,
                'End Date': project_end_date,
                'Positioning': project_positioning,
                'Target Audience': project_target_audience,
                'Coverage Plan': project_coverage_plan,
                'Coverage Fact': project_coverage_fact,
                'Budget': project_budget,
                'Contract Number': project_contract_number,
                'Payment Number': project_payment_number,
                'Partner Company': project_partner_company,
                'KPI1': project_kpi,
                'KPI2': project_kpi,
                'KPI3': project_kpi,
                'Uniqueness': project_uniqueness
            }

            # Add the project details to the DataFrame
            projects_df.loc[len(projects_df)] = project_details
            st.success('Project added successfully!')
