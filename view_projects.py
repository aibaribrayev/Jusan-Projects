import streamlit as st
from data import projects_df, project_types


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
