# EchoSale
![opener_agent_ui](images/opener_agent_ui.png)
![escalator_agent_ui](images/escalator_agent_ui.png)

In this project I am building Opener and Escalator agent that will assist Antematter's sales department. Here is the description about the two agents that I am going 

## Opener Agent
The Opener Agent is responsible for generating personalized cold emails to potential leads with the goal of enticing them to choose Antematter as their software consultancy provider. The agent should follow these guidelines:

1. Personalized Emails: The emails should be personalized for each lead.
2. Inquire about Details: The email should inquire about the scope and budget the lead has in mind.
3. Length and Format: The email should have a brief subject (less than 30 characters) and a body no longer than three paragraphs.
4. Tone: The tone of the email should be human and not mechanical.
5. Language: The email should not use flowery or flattering language.
6. Data Storage: Store all inputs and outputs of the agent in a CSV file, including Model Name, Temperature, Lead information, Prompt, Email Subject, and Email Body.


## Escalator Agent
The Escalator Agent is responsible for handling the responses from the leads and taking appropriate actions based on the information provided. The agent should follow these guidelines:

1. Escalate with Budget and Scope: If the lead provides information about the budget and project scope, escalate the lead to the admin.
2. Request Missing Details: If no information is available for either budget, scope, or both, prompt the user to provide the missing details.
3. Escalate for More Information: If the user requests more information, escalate the lead to the admin.

The goal of these agents is to streamline the sales process by generating personalized emails and handling lead responses autonomously, ultimately escalating qualified leads to the admin for further action.

## Opener Agent Architecture

![opener_agent_architecture](diagrams/architecture_diagram_openeragent.png)

## Escalator Agent Architecture
![escalator_agent_architecture](diagrams/architecture_digram_escalatoragent.png)


## Steps to Run the Code
1. Clone the repository.

```bash
git clone https://github.com/enstazao/EchoSale.git
```

2. Create a virtual Environment

```bash
conda create -n echosale_env python=3.10
```

3. I have added all the dependencies in the file requirements.txt run this command to install all the requirements.

```bash
pip install -r requirements.txt
```

4. Create a new file .env and place OPENAI_API_KEY their.

```bash
OPENAI_API_KEY="Your_OPENAI_API_KEY"
```

5. Now run the streamlit application.

```bash
streamlit run app.py
``` 

## Opener Agent Inputs, Outputs CSV
[https://docs.google.com/spreadsheets/d/1NCRNOnNK1kzKHRKCKYqJGoATY3YPBro1n3MMe04HvMg/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1NCRNOnNK1kzKHRKCKYqJGoATY3YPBro1n3MMe04HvMg/edit?usp=sharing)
## Escalator Agent Inputs, Outpus CSV
[https://docs.google.com/spreadsheets/d/19MFeFBwUx-9d6-7PFJXs0EKJENtuzy2E4cHy9l6_zZo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/19MFeFBwUx-9d6-7PFJXs0EKJENtuzy2E4cHy9l6_zZo/edit?usp=sharing)