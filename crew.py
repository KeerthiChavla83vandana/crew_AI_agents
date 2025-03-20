from crewai import Crew,Process
from tasks import research_task,write_task
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration

"""
    EX: CREATING 2 AGENTS TO REASEARCH AND WRITE AN ARTICLE ON A GIVEN TOPIC 

    # THAT AGENTS USE GOOGLE ‘S GEMINI AI MODEL FOR REASONING AND THE SERPERDEV TOOL INTERNET SEARCHES 

    When you call crew.kickoff(inputs={'topic':'An artificial Mother womb'}), here's what happens step by step: 

    1️⃣ Crew Initialization 

    Crew is initialized with:  

    Agents: news_researcher and news_writer 

    Tasks: research_task and write_task 

    Process: sequential, meaning tasks execute one after another. 
"""
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'An artificial Mother womb'})
print(result)