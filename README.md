+ Integrated Application Tracking System

+ Job seekers who want to track applications across multiple platforms. Professionals looking for a modern and efficient way to manage their job applications. 


![Alt text](iATS%20erd.jpg)
NB: for the purpose of this project, we are to focus on the Users and Applications entities, therefore the database will be seedcoded accordingly (i.e., additional entity such as Company may not be included)

-----------------------------------------

DEV NOTES (can be ignored by reader)

- ats api integration x different sources | need to generate csv files as such APIs are not generally provisioned for applicants perspective | 2 dummy datasets created representing job application data with small variance in the field settings


- data class normalisation for consistencies | include data classes for users, applicant data
i.e., in "/models/users.py"

- database partitioning: 
Due to projected growth of data i.e., for Affiliations table; better to partition into multiple tables based on users and based on record limit for 'optimal' performance

- use of ORM (object relational mapping) i.e., ../iats-server/dbutils/mysqlcls.py for streamlining database object management through the program.

- login authentication 
+ flask part:
(prior to applications table seeding as users.userid required as foreign key)

+ react part:
npm install react-router-dom
RegistrationForm.jsx 


- client/server rest api functionality
mvc framework but server-side (flask) only for model/controllers, as views will be client-side (react)
flask blueprints for modularising api paths, i.e., 'registration.py' for handling registration related api component

# git caching issue
git rm -r --cached .
git add .
git commit -m "Fixed gitignore"

# git branch
git checkout -b new_branch_name
git push origin branch_name
