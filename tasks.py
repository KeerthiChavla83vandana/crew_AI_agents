from crewai import Task
from tools import tool
from agents import news_researcher,news_writer

# Research task
research_task = Task(
  description=(
    "Identify the next big trend in {topic}."
    "Focus on identifying pros and cons and the overall narrative."
    "Structure the report with clear, engaging **headings**. "
    "Make it **informative**, **concise**, and **engaging**. "
    "Add **catchy phrases** to keep readers hooked 🎯. "
    "Use relevant **emojis** to make it visually appealing"
    "Your final report should clearly articulate the key points,"

    "its market opportunities, and potential risks."
  ),
  expected_output=("Should include a summary, pros & cons, market potential, and a conclusion."
                   "A comprehensive 3 paragraphs long report on the latest AI trends."),
  tools=[tool],
  agent=news_researcher,
)


"""
An agent may have access to multiple tools.Agent1-> backend task, db task
 backend task need -> Fast API tool
 db task need -> postgresql tool

 A task may only require specific tools, ensuring efficient execution.
 
"""
# Writing task with language model configuration
write_task = Task(
  description=(
    "Compose an **engaging**,insightful article on {topic}."
    "Focus on the latest trends and how it's impacting the industry."
    "This article should be easy to understand, engaging, and positive. 💡✨"
    "Use clear **headings**, short paragraphs, and catchy **subheadings**. "
    "Include **emojis** to make it more fun and interactive. "
    "End with a **call to action** to keep the readers engaged!"

  ),
  expected_output=( "A well-structured, **4-paragraph article on {topic}**  with **headings**, "
    "bolded key points, and **emoji-filled** engaging content 🎉📖."),
  tools=[tool],
  agent=news_writer,
  async_execution=False,
  output_file='new-blog2-post.md'  # Example of output customization
)