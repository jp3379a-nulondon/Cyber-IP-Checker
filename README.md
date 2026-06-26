# Cyber Check - IP Checker

Code and Documentation for Cyber Check Web Application (SE Summative). Created by Joe Petzold.


<details>

<summary>Introduction</summary>

### Proposal

This project proposes the development of a cyber security web application that allows users to submit an IP address through a web interface. The IP address is sent to a backend server, checked against an external reputation API, and the results are returned to the user in a clear and easy-to-understand format.

### Purpose

The purpose of the application is to provide security analysts with a single interface for checking the reputation of IP addresses. The application will present the results in a simple and user-friendly way, supporting quicker triage, clearer interpretation of reputation data, and more informed decision-making during security investigations.

### Business Requirement – Benefit Realisation

The business requirement is to reduce the need for analysts to manually check multiple external platforms when investigating suspicious IP addresses. A centralised IP reputation checker improves operational efficiency by reducing investigation time, supporting consistent reporting, and allowing analysts to focus more on analysis and response actions.

If the MVP (Minimum Viable Product) is successful, the application could be expanded to include multiple threat intelligence sources, providing a more complete risk profile for each IP address. This would further improve detection accuracy, support faster incident response, and reduce cognitive load on the security team when dealing with active or potential threats.

### Feasibility

The TELOS framework has been applied to this project to understand how feasible the project is. 
| Feasibility Area | Assessment |
|---|---|
| **Technical Feasibility** | The project is technically viable using a Python backend, such as Flask or FastAPI, with a lightweight frontend. The VirusTotal REST API provides structured JSON responses that can be parsed and displayed in a custom user interface. Additional APIs, such as AbuseIPDB or Shodan, could be integrated later using a modular API-handling design. Hosting can be provided via free online tools like Render.com, but this could be improved through internal infrastructure or cloud platforms such as Microsoft Azure. |
| **Economic Feasibility** | The MVP has minimal costs, mainly involving development time and any potential API rate limits or subscription requirements for VirusTotal. Expanding the system to include multiple APIs may introduce licensing costs, but these could be justified by reducing analyst workload and improving investigation speed. |
| **Legal Feasibility** | The system must comply with API terms of service, including VirusTotal data usage restrictions, as well as organisational data handling policies. Although no personal data is processed, logs may contain sensitive security intelligence and should therefore be securely stored with appropriate access control. |
| **Operational Feasibility** | The tool aligns with security workflows and requires minimal training due to its simple IP input and results output design. It can support existing investigation processes. |
| **Schedule Feasibility** | An MVP can be delivered within a short development cycle, focusing on core API integration, a basic user interface, and clear response display. Future iterations could expand API coverage and introduce dashboard-style functionality. |

***Table 1** – TELOS framework analysis.*

Using the TELOS framework, the project can be considered feasible. Developing the MVP requires technical implementation which the development team possess, as they have the necessary skills to build the MVP using suitable web technologies. The project is also economically viable because it is small in scope and is expected to involve limited development costs, while still addressing the user’s need for a centralised IP reputation checking tool. The project is achievable within a short development timeframe and provides a practical foundation for future expansion if the MVP proves successful.

</details>


<details>

<summary>Design and Prototyping</summary>

### Requirements
The IP Checker is designed to be a user-friendly and intuitive web application. It contains minimal pages, making navigation simple and easy to follow. Users access the application through a homepage, where they are presented with an input box and clear instructions. Once an IP address is submitted, the results are clearly displayed. If an error occurs, a constructive error message is shown, suggesting the potential issue that has caused the error.

### Functional Requirements

| ID | Functional Requirement | Description |
|---|---|---|
| FR1 | IP Address Input | The application must allow users to enter an IP address into an input field. |
| FR2 | Input Validation | The application must check that the input field is not empty before submitting the request. |
| FR3 | API Request | The application must send the entered IP address to a backend server to make the API call for reputation checking. |
| FR4 | Reputation Results | The application must display the IP reputation results returned from the API, including malicious and suspicious results. |
| FR5 | Visual Results Display | The application must present the results in a clear visual format, such as percentage-style bars, to make the output easier to understand. |
| FR6 | Error Handling | The application must display an error message if the IP address cannot be checked or if the backend server/API returns an error. |
| FR7 | Homepage Navigation | The application should allow users to return to the homepage by clicking the Cyber Check logo. |

***Table 2** – Key Functional Requirements of the IP Checker MVP.*

### Non-Functional Requirements

| ID | Non-Functional Requirement | Description |
|---|---|---|
| NFR1 | Usability | The application should be simple and easy to use, allowing users to check an IP address without needing detailed instructions. |
| NFR2 | Performance | The application should return results quickly enough to support efficient security investigation and triage. |
| NFR3 | Reliability | The application should handle API or server errors gracefully and provide clear feedback to the user. |
| NFR4 | Security | The VirusTotal API key must not be exposed in the frontend JavaScript or Python code and should be stored securely in the backend environment. |
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

<summary>Project Management</summary>

### Management Structure
The IP Checker project adopts an agile style approach while following the typical software development lifecycle, including feasibility analysis, requirements analysis, planning, design, development, testing, and deployment. This initial project represents the first iteration of the product’s lifecycle and is delivered across three sprints. The first sprint focuses on planning and design activities, the second sprint concentrates on development and testing, and the third sprint involves deploying the completed minimum viable product (MVP) to GitHub alongside the required project documentation. If further development is required, the project can be extended into a continuous agile development cycle, allowing additional iterations, refinements, and feature enhancements to be implemented over time.
New features are managed through a structured GitHub workflow, supported by integration between Visual Studio Code and the GitHub repository. Updated code and functionality are developed locally in Visual Studio Code before being pushed to GitHub through pull requests. Each new feature is created within a dedicated feature branch, which is then merged into the development branch for review and testing. Once the changes are checked and approved, they are merged into the main branch to form part of the stable version of the project. This approach supports version control, collaboration, and a clear audit trail of development activity.


### Kanaban board – GitHub Projects

![Kanban board start](https://github.com/user-attachments/assets/d9088470-eae0-499f-945c-abe75f42da71)
***Figure 4**: The project Kanban board at the ealier stages of the development lifecycle.* 

![Kanban board middle](https://github.com/user-attachments/assets/ccd4f06a-2786-463a-954d-ac34bc6fe253)
***Figure 5**: The project Kanban board at a middle point of the development lifecycle.*

GitHub Projects is used to manage the project through an agile-style workflow, where tasks are converted into tickets or issues and tracked across a Kanban-style board. This supports structured planning by making each task visible and allowing dependencies between issues to be identified. For example, if one issue needs to be completed before another can begin, this can be recognised early and prioritised appropriately.
The work is organised into sprints, which allows the overall project to be divided into smaller, more manageable sections. This approach supports incremental progress and helps ensure that planning, design, development, testing, deployment, documentation, and evaluation activities are completed in a logical order. The GitHub Projects board is organised using columns **Backlog**, **In Progress**, **In Review**, and **Done**, enabling progress to be monitored throughout the development lifecycle. This provides a clear structure for managing requirements, tracking development activity, and ensuring that each stage of the project is completed in a controlled and transparent manner.

### Labelling

![Project labels](https://github.com/user-attachments/assets/314780cd-b60f-41d9-bd02-0b8332563d57)
***Figure 6**: The project labels are used to assign to issues.*

Custom labels are used to categorise issues and improve the organisation of the GitHub Projects board. Labels such as **planning**, **feasibility**, **requirements**, **design**, **testing**, **development** and **deployment** make it easier to identify the purpose of each issue and understand which part of the project it relates to. Labelling supports filtering and prioritisation, as specific types of work can be grouped together and reviewed more efficiently during each sprint. 

### Issues

![Project issues](https://github.com/user-attachments/assets/c9469fbc-ced3-41b3-a105-bee74c61e488)
***Figure 7**: The project issues are created and placed on the kanban board.*

GitHub issues are used and created at the start of the project and added to the backlog to support planning and task management. These issues cover key project activities, including design, development, testing, deployment and documentation. Each issue represents a specific task, bug, or improvement, making the workload easier to organise.
Issues can be created at any time during the project to address new problems, such as coding errors or design changes. Each issue is linked to the GitHub Projects Kanban board, allowing progress to be tracked across stages such as **Backlog**, **In Progress**, **In Review**, and **Done**.
Issues are linked to branches and pull requests, creating traceability between the task and code changes. This supports version control and a structured development workflow.

</details>
