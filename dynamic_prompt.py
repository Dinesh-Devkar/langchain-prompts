
import streamlit as st

from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import PromptTemplate



load_dotenv()



# model=ChatAnthropic(model_name='claude-sonnet-4-6')
# result = model.invoke("writefive lines about india")
# print(result)




st.title("Research Paper Summarizer")

# Dropdown 1: Research Paper
research_paper = st.selectbox(
    "Research Paper",
    ["Attention Is All You Need",
      "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners", 
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

# Dropdown 2: Input Style
input_style = st.selectbox(
    "Input Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

# Dropdown 3: Input Length
input_length = st.selectbox(
    "Input Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

template= PromptTemplate(template="""
Please summarize the research paper titled \'{paper_input}\' with the following specifications: Explanation Style: {style_input}  Explanation Length: {length_input}  1. Mathematical Details:     - Include relevant mathematical equations if present in the paper. 
  - Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
   2. Analogies:     - Use relatable analogies to simplify complex ideas. 
     If certain information is not available in the paper,
       respond with: \'Insufficient information available\' instead of guessing.
           Ensure the summary is clear, accurate, and aligned with the provided style and length.
""",input_variables=['paper_input','style_input','length_input'])


# Summarize button
if st.button("Summarize"):
    model=ChatAnthropic(model='claude-sonnet-4-6')
    prompt= template.invoke({
        'paper_input':research_paper,
        'style_input':input_style,
        'length_input':input_length
    })
    result= model.invoke(prompt)
    st.write(result.content)
