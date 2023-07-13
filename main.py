import streamlit as st
import pandas as pd

# Create a DataFrame to store the projects
projects_df = pd.DataFrame(columns=['Project Name', 'Type', 'City', 'Branch', 'Start Date', 'End Date',
                                    'Positioning', 'Target Audience', 'Coverage Plan', 'Coverage Fact',
                                    'Budget', 'Contract Number', 'Payment Number', 'Partner Company',
                                    'KPI1', 'KPI2', 'KPI3', 'Uniqueness'])

# Define the project types and their corresponding fields
project_types = {
    'Event': ['City', 'Branch', 'Start Date', 'End Date', 'Positioning', 'Target Audience', 'Coverage Plan',
              'Coverage Fact', 'Budget', 'Contract Number', 'Payment Number', 'Partner Company', 'KPI1', 'KPI2', 'KPI3',
              'Uniqueness'],
    'Film': ['City', 'Positioning', 'Target Audience', 'Release Date', 'Uniqueness', 'Coverage Plan', 'Coverage Fact',
             'Budget', 'Contract Number', 'Payment Number', 'Partner Company', 'KPI Transitions', 'KPI Installations',
             'KPI Number of Comments', 'KPI Views', 'KPI Number of Auditions'],
    'Space': ['City', 'Branch', 'Start Date', 'End Date', 'Positioning', 'Target Audience', 'Coverage Plan',
              'Coverage Fact', 'Budget', 'Contract Number', 'Payment Number', 'Partner Company', 'KPI Number and Transaction Amounts',
              'Uniqueness'],
    'Special project': ['City', 'Branch', 'Collage', 'Platform', 'Start Date', 'End Date', 'Positioning',
                        'Target Audience', 'Coverage Plan', 'Coverage Fact', 'Budget', 'Contract Number',
                        'Payment Number', 'Partner Company', 'KPI1', 'KPI2', 'KPI3', 'Uniqueness',
                        'KPI Transitions', 'KPI Installations', 'KPI Number of Comments', 'KPI Views',
                        'KPI Number of Listens'],
    'BTL': ['City', 'Branch', 'Start Date', 'End Date', 'Positioning', 'Target Audience', 'Coverage Plan',
            'Coverage Fact', 'Budget', 'Contract Number', 'Payment Number', 'Partner Company', 'KPI1', 'KPI2', 'KPI3',
            'Uniqueness']
}

# Page for viewing projects
def view_projects():
    st.title('Project Showcase')

    if projects_df.empty:
        st.info('No projects found.')
    else:
        for index, project in projects_df.iterrows():
            st.subheader(project['Project Name'])
            st.write('Type:', project['Type'])
            st.write('City:', project['City'])
            st.write('Branch:', project['Branch'])
            st.write('Start Date:', project['Start Date'])
            st.write('End Date:', project['End Date'])

            if project['Type'] in project_types:
                fields = project_types[project['Type']]
                for field in fields:
                    st.write(field + ':', project[field])

            st.markdown('---')

# Page for adding a project
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

# Main application
def main():
    st.sidebar.title('Project Management')
    page_options = ['View Projects', 'Add Project']
    page = st.sidebar.radio('Navigation', page_options)

    if page == 'View Projects':
        view_projects()
    elif page == 'Add Project':
        add_project()


if __name__ == '__main__':
    main()