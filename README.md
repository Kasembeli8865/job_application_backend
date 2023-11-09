## API DOCUMENTATION

# Authentication

## Register Employee

Registers a new employee user.

- URL: `/employees/register`
- Method: POST
- Data: 
  - `name`: Required name 
  - `email`: Required email
  - `username`: Required username
  - `password`: Required password
- Response: 201 Created with employee data on success

## Register Employer 

Registers a new employer user.

- URL: `/employers/register`
- Method: POST 
- Data:
  - `name`: Required name
  - `email`: Required email 
  - `username`: Required username
  - `password`: Required password
- Response: 201 Created with employer data on success

## Employee Login

Logs in an employee and returns a JWT access token.

- URL: `/employees/login`
- Method: POST
- Data: 
  - `email` or `username`: Required
  - `password`: Required 
- Response: 
  - 200 OK with `access_token`, `email`, `username`, `id` on success
  - 401 Unauthorized if invalid credentials

## Employer Login 

Logs in an employer and returns a JWT access token.

- URL: `/employers/login`
- Method: POST
- Data:
  - `email` or `username`: Required
  - `password`: Required
- Response:
  - 200 OK with `access_token`, `email`, `username`, `id` on success 
  - 401 Unauthorized if invalid credentials

# Employees

## Get Employees

Returns a list of all employees.

- URL: `/employees`
- Method: GET
- Response: 200 OK with list of employee objects

## Get Employee

Returns a single employee by ID.

- URL: `/employees/<id>` 
- Method: GET
- Response: 
  - 200 OK with employee data
  - 404 Not Found if no employee for given ID

## Update Employee

Updates an existing employee.

- URL: `/employees/<id>`
- Method: PATCH
- Data: Object containing any subset of employee fields to update
- Response:
  - 200 OK with updated employee data
  - 404 Not Found if no employee for given ID  

# Employers

## Get Employers

Returns a list of all employers.

- URL: `/employers`
- Method: GET
- Response: 200 OK with list of employer objects

## Get Employer 

Returns a single employer by ID.

- URL: `/employers/<id>`
- Method: GET
- Response:
  - 200 OK with employer data
  - 404 Not Found if no employer for given ID

## Update Employer

Updates an existing employer.

- URL: `/employers/<id>` 
- Method: PATCH
- Data: Object containing any subset of employer fields to update
- Response: 
  - 200 OK with updated employer data
  - 404 Not Found if no employer for given ID

# Jobs

## Get Jobs

Returns a list of all jobs.

- URL: `/jobs`
- Method: GET
- Response: 200 OK with list of job objects

## Create Job 

Creates a new job (employers only).

- URL: `/jobs`
- Method: POST 
- Headers: Authorization with JWT access token 
- Data: Job data to create 
- Response:
  - 201 Created with new job data
  - 403 Forbidden if not employer
  - 401 Unauthorized if invalid token

## Get Job

Returns a job by ID.

- URL: `/jobs/<id>`
- Method: GET
- Response: 
  - 200 OK with job data
  - 404 Not Found if invalid ID

## Update Job 

Updates an existing job (employers only).

- URL: `/jobs/<id>`
- Method: PATCH
- Headers: Authorization with JWT access token
- Data: Job data to update
- Response:
  - 200 OK with updated job  
  - 403 Forbidden if not employer
  - 401 Unauthorized if invalid token
  - 404 Not Found if invalid ID

## Delete Job

Deletes a job by ID (employers only).

- URL: `/jobs/<id>`
- Method: DELETE 
- Headers: Authorization with JWT access token
- Response:
  - 200 OK if deleted
  - 403 Forbidden if not employer
  - 401 Unauthorized if invalid token
  - 404 Not Found if invalid ID

# Ratings

## Get Ratings

Returns all ratings.

- URL: `/ratings`
- Method: GET
- Response: 200 OK with list of rating objects

## Create Rating

Creates a new rating.

- URL: `/ratings`
- Method: POST
- Data: Rating data to create
- Response: 201 Created with new rating object

## Get Rating

Returns a rating by ID.

- URL: `/ratings/<id>`
- Method: GET 
- Response:
  - 200 OK with rating data
  - 404 Not Found if invalid ID

## Update Rating

Updates an existing rating.

- URL: `/ratings/<id>`
- Method: PATCH  
- Data: Rating data to update
- Response:
  - 200 OK with updated rating
  - 404 Not Found if invalid ID

## Delete Rating

Deletes a rating by ID.

- URL: `/ratings/<id>`
- Method: DELETE
- Response:
  - 200 OK if deleted
  - 404 Not Found if invalid ID


