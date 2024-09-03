from .prompts import JD_PROMPT
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

def generate_job_description(validated_data):
    prompt_template = JD_PROMPT
    prompt = PromptTemplate(
        template=prompt_template, 
        input_variables=[
            "company_name", "job_title", "require_skills", "experience", 
            "location", "qualifications", "salary", 
            "job_type", "benefits"
        ]

    )

    OPENAI_API_KEY = ''
    llm = ChatOpenAI(model="gpt-4o-mini", api_key=OPENAI_API_KEY, temperature=0.7)
    chain = prompt | llm | StrOutputParser()
    
    response = chain.invoke(validated_data)
    
    # Output text is directly parsed
    output_text = response
    
    sections = output_text.split("\n\n")
    
    # Initialize empty strings for each section
    position_description = ""
    Job_description = ""
    Requirements = ""
    why_work_here = ""
    perks_and_benefits = ""
    about_us = ""
    salary_range=""
    Job_info=""

    # Extract relevant sections into the corresponding variables
    for section in sections:
        if "Position:" in section:
            position_description = section
        elif "Job Description:" in section:
            Job_description = section
        elif "Requirements:" in section:
            Requirements = section
        elif "Why Work at" in section:
            why_work_here = section
        elif "Perks and Benefits:" in section:
            perks_and_benefits = section
        elif "About Us" in section:
            about_us = section
        elif "Salary Range" in section:
            salary_range = section
        elif "Job Information" in section:
            Job_info = section
        elif "Website Link" in section:
            website_link = section

    
    # Retu rn each section separately
    return position_description,why_work_here, Job_description, Requirements, perks_and_benefits ,about_us,salary_range,Job_info,website_link
