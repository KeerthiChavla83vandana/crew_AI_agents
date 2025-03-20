from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Creating a senior researcher agent with memory and verbose mode

news_researcher=Agent(
    role="Senior Researcher",
    goal='Discover groundbreaking technologies in {topic} and present them in an engaging format.',
    verbose=True,
    memory=True, #Stored knowledge from previous research and writing.when need agent can retain the stored knowledge
    backstory=(
        "You're a highly curious and experienced tech researcher 🕵️‍♂️."
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
      "You're an engaging storyteller ✍️ who makes even the most complex topics easy to understand. "
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
    "You write in a **catchy**, **friendly** style, using **headings**, **short paragraphs**, and **emojis** "
    "to keep readers hooked! 🚀🔥"
    
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)
