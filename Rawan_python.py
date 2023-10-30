import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import altair as alt
import sqlite3


def main():
    df = pd.read_csv('Employee_Salary.csv')

    salaries = ['Years', 'Salary']
    menu = ["Home", "Advanced Analytics", "SQL Database", "About"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        st.subheader("Employee Salaries App")
        st.caption("This app offers powerful analytics for Human Resources, leveraging a SQL database for insightful data.")

        st.image("https://lewishamtalkingtherapies.nhs.uk/wp-content/uploads/2023/10/iStock-1409637645-1536x1024.jpg", width=450)

        st.subheader("Employee Authorization")
        st.caption("Due to the sensitive nature of the data, access is restricted to authorized HR personnel only")
        authorized_employee = ['Rawan', 'Mike', 'Concepcion Diaz']

        if st.button("Check Authorization"):
            employee_name = st.text_input("Enter Employee Name")

            if employee_name in authorized_employee:
                st.success("Employee is authorized!")
            else:
                st.error("Employee is not authorized!")

        st.markdown('---')



    elif choice == "Advanced Analytics":
        st.header('Human Resource - Advanced Analytics')
        st.caption('Explore comprehensive analytics showcasing the relationship between employees salaries and their years of experience.')
        data = pd.read_csv('Employee_Salary.csv')
        st.markdown('-----')
        st.write('1. Get a comprehensive overview of the dataset, including essential columns')
        st.dataframe(data.head(5))

        st.markdown('---')

        st.write('2. Explore the data types present in the dataset, providing valuable insights into the structure and format of the data')
        data_types = df.dtypes
        st.write(data_types)

        st.markdown('---')

        st.subheader('The Distribution of Years of Experience in The Organization')
        fig = px.histogram(df, x='Years', nbins=10)
        st.plotly_chart(fig)

        st.markdown('----')
        st.subheader('The Distribution of Salaries in The Organization - Yearly - ')

        fig = px.histogram(df, x='Salary', nbins=5)
        st.plotly_chart(fig)

        st.markdown('-----')
        st.subheader('The Relationship Between Years of Experience and Salary')
        fig = px.scatter(data_frame=df, x='Years', y='Salary')
        st.plotly_chart(fig)

        st.markdown('-----')
        st.subheader('Main findings from Data Analytics')
        st.write('1. There is a positive correlation between years of experience and salary, indicating that as experience increases, so does the salary.')
        st.write('2. The distribution of salaries reveals that the average salary amount is around 100K.')
        st.write('3. The organization typically has employees with an average range of 9 to 11 years of experience.')

        st.markdown("------")



        
    elif choice == "SQL Database":
        conn = sqlite3.connect('data/data.sqlite')
        c = conn.cursor()


        def sql_executor(raw_code):
        	c.execute(raw_code)
        	data = c.fetchall()
        	return data 

        salaries = ['Years', 'Salary']

        st.title("Database Results")
        col1, col2 = st.columns(2)

        with col1:
            with st.form(key='query_form'):
                raw_code = st.text_area("SQL Code Here")
                submit_code = st.form_submit_button("Execute")

            with st.expander("Table Info"):
                table_info = {'salaries':salaries}

        with col2:
            if submit_code:
                st.info("Query Submitted")
                st.code(raw_code)

                query_results = sql_executor(raw_code)
                with st.expander("Results"):
                    st.write(query_results)

                with st.expander("Database"):
                    query_df = pd.DataFrame(query_results)
                    st.dataframe(query_df)

    elif choice == "About":
        st.title("About")
        st.write("This app is designed for Python Analysis 2 at IE University, providing powerful tools and analytics for data exploration and visualization.")
        st.caption("#### It is developed by Rawan Alhosayen, a student in Section 2 of the Master's program in Business Analytics and Big Data.")
if __name__ == '__main__':
    main()