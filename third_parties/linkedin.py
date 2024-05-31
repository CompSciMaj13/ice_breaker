"""
LinkedIn Profile Scrapper

This module provides functions to scrape information from LinkedIn profiles.
It can be used to extract profile data, such as name, title, company, location, etc.

The module includes a function `scrape_linkedin_profile` that takes a LinkedIn profile URL and an optional `mock` parameter. If `mock` is True, it uses a pre-defined JSON response instead of making an actual API request.
"""

import os

import requests
from dotenv import load_dotenv

load_dotenv()


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False):
    """
    Scrape information from LinkedIn profiles.

    :param linkedin_profile_url: The URL of the LinkedIn profile to scrape.
    :type linkedin_profile_url: str
    :param mock: Whether to use a mock response (default is False).
    :type mock: bool

    Manually scrape the information from the LinkedIn profile. If `mock` is True, uses a pre-defined JSON response instead of making an actual API request.
    """
    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/emarco177/0d6a3f93dd06634d95e46a2782ed7490/raw/fad4d7a87e3e934ad52ba2a968bad9eb45128665/eden-marco.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )
    else:
        api_endpoint = "https://nubela.co/proxycurl/api/v2/linkedin"
        header_dict = {"Authorization": f'Bearer {os.getenv("PROXYCURL_API_KEY")}'}
        response = requests.get(
            api_endpoint,
            params={"url": linkedin_profile_url},
            headers=header_dict,
            timeout=60,
        )

    data = response.json()
    return data


if __name__ == "__main__":
    # Testing the function with a real LinkedIn profile URL and the mock parameter set to True (using a GitHub Gist).
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/eden-marco",
            mock=True,
        )
    )
