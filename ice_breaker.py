from langchain.prompts.prompt import PromptTemplate
from langchain_community.llms import Ollama

from third_parties.linkedin import scrape_linkedin_profile


if __name__ == "__main__":
    print("Hello langchain")

    summary_template = """
        given the Linkedin JSON information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
        """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = Ollama(temperature=0, model="llama3:instruct", base_url="http://aibox:11434")

    chain = summary_prompt_template | llm
    linkedin_data = scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco",
            mock=True,
        )
    res = chain.invoke(input={"information": linkedin_data})

    print(res)
