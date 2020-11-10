-- CREATE DEPARTMENT TABLE:
create table departments (
    dept_no VARCHAR(100) not NULL,
    dept_name VARCHAR(100) not NULL,
    constraint pk_departments primary key (
        dept_no
     )
);

select * from departments;

-- CREATE DEPT_EMP TABLE:
create table dept_emp (
    emp_no INT not NULL,
    dept_no VARCHAR(100) not NULL
);

select * from dept_emp;

-- CREATE DEPT_MANAGER TABLE:
create table dept_manager (
    dept_no VARCHAR(100) not NULL,
    emp_no INT not NULL
);

select * from dept_manager;

-- CREATE EMPLOYEES TABLE:
create table employees (
    emp_no INT not NULL,
    emp_title_id VARCHAR(100) not NULL,
    birth_date DATE not NULL,
    first_name VARCHAR(255) not NULL,
    last_name VARCHAR(255) not NULL,
    sex VARCHAR(20) not NULL,
    hire_date DATE not NULL,
    constraint pk_employees primary key (
        emp_no
     )
);

select * from employees;

-- CREATE SALARIES TABLE:
create table salaries (
    emp_no INT not NULL primary key,
    salary INT not NULL
);

select * from salaries;

-- CREATE TITLES TABLE:
create table titles (
    title_id VARCHAR(100) not NULL,
    title VARCHAR(100) not NULL,
    constraint pk_titles primary key (
        title_id
     )
);

select * from titles;

-- ALTER TABLES TO INCLUDE FORIEGN KEYS:
alter table dept_emp add constraint fk_dept_emp_emp_no foreign key(emp_no)
references employees (emp_no);

alter table dept_emp add constraint fk_dept_emp_dept_no foreign key(dept_no)
references departments (dept_no);

alter table dept_manager add constraint fk_dept_manager_dept_no foreign key(dept_no)
references departments (dept_no);

alter table employees add constraint fk_employees_emp_title_id foreign key(emp_title_id)
references titles (title_id);

alter table salaries add constraint fk_salaries_emp_no foreign key(emp_no)
references employees (emp_no);

-- alter table dept_manager add constraint fk_dept_manager_emp_no foreign key(emp_no)
-- references dept_emp (emp_no);