"""
This module provides a function to generate a short summary and two interesting facts about a person based on their LinkedIn profile.
The function uses the `linkedin_lookup_agent` to find the LinkedIn profile URL of the given name, then scrapes the profile data using the `scrape_linkedin_profile` function.
A prompt template is used to create a summary and interesting facts based on this data.

:author: Jesse A. Lane
:date: 2024-05-30
"""

from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama

from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from third_parties.linkedin import scrape_linkedin_profile
from output_parsers import summary_parser


def ice_break_with(name: str) -> str:
    """Generates a short summary and two interesting facts about a person based on their LinkedIn profile.

    :param name: The name of the person to generate information about (used to lookup their LinkedIn username)
    :type name: str
    :return: A formatted string containing the summary, two interesting facts, and the provided information
    :rtype: str
    """
    linkedin_username = linkedin_lookup_agent(name=name)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)

    summary_template = """
        Given the Linkedin JSON information {information} about a person from I want you to create:
        1. A short summary
        2. Two interesting facts about the person

        \n{format_instructions}
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={"format_instructions": summary_parser.get_format_instructions()}
    )

    llm = Ollama(temperature=0, model="llama3:instruct", base_url="http://aibox:11434")

    chain = summary_prompt_template | llm | summary_parser
    res = chain.invoke(input={"information": linkedin_data})

    print(res)


if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    ice_break_with(name="Aravind Srinivas")
