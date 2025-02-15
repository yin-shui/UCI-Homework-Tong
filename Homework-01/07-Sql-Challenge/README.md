# SQL Challenge - Employee Database: A Mystery in Two Parts

In this challenge, I will design tables to hold data of employees of a corporation from the 1980s and 1990s in the CSV form, importing the CSVs into a SQL database, and answer questions about the data. In other words, I will perform:

1. Data Engineering

3. Data Analysis

#### Data Engineering

* Using the information I have to create a table schema for each of the six CSV files. Specifying data types, primary keys, foreign keys, and other constraints.

  * For the primary keys check to see if the column is unique, otherwise create a [composite key](https://en.wikipedia.org/wiki/Compound_key). Which takes to primary keys in order to uniquely identify a row.
  * Being sure to create tables in the correct order to handle foreign keys.

* Importing each CSV file into the corresponding SQL table. 

#### Data Analysis

Once I have a complete database, do the following:

1. List the following details of each employee: employee number, last name, first name, sex, and salary.

2. List first name, last name, and hire date for employees who were hired in 1986.

3. List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name.

4. List the department of each employee with the following information: employee number, last name, first name, and department name.

5. List first name, last name, and sex for employees whose first name is "Hercules" and last names begin with "B."

6. List all employees in the Sales department, including their employee number, last name, first name, and department name.

7. List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.

8. In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.





