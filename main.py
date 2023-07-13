import streamlit as st
from view_projects import view_projects
from add_project import add_project


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
