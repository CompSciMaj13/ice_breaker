from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile


def ice_break_with(name: str) -> str:
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        Given the Linkedin JSON information {information} about a person from I want you to create:
        1. A short summary
        2. Two interesting facts about the person
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = Ollama(temperature=0, model="llama3:instruct", base_url="http://aibox:11434")

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break_with(name="Aravind Srinivas")
