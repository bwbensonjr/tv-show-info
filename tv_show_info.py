from langchain_aws import ChatBedrock
from langchain_core.tools import tool, Tool
from langchain_google_community import GoogleSearchAPIWrapper
from dotenv import load_dotenv
from pydantic import BaseModel, Field
from typing import List

# Define the structured output schema
class EpisodeSchedule(BaseModel):
    show_name: str = Field(description="The name of the TV show")
    next_air_dates: List[str] = Field(description="A list of the upcoming air dates of the show")

def main():
    load_dotenv(".env")

def top_results(query, k=5):
    results = search.results(query, k)
    return results
    
def web_search_tool(k=5):
    search = GoogleSearchAPIWrapper()
    search_tool = Tool(
        name="web_search",
        description="Search the web",
        func=top_results,
    )
    return search_tool
