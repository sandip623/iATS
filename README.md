# iNTEGRATED APPLICATION TRACKING SYSTEM

- ats api integration x different sources | need to generate csv files as such APIs are not generally provisioned for applicants perspective | 2 dummy datasets created representing job application data with small variance in the field settings

- data class normalisation for consistencies | include data classes for users, applicant data

- login authentication 

- client/server rest api functionality
mvc framework but server-side (flask) only for model/controllers, as views will be client-side (react)
flask blueprints for modularising api paths

# git caching issue
git rm -r --cached .
git add .
git commit -m "Fixed gitignore"

# git branch
git checkout -b new_branch_name
git push origin branch_name