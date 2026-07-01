# Cyber Check - IP Checker

Code and Documentation for Cyber Check Web Application. Created by Joe Petzold.

## App URL

[Click here for the live version of the application.](https://jp3379a-nulondon.github.io/Cyber-IP-Checker/)


<details>

<summary><h2>Introduction</h2></summary>

### Proposal

This project proposes the development of a cyber security web application that allows users to submit an IP (Internet Protocol) address through a web interface. The IP address is sent to a backend server, checked against an external reputation API, and the results are returned to the user in a clear and user friendly format.

### Purpose

The purpose of the application is to provide security analysts with a single interface for checking the reputation of IP addresses. The application will present the results in a simple and user friendly way, supporting quicker triage, clearer interpretation of reputation data, and better decision making during security investigations.

### Business Requirement – Benefit Realisation

The business requirement is to reduce the need for analysts to manually check multiple external platforms when investigating suspicious IP addresses. A centralised IP reputation checker improves operational efficiency by reducing investigation time, supporting consistent reporting, and allowing analysts to focus more on analysis and response actions.

If the MVP (Minimum Viable Product) is successful, the application could be expanded to include multiple threat intelligence sources, providing a more complete risk profile for each IP address. This would support faster incident response and reduce cognitive load on the security team when dealing with potential threats.

### Feasibility

The TELOS framework has been applied to this project to understand how feasible the project is. 
| Feasibility Area | Assessment |
|---|---|
| **Technical Feasibility** | The project is technically viable using a Python backend, such as Flask or FastAPI, with a lightweight frontend. The Virus Total REST API provides structured JSON responses that can be parsed and displayed in a custom user interface. Additional APIs, such as AbuseIPDB or Shodan, could be integrated later using a modular API design. Hosting can be provided via free online tools like Render.com, but this could be improved through internal infrastructure or cloud platforms such as Microsoft Azure. |
| **Economic Feasibility** | The MVP has minimal costs, mainly involving development time and any potential API rate limits or subscription requirements for Virus Total. Expanding the system to include multiple APIs may introduce licensing costs, but these could be justified by reducing analyst workload and improving investigation speed. |
| **Legal Feasibility** | The system must comply with API terms of service, including Virus Total data usage restrictions, as well as organisational data handling policies. Although no personal data is processed, logs may contain sensitive security intelligence and should therefore be securely stored with appropriate access control. |
| **Operational Feasibility** | The tool aligns with security workflows and requires minimal training due to its simple IP input and results output design. It can support existing investigation processes. |
| **Schedule Feasibility** | An MVP can be delivered within a short development cycle, focusing on core API integration, a basic user interface, and clear response display. Future iterations could expand API coverage and introduce dashboard functionality. |

***Table 1** – TELOS framework analysis.*

Using the TELOS framework, the project can be considered feasible. Developing the MVP requires technical implementation which the development team possess, as they have the necessary skills to build the MVP using suitable web technologies. The project is also economically viable because it is small in scope and is expected to involve limited development costs, while still addressing the user’s need for a centralised IP reputation checking tool. The project is achievable within a short development timeframe and provides a practical foundation for future expansion if the MVP proves successful.

</details>


<details>

<summary><h2>Design and Prototyping</h2></summary>

### Requirements
The IP Checker is designed to be a user friendly and intuitive web application. It contains minimal pages, making navigation simple and easy to follow. Users access the application through a homepage, where they are presented with an input box and clear instructions. Once an IP address is submitted, the results are clearly displayed. If an error occurs, a constructive error message is shown, suggesting the potential issue that has caused the error.

### Functional Requirements

| ID | Functional Requirement | Description |
|---|---|---|
| FR1 | IP Address Input | The application must allow users to enter an IP address into an input field. |
| FR2 | Input Validation | The application must check that the input field is not empty before submitting the request. |
| FR3 | API Request | The application must send the entered IP address to a backend server to make the API call for reputation checking. |
| FR4 | Reputation Results | The application must display the IP reputation results returned from the API, including malicious and suspicious results. |
| FR5 | Visual Results Display | The application must present the results in a clear visual format, such as percentage bars, to make the output easier to understand. |
| FR6 | Error Handling | The application must display an error message if the IP address cannot be checked or if the backend server/API returns an error. |
| FR7 | Homepage Navigation | The application should allow users to return to the homepage by clicking the Cyber Check logo. |

***Table 2** – Key Functional Requirements of the IP Checker MVP.*

### Non-Functional Requirements

| ID | Non-Functional Requirement | Description |
|---|---|---|
| NFR1 | Usability | The application should be simple and easy to use, allowing users to check an IP address without needing detailed instructions. |
| NFR2 | Performance | The application should return results quickly enough to support efficient security investigation and triage. |
| NFR3 | Reliability | The application should handle API or server errors gracefully and provide clear feedback to the user. |
| NFR4 | Security | The Virus Total API key must not be exposed in the frontend JavaScript or Python code and should be stored securely in the backend environment. |
| NFR5 | Maintainability | The code should be clearly structured so future APIs, such as AbuseIPDB or Shodan, can be added easily. |
| NFR6 | Compatibility | The application should work correctly in modern web browsers when accessed through the deployed frontend. |
| NFR7 | Accessibility | The interface should use clear text, readable colours, and a simple layout to support ease of use. |

***Table 3** – Key Non-Functional Requirements of the IP Checker MVP.*

### User Persona

![Proto-Persona User Card](https://github.com/user-attachments/assets/2100fe4a-2210-4b82-8f9b-ae038744df46)

***Figure 1**: Proto-persona card of a likely user.*

### Figma Design
Based on the proto-persona card shown in Figure 1, the design is aimed at users who are interested in, or work within, the cyber security field. Therefore, the web application adopts a cyber/futuristic theme that is visually engaging and appealing to this audience, while remaining simple, clear, and not overly cluttered or confusing. The design also maintains a professional tone, as the application produces results that may identify potentially malicious IP addresses. The following designs are created based on these highlighted design considerations.

#### Low Fidelity design
![Lo-Fi MVP design](https://github.com/user-attachments/assets/d237200f-371e-44de-bd88-5ba1386073ea)

***Figure 2**: Low Fidelity design of the MVP IP checker.*

**[Click here for a full Figma prototype](https://www.figma.com/proto/z22xMGlc1B1KgzUcfBqSaS/Software-Engineering-Year-3?node-id=0-1&t=xXiWXE5LrOzMTkP3-1)**

#### High Fidelity design
![Hi-Fi MVP design](https://github.com/user-attachments/assets/dec8213a-316c-431a-977c-d71595982768)

***Figure 3**: High Fidelity design of the homepage MVP IP checker.*

</details>


<details>

<summary><h2>Project Management</h2></summary>

### Management Structure
The IP Checker project adopts an agile style approach. It follows a typical software development lifecycle, including feasibility analysis, requirements analysis, planning, design, development, testing, and deployment. This initial project represents the first iteration of the product’s lifecycle and is delivered across three sprints. The first sprint focuses on planning and design activities, the second sprint concentrates on development and testing, and the third sprint involves deploying the completed minimum viable product (MVP) to GitHub alongside the required project documentation. If further development is required, the project can be extended into a continuous agile development cycle, allowing additional iterations, refinements, and feature enhancements to be implemented over time.
New features are managed through a structured GitHub workflow, supported by integration between Visual Studio Code and the GitHub repository. Updated code and functionality are developed locally in Visual Studio Code before being pushed to GitHub through pull requests. Each new feature is created within a dedicated feature branch, which is then merged into the development branch for review and testing. Once the changes are checked and approved, they are merged into the main branch to form part of the stable version of the project. This approach supports version control, collaboration, and a clear audit trail of development activity.


### Kanban board – GitHub Projects

![Kanban board start](https://github.com/user-attachments/assets/d9088470-eae0-499f-945c-abe75f42da71)
***Figure 4**: The project Kanban board at the earlier stages of the development lifecycle.* 

![Kanban board middle](https://github.com/user-attachments/assets/ccd4f06a-2786-463a-954d-ac34bc6fe253)
***Figure 5**: The project Kanban board at a middle point of the development lifecycle.*

GitHub Projects is used to manage the project through an agile workflow, where tasks or issues are converted into tickets and tracked across a Kanban style board. This supports structured planning by making each task visible and allowing dependencies between issues to be identified. For example, if one issue needs to be completed before another can begin, this can be recognised early and prioritised appropriately.
The work is organised into sprints, which allows the overall project to be divided into smaller, more manageable sections. This approach supports incremental progress and that key activities are completed in a logical order. The GitHub Projects board is organised using columns **Backlog**, **In Progress**, **In Review**, and **Done**, enabling progress to be monitored throughout the development lifecycle. This provides a clear structure for managing requirements, tracking development activity, and makes sure that each stage of the project is completed in a controlled and transparent manner.

### Labelling

![Project labels](https://github.com/user-attachments/assets/314780cd-b60f-41d9-bd02-0b8332563d57)
***Figure 6**: The project labels that are used to assign to issues.*

Custom labels are used to categorise issues and improve the organisation of the GitHub Projects board. Labels such as **planning**, **feasibility**, **requirements**, **design**, **testing**, **development** and **deployment** make it easier to identify the purpose of each issue and understand which part of the project it relates to. Labelling supports filtering and prioritisation, as specific types of work can be grouped together and reviewed more efficiently during each sprint. 

### Issues

![Project issues](https://github.com/user-attachments/assets/c9469fbc-ced3-41b3-a105-bee74c61e488)
***Figure 7**: The project issues are created and placed on the Kanban board.*

GitHub issues are used and created at the start of the project and added to the backlog to support planning and task management. These issues cover key project activities, including design, development, testing, deployment and documentation. Each issue represents a specific task, bug, or improvement, making the workload easier to organise.
Issues can be created at any time during the project to address new problems, such as coding errors or design changes. Issues are linked to branches and pull requests, creating traceability between the task and code changes. This supports version control and a structured development workflow.

</details>



<details>

<summary><h2>Coding Journey</h2></summary>

### Coding Process
The coding process is managed through GitHub Issues and the project Kanban board. Each issue represents a specific development task, allowing the coding journey to be tracked in a clear and structured way. This supports an incremental development approach, where the IP Checker is built in stages rather than all at once. The process begins with the frontend structure and styling, before moving on to JavaScript functionality, testing, backend Python development, and final deployment. This allows each part of the MVP to be developed, tested, reviewed, and improved throughout the project lifecycle.
Table 4 outlines the main stages of the coding process:
| Stage | Development Task | Description |
|---|---|---|
| 1 | Create HTML homepage | Build the main landing page for the IP Checker web application. |
| 2 | Add CSS styling for homepage | Create reusable styling for text, buttons, layout, and visual consistency. |
| 3 | Create HTML IP input page | Develop the page where users enter an IP address for reputation checking. |
| 4 | Adjust CSS for input page | Refine the input page styling with consistency with the homepage design. |
| 5 | Create JavaScript tests | Test key JavaScript functionality, such as capturing and handling the inputted IP address. |
| 6 | Develop JavaScript functionality | Add client side logic to process user input and support interaction with the application. |
| 7 | Create Python tests | Test backend requirements, including smoke testing, IP validation, and result output validation. |
| 8 | Develop Python backend | Build and test the backend code required to process IP reputation checks. |
| 9 | Deploy application | Deploy the completed MVP using Render.com so the application can be accessed online. |

***Table 4** – The project coding journey.*

![Image of code process high level design](https://github.com/user-attachments/assets/109334a8-91ab-4d8b-a083-a16e57e0c0d6)
***Figure 8**: High level design of code flow.*


![Image of HTML code in VS code being pushed to Github](https://github.com/user-attachments/assets/6a044182-0e73-4d7e-a08c-ab48671edded)
***Figure 9**: Screenshot of HTML code being placed on a feature branch called ‘feature/html-homepage’. The change has been staged and is ready to be committed to the connected GitHub repository.*


![Image of html homepage merge complete to main branch](https://github.com/user-attachments/assets/bc88f39a-1278-49a6-aae6-a4fda5892ef4)
***Figure 10**: Screenshot of final commit to main branch from feature branch, via develop branch, of html homepage.*

This process shown in figure 9 and 10 was carried out for each feature that was linked to an issue within the GitHub Kanban board, which allowed the controlled growth of the web application. 


### Static Analysis

![Image of live server screenshot in edge alongside both html and css code](https://github.com/user-attachments/assets/d2c85f19-b515-4ce8-83d0-30925d5416ae)
***Figure 11**: Testing on local server of webpage CSS styling.*

The extension in VS Code called "Live Server" was used throughout the development of the code. This allowed a quick and easy way to test the web application and see how the functionality with the API would work, along with how the Python, JavaScript, HTML and CSS scripts would work with each other. The extension mimics what the render server would do when live deployment is made. 
 

Another useful free tool used was [Prettier.io](https://prettier.io/playground/). This site allowed code to be organised into an industry standard format and made it more readable.

</details>



<details>

<summary><h2>Technical Documentation</h2></summary>

### Tech Stack 

| Technology | Purpose |
|---|---|
| **Python** | Backend programming language. |
| **Flask** | Lightweight Python web framework used to build the API/backend. |
| **JavaScript** | Handles frontend logic and dynamic user interaction. |
| **HTML** | Provides the structure of the web application. |
| **CSS** | Provides styling and responsive layout. |
| **GitHub Pages** | Used to host the frontend. |
| **Render** | Used to deploy the backend service. |

***Table 5** – Tech stack for the the IP reputation checker web application.*


### High Level Code Breakdown

| File | Purpose | What it does |
|---|---|---|
| `index.html` | Homepage | Provides the main landing page for the application. It introduces the user to the IP reputation checker and includes the **Enter** button that takes the user to the IP input page. |
| `ip_input_page.html` | IP input and results page | Contains the form where users enter an IP address. It also displays the instructions, submits the IP address for checking, and shows the results returned by the application. |
| `index.css` | Styling | Controls the visual design of the application, including page layout, colours, fonts, buttons, spacing, images, and responsive styling. |
| `index.js` | Frontend logic | Handles user interaction on the webpage, such as reading the entered IP address, sending it to the backend Python API script, receiving the response, displaying results, and showing error messages. |
| `cyber_input_checker.py` | Backend/API logic | Runs the Python server backend. It validates the submitted IP address, reads the API key from the `.env` file or live server deployment, sends a request to the Virus Total API, and returns the results to the frontend. |
|**Testing**|||
| `test_api.py` | Backend testing | Contains tests for the Python backend/API to check that key functions work correctly, such as IP validation and API responses. |
| `index.test.js` | Frontend testing | Contains tests for the JavaScript/frontend functionality, such as checking user input and error messages. |
| `package.json` | Project dependency/configuration file | Lists the JavaScript project details, scripts, and dependencies required for testing. |
| `package-lock.json` | Dependency lock file | Records the versions of installed JavaScript packages so the project works consistently across different machines. |

***Table 6** - High level explanation of the code use, broken down by code file.*

### Running the Application Locally

1) To run the application locally, clone the GitHub repository onto your machine and open the project folder in a code editor such as Visual Studio Code ([Git Clone instructions](https://git-scm.com/docs/git-clone)). 

2) Before running the application, create a `.env` file in the local project folder and add your personal API key as an environment variable:

```env
API_KEY = [insert personal key]
```

[Click here to get a Virus Total API key.](https://docs.virustotal.com/reference/overview)

3) Ensure Python is installed and install any required dependencies using the terminal:
```
pip install flask flask-cors python-dotenv requests
```
The Python backend must be running before the application can be used. Start the backend by running the Python file from the terminal.

4) Once the backend is running, open index.html using a local server. For example, in VS Code you can use the Live Server extension by right clicking on the index.html file and selecting ‘Open with Live Server’. This should open the application in your browser at a local address such as:
   ```
   http://127.0.0.1:5500
   ```

![image of local serving running in Python terminal](https://github.com/user-attachments/assets/e47fc68b-ce6b-45ec-9aa0-a068f86a15c0)

***Figure 12** - Local server running in Python terminal.*


### Automated Testing with GitHub Actions 

GitHub Actions is used to automatically run the project test suites when relevant Python or JavaScript files are updated. The workflow files are stored in the `.github/workflows/` directory using `.yml` configuration files. These workflows are triggered on push and pull requests, supporting a basic CI/CD pipeline by allowing key functionality testing before changes are merged.

Project dependencies are installed as part of the workflow. Python dependencies are defined in `requirements.txt`, while JavaScript dependencies are managed through `package.json`. This ensures that GitHub Actions can recreate the required test environment and run the automated tests consistently.



| Test Area | Test | Purpose |
|---|---|---|
| JavaScript | Smoke test | Confirms that the JavaScript test environment is configured and running correctly. |
| JavaScript | Trim IP address test | Verifies that whitespace is correctly removed from user input before processing. |
| JavaScript | API error test | Checks that error messages are displayed correctly by using a mocked API response. This also validates interaction between the frontend JavaScript and the Python backend error response. |
| Python | Smoke test | Confirms that `pytest` is working correctly using a simple addition test. |
| Python | Valid IP address test | Confirms that a valid IP address is accepted by the validation function. |
| Python | Invalid IP address test | Confirms that an invalid IP address is rejected by the validation function. |
| Python | Results extraction test | Verifies that Virus Total analysis statistics are extracted and presented correctly. |

***Table 7** - Summary of Python and JavaScript tests in GitHub Actions.*

#### The Python CI/CD process:

The GitHub repository is configured to run automated tests using GitHub Actions. When code is changed locally and then pushed or uploaded to the repository, the test suite will run automatically, provided the required CI/CD files remain in place. This includes the workflow `.yml` file within `.github/workflows/`, the relevant test scripts, and dependency files such as `requirements.txt` for Python and `package.json` for JavaScript.

Tests can also be run on a local machine. To do this, the project files should be downloaded or cloned from the GitHub repository, keeping the same folder structure. The required dependencies must then be installed locally. Python testing requires `pytest`, while JavaScript testing requires `jest`.

To run the Python tests locally, use the following terminal command:

```
python -m pytest test_api.py -v
```

To run the JavaScript tests locally, use:
```bash
npm test
```


![Picture of python test passing](https://github.com/user-attachments/assets/19d80c95-e870-4779-8c98-e147b94a1c1c)

***Figure 13** - Local Python test running and passing all four tests in VS code terminal.*

[How to install pytest](https://docs.pytest.org/en/stable/getting-started.html)

[How to install Jest](https://jestjs.io/docs/getting-started)

#### Google Lighthouse

Accessibility testing was conducted on the finished web application using Google Lighthouse. When the first test was run the accessibility score was 96/100 for the homepage and 97/100 for the IP input page.

![Picture of accessibility check](https://github.com/user-attachments/assets/0b208d48-223f-4f63-a00e-e0c79c66bf52)

***Figure 14** - Accessibility test using Google Lighthouse on the IP input page.*

Issues #44 was created to solve this problem. This was solved by adding ``` role="main" ``` into the html body tag <body role="main">. This allows easier identification of the primary content area of a web page for assistive technologies like screen readers.


![Picture of accessibility check passing](https://github.com/user-attachments/assets/be295ce7-8291-43e5-a343-feeeae6fdd5c)

***Figure 15** - Accessibility test using Google Lighthouse on the IP input page scoring 100.*

[Click here for the full Google Lighthouse Report](https://github.com/user-attachments/files/29571876/Google.Lighthouse.Report.pdf)



### User Testing

A small group of six security analysts were asked to test the MVP and answer a questionnaire of ten questions. The results gave mixed feedback highlighting strengths and weaknesses of the product. Feedback from user engagement gave an overall score of 6.83 /10, as shown in figure 16:

![User overall score](https://github.com/user-attachments/assets/5ac03290-73aa-41d5-9a5e-7d576dd3b2d8)

***Figure 16** - User testing overall score.*

[Click here to see a blank copy of the questionnaire](https://github.com/user-attachments/files/29571962/Blank.Feedback.Survey.pdf)

[Click here to see the full user feedback results](https://github.com/user-attachments/files/29571974/Feedback.results.pdf)


### Live Server – Render
Currently the application is based on [Render.com](https://render.com/), this is a free to use service. The link in the about section of the GitHub main page for this application has the link that render uses. 
This link is also embedded in the index.js file. If the server needs to be changed this file is the only file that would have to be edited. 
Render is a simple free live server platform - [read more here](https://render.com/docs).

</details>


