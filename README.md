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

***Table 1** – TELOS framework analysis*

Using the TELOS framework, the project can be considered feasible. Developing the MVP requires technical implementation which the development team possess, as they have the necessary skills to build the MVP using suitable web technologies. The project is also economically viable because it is small in scope and is expected to involve limited development costs, while still addressing the user’s need for a centralised IP reputation checking tool. The project is achievable within a short development timeframe and provides a practical foundation for future expansion if the MVP proves successful.

</details>
