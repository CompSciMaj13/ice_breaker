# Ice Breaker App
===============

The Ice Breaker App is a web-based application that generates a short summary and two interesting facts about a person based on their LinkedIn profile. The app uses natural language processing (NLP) techniques to scrape relevant information from the LinkedIn profile and generate a human-readable summary.

### How it Works
----------------

1. The user enters the name of the person they want to generate information for.
2. The app uses the `linkedin_lookup_agent` to find the LinkedIn username associated with the given name.
3. The app then scrapes the relevant data from the LinkedIn profile using the `scrape_linkedin_profile` function.
4. The scraped data is used as input to a prompt template, which generates a summary and two interesting facts about the person.

### Running the Flask App
-------------------------

To run the Flask app, follow these steps:

1. Install the required packages by running the following command in your terminal:
```bash
pip install -r Pipfile
```
2. Set up your API keys for OpenAI, Tavily, and Proxycurl by copying `default.env` to a file named `.env` with the following content:
```makefile
OPENAI_API_KEY=
TAVILY_API_KEY=
PROXYCURL_API_KEY=
```
Replace the empty strings with your actual API keys.

3. Run the following command to start the Flask app:
```bash
python app.py
```
This will start the Flask development server, which can be accessed at <http://127.0.0.1:5000>.

### Using the App
-----------------

To use the app, open a web browser and navigate to <http://127.0.0.1:5000>. You will see an HTML form with a single input field labeled "Name". Enter the name of the person you want to generate information for (e.g., "Aravind Srinivas"), and click the submit button.

The app will then generate a summary and two interesting facts about the person, along with their profile picture URL. You can view the generated text by clicking on the "Process" button.

### index.html File
--------------------

The `index.html` file is used as the template for the app's user interface. It contains HTML, CSS, and JavaScript code to render the summary, interesting facts, and profile picture.

### Prerequisites
------------------

* Python 3.12 or later
* Flask installed using pip
* Required packages listed in the Pipfile (langchain, langchain-openai, black, etc.)
* API keys for OpenAI, Tavily, and Proxycurl set up in `default.env` file

Note: The app requires an active internet connection to function properly.