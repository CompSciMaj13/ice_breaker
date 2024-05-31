"""
This module contains tools for searching and scraping data from various sources, including LinkedIn.
The `get_profile_urls_tavily` function is used to search for LinkedIn profile URLs based on a given username.
"""

from langchain_community.tools.tavily_search import TavilySearchResults


def get_profile_urls_tavily(name: str):
    """
    Searches for LinkedIn Profile URLs.

    :param name: The username to search for
    :type name: str
    :return: A tuple of the top 3 URL search results
    :rtype: tuple
    """
    search = TavilySearchResults()
    res = search.run(f"{name} LinkedIn Profile")
    return res[0]["url"], res[1]["url"], res[2]["url"]
