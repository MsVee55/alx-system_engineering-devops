# Postmortem

A postmortem in tech is a process of analyzing and learning from an incident or outage that occurred in a technical system or application. It is a retrospective evaluation of what happened, why it happened, and what can be done to prevent it from happening again in future.

The goal of a postmortem is not to place blame on any individual or team, but rather to identify the root cause of the problem and create a plan to prevent it from recurring. It is a collaborative effort that involves multiple stakeholders, including software developers, operations teams, support teams, and management.

A typical postmortem process involves gathering data about the incident, holding a meeting or workshop to discuss the incident and its causes, and creating a report that outlines the findings and recommendations for preventing similar issues in the future.

Overall, postmortems are a crucial part of maintaining reliable and stable technical systems. They allow organizations to learn from mistakes and improve their processes, ultimately leading to better service for their customers

# My Postmortem

# Issue in summary:


* Duration: May 12, 2023 3:00 PM PST - May 12, 2023 6:00 PM PST

* Impact: Our company's web application was down for three hours, resulting in a complete outage for all users, including our paying customers. Users were experiencing slow load times and inability to access the application.

* Root Cause: The root cause of the issue was a database connectivity problem.

* Timeline:
- 3:00 PM PST: The issue was detected by our monitoring system that alerted the on-call engineer.
- The engineer noticed multiple errors in the database logs and started investigating the issue.
- Assumption was made that the database might have been overwhelmed by excessive traffic.
- Investigation of the database server logs followed by database restart. However, it didn't fix the issue.
- The situation was escalated to the entire engineering team.
- The team noticed an issue with the database configuration resulting in connectivity issues and an update to the database.
- The incident was resolved at 6:00 PM PST.

* Root Cause and Resolution:

The database configuration was updated recently, resulting in connectivity issues. This prevented the application from accessing the database, causing the outage. The incident was resolved by updating the database configuration to the correct setting and restarting the database services.

* Corrective and Preventative Measures:

To prevent this type of outage from occurring again, we need to take the following measures:
- Implement better monitoring to detect database connectivity issues specifically.
- Develop runbooks for proper procedures during outages to minimize their length and impact.
- Review database configuration changes with the team before performing any update going forward.
- Develop better communication channels between engineering and management to improve incident management and notification.


Hey! Don't worry, not everyone will face such outage.
We're programmers, and we never make errors....without solutions.
