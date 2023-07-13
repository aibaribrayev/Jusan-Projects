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
