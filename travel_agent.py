import sys
from typing import List
from textwrap import dedent
from agno.agent import Agent
from agno.models.ollama import Ollama
from agno.tools.exa import ExaTools
from agno.tools.duckduckgo import DuckDuckGoTools
from pydantic import BaseModel, Field
from rich.prompt import Prompt
from maps_tools import GoogleMapsTool
from prompts import system_prompt_travel_agent, expected_output, instructions
from dotenv import load_dotenv
EXAAI_API_KEY = load_dotenv("EXAAI_API_KEY")

class MapURL(BaseModel):
    place_name:str = Field(None,description='Name of the place search for')
    maps_url:str = Field(None, description='Google Maps URL for the place')

class MapURLs(BaseModel):
    urls:List[MapURL]

class Inputs(BaseModel):
    days: int =Field(None,'Number of Days for the Tript')
    description :str = Field(None, )