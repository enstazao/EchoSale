import os
from dotenv import load_dotenv
from langchain import LLMChain
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


# @desc     Generate an email based on the prompt 
# @prompt   prompts/escalator_agent_prompt.md
def setup_escalator_chain():
    # Load environment variables
    load_dotenv()

    # Set up OpenAI API key
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    # Determine the absolute path to the markdown file
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    markdown_file_path = os.path.join(base_dir, 'prompts', 'escalator_agent_prompt.md')

    # Load prompt from markdown file
    with open(markdown_file_path, 'r') as file:
        escalator_agent_prompt = file.read()

    # Create the prompt template and LLMChain
    escalator_agent_prompt_template = PromptTemplate(
        template=escalator_agent_prompt,
        input_variables=["lead_name", "lead_role", "lead_company_name", "lead_company_information", "lead_response", "looking_for", "project_title"]
    )

    # Instantiate the language model with the GPT-4 model
    llm = ChatOpenAI(model_name="gpt-4", temperature=0.5)

    # Create the LLMChain with the defined prompt template and language model
    chain = LLMChain(llm=llm, prompt=escalator_agent_prompt_template)

    return chain
