from langchain_openai import ChatOpenAI
from langchain_aws import ChatBedrock
from langchain_google_community import GoogleSearchAPIWrapper
from pydantic import BaseModel, Field
from pprint import pprint
from typing import List
from dotenv import load_dotenv
import sys

# Define a Pydantic model for structured output
class TVShowAirDates(BaseModel):
    show_name: str = Field(description="The confirmed name of the TV show")
    synopsis: str = Field(description="A short synopsis of the show")
    network: str = Field(description="Network or streaming service of the TV show")
    number_of_seasons: int = Field(description="The number of seasons the TV show has aired")
    most_recent_season: int = Field(description="The most recent season of the TV show")
    upcoming_air_dates: List[str] = Field(description="List of upcoming air dates")

def main():
    load_dotenv(".env")
    show_name = sys.argv[1]
    
    # Initialize the Google Search API wrapper
    search = GoogleSearchAPIWrapper(k=10)

    # Initialize the chat model with structured output capability
    # llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    llm = ChatBedrock(model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0")
    structured_llm = llm.with_structured_output(TVShowAirDates)
    # Perform a web search to get context
    search_results = search.run(f"Synopsis, season, and episode details for TV show \"{show_name}\"")
    result = structured_llm.invoke(
        f"Based on these search results, extract the TV show details:\n{search_results}"
    )    
    # Print the structured results
    pprint(result.model_dump())

if __name__ == "__main__":
    main()
    
