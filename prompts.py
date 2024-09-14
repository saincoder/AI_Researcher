# prompts.py

def get_research_prompt(question, field):
    return {
        "role": "user",
        "content": f"""
        The user is asking a question related to the field '{field}'.
        Is this question research-related? If it is, explain the topic '{question}' clearly,
        focusing on important concepts, recent advancements, and potential research directions.
        If the question is not related to research, reply that the question doesn't fit the research criteria
        and suggest research-related topics.
        """
    }

def get_guidance_prompt(question, field):
    return f"""
    To help you explore the research question '{question}' in the field of '{field}', I suggest starting
    with a broad literature review. Identify key papers and influential research in this area. 
    Then, explore open challenges or gaps that your question might address. 
    Focus on gathering sources that are peer-reviewed and relevant to your specific research interest. 
    Formulate experiments or approaches to investigate the research problem.
    """

def invalid_question_prompt():
    return """
    This question doesn't appear to be research-related. Please ask questions that align with research topics
    such as theories, methodologies, or advancements in the field. You could ask about current trends, 
    innovations, or key challenges in research fields like AI or Data Science.
    """
