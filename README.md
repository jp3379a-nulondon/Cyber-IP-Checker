# Cyber Check - IP Checker

Code and Documentation for Cyber Check Web Application (SE Summative). Created by Joe Petzold.

<details>

<summary>Introduction</summary>

### Proposal

This project proposes the development of a cyber security web application that allows users to submit an IP address through a web interface. The IP address is sent to a backend server, checked against an external reputation API, and the results are returned to the user in a clear and easy-to-understand format.

### Purpose

The purpose of the application is to provide security analysts with a single interface for checking the reputation of IP addresses. By presenting the results in a simple and user-friendly way, the application supports quicker triage, clearer interpretation of reputation data, and more informed decision-making during security investigations.

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
The IP Checker is designed to be a user-friendly and intuitive web application. It will contain minimal pages, making navigation simple and easy to follow. Users will access the application through a homepage, where they will be presented with an input box and clear instructions. Once an IP address is submitted, the results will be clearly displayed. If an error occurs, a constructive error message will be shown, suggesting the potential issue that caused the error.

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
Based on the proto-persona card shown in Figure 1, the design should be aimed at users who are interested in, or work within, the cyber security field. Therefore, the web application should adopt a cyber/futuristic theme that is visually engaging and appealing to this audience, while remaining simple, clear, and not overly cluttered or confusing. The design should also maintain a professional tone, as the application produces results that may identify potentially malicious IP addresses. The following designs have been created based on these highlighted design considerations.

#### Low Fidelity design
![Lo-Fi MVP design](https://github.com/user-attachments/assets/d237200f-371e-44de-bd88-5ba1386073ea)

***Figure 2**: Low Fidelity design of the MVP IP checker.*

**[Click here for a full Figma prototype](https://www.figma.com/proto/z22xMGlc1B1KgzUcfBqSaS/Software-Engineering-Year-3?node-id=0-1&t=xXiWXE5LrOzMTkP3-1)**

#### High Fidelity design
![Hi-Fi MVP design](https://github.com/user-attachments/assets/dec8213a-316c-431a-977c-d71595982768)

***Figure 3**: High Fidelity design of the homepage MVP IP checker.*

</details>

