"""
This module contains the `lookup` function, which uses OpenAI's GPT-3.5-turbo
model to find the LinkedIn profile URL of a given person. The function takes a
full name as input and returns the corresponding LinkedIn profile URL.

The `lookup` function utilizes various tools from LangChain, including the
ChatOpenAI, and React Agent. It can be used for finding LinkedIn profile URLs of
individuals or for other natural language processing tasks.
"""

import os

from dotenv import load_dotenv
from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama
from langchain_core.tools import Tool
from langchain_openai import ChatOpenAI

from tools.tools import get_profile_urls_tavily

load_dotenv()


def lookup(name: str) -> str:
    """
    Looks up a LinkedIn profile URL using OpenAI's GPT-3.5-turbo model.

    :param name: The full name of the person whose LinkedIn profile URL is to be looked up.
    :type name: str
    :return: The URL of the LinkedIn profile page
    :rtype: str
    """
    # llm = Ollama(
    #    temperature=0.8,
    #    #model="llama3:instruct",
    #    #model="dolphin-llama3",
    #    #model="phi3:instruct",
    #    #model="llama3-chatqa",
    #    #model="vanilj/llama-3-magenta-instruct-4x8b-moe",
    #    base_url="http://aibox:11434"
    #    )

    # OpenAI
    llm = ChatOpenAI(
        temperature=0,
        model_name="gpt-3.5-turbo",
    )

    template = """
        Given the full name {name_of_person}, I want you to find the URL to their LinkedIn profile page.
        The LinkedIn Profile URL will start with https://il.linkedin.com/in/
        Your Answer should contain only one URL. Do not answer with multiple options.
        """

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )
    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn Profile page",
            func=get_profile_urls_tavily,
            description="Useful for when you need to find a LinkedIn profile page URL.",
        )
    ]

    react_prompt = hub.pull("hwchase17/react")

    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        handle_parsing_errors=True,
        max_iterations=5,
        verbose=True,
    )

    result = agent_executor.invoke(
        input={"input": prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile_url = result["output"]
    return linkedin_profile_url


if __name__ == "__main__":
    # Test the function with a name of the instructor of the LangChain course, Eden Marco
    linkedin_url = lookup(name="Eden Marco")
    print(linkedin_url)
