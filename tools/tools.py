from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_urls_tavily(name: str):
    """Searches for Linkedin or Twitter Profile Page. Returns the top 3 URL search results."""
    search = TavilySearchResults()
    res = search.run(f"{name} LinkedIn Profile")
    return res[0]["url"], res[1]["url"], res[2]["url"]