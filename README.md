# Issue Tracking RESTful API

## Table Of Contents

- [Preamble](#preamble)
- [About the project](#about-the-project)
  - [Project context](#project-context)
  - [About the API](#about-the-api)
    - [Resources](#resources)
    - [Permissions](#permissions)
  - [API Endpoints](#api-endpoints)
  - [About the project design and compliance](#about-the-project-design-and-compliance)
- [Technology](#technology)
- [Installation](#installation)
    
## Preamble
This website was designed for a school project with specific requirements and fixed constraints.
It was developed in a limited period of time and in this context this project is not intended
to evolve that much once finished. This project is not open to contribution.
The following need is fictive.

## About the project

<img src="https://github.com/nanakin/OC-P10-DRF/assets/14202917/e7a9510f-6e29-40d2-9024-31a1c5a6371e" alt="SoftDesk logo" width=100>

### Project context
SoftDesk, a software publishing company, decided to develop an application to **report and track technical problems**.
I was hired as a software engineer to create an efficient and secure back-end to serve front-end applications on different platforms, using a **RESTful API** for their communications.

### About the API

#### Resources
The API provides the following resources :
- Users:
  - Username, password, birthdate, RGPD data.
- Contributors:
  - User-project association.
- Projects:
  - Title, description, type of project, list of contributors.
- Issues (related to a project):
  - Title, description, assignment to a contributor, priority, type of issue, status of progression.
- Comments (related to an issue):
  - Description.

#### Permissions
The API **allows**:
- Unauthenticated users to: 
   - create users.
- Authenticated users to:
  - modify or delete their user profile,
  - create projects,
  - add contributors to their created projects,
  - delete added contributors,
  - modify and delete their created projects.
- Authenticated contributors to:
  - add contributors to collaborating projects,
  - delete added contributors,
  - create issues and comments to collaborating projects,
  - read access to projects details, issues and comments from collaborating projects,
  - modify and delete their posted issues and comments.
  
Note : The API uses bearer authentication (token) as HTTP authentication scheme.

### API Endpoints
The API exposes the following URLs:
- Users
  - http://localhost:8000/api/users/ POST and GET
  - http://localhost:8000/api/users/<user_pk> GET, PATCH, PUT, DELETE
  - http://localhost:8000/api/users/<user_pk>/change_password/ POST
- Projects
  - http://localhost:8000/api/projects/ POST and GET
  - http://localhost:8000/api/projects/<project_pk> GET, PATCH, PUT, DELETE
- Contributors 
  - http://localhost:8000/api/contributors/ POST and GET
  - http://localhost:8000/api/contributors/<user_pk> GET, DELETE
- Issues
  - http://localhost:8000/api/issues/ POST and GET
  - http://localhost:8000/api/issues/<issue_pk> GET, PATCH, PUT, DELETE
- Comments
  - http://localhost:8000/api/comments/ POST and GET
  - http://localhost:8000/api/comments/<comment_pk> GET, PATCH, PUT, DELETE
- Authentication
  - http://localhost:8000/api/token/ POST
  - http://localhost:8000/api/token/resfresh POST
  
Where `<resourcename_pk>` is the primary key (often an id) of the database entry.

### About the project design and compliance
The back-end : 
- is a REST API 
- is [GDPR](https://gdpr.eu/) (General Data Protection Regulation) compliant
- is optimized (using pagination and method adapted serializers)
- is secure (using token authentication and custom permissions)

The python code:
- is following Django's best practices,
- is [PEP8](https://peps.python.org/pep-0008/) compliant ([flake8](https://pypi.org/project/flake8/) valid),
- is [Black](https://pypi.org/project/black/) formatted.

## Technology

This application was tested with [python](https://www.python.org/) `3.11`  and [poetry](https://python-poetry.org/) `1.5` (for the virtual environnement and dependencies).
### Projects dependencies:
<img src="https://github.com/nanakin/OC-P10-DRF/assets/14202917/9b540a1a-68de-428f-af1e-f7a911412f86" alt="DRF" width="150"/>

- [Django REST Framework](https://www.django-rest-framework.org/) (`djangorestframework` 3.14).

- [Simple JWT](https://pypi.org/project/djangorestframework-simplejwt) (`djangorestframework-simplejwt` 5.3)

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/nanakin/OC-P10-DRF.git DRF-project
   ```
2. Move to the project directory:   
   ```sh
   cd DRF-project
   ```
3. Install dependencies in a new virtual environment:
   ```sh
   poetry install
   ```
   and use it:
   ```sh
   poetry shell
   ```
4. Migrate the database
   ```sh
   python3 manage.py migrate
   ```
5. Launch the server:
   ```sh
   python3 manage.py runserver
   ```
6. Start using API [endpoints](#api-endpoints) `http://localhost:8000/api/...`
