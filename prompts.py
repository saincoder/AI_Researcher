# prompts.py

def get_research_prompt(question, field):
    return {
        "role": "user",
        "content": f"""
        The user is asking a research-related question in the field of '{field}'. Please provide a comprehensive answer to the question '{question}'.
        
        Additionally, include the following guidance:
        - A suggested approach to perform a literature review.
        - Potential open challenges or unresolved questions in this field.
        - The most suitable methods or frameworks to address the research problem.
        - Peer-reviewed sources or journals to consult.
        - Next steps to further explore the topic, including objectives, methodology, and potential tools or datasets.

        Make sure the response is structured and concise.
        """
    }



def get_guidance_prompt(question, field):
    return f"""
    Here’s a suggested approach to explore the research question '{question}' in the field of '{field}':

    - **Literature Review**: Start by identifying key papers, influential researchers, and recent advancements in the field.
    - **Open Challenges**: Look for gaps or unresolved questions in existing research that align with your query.
    - **Peer-Reviewed Sources**: Focus on gathering peer-reviewed papers, conference publications, and reputable journals.
    - **Approach and Methods**: Consider the most suitable experimental methods or theoretical frameworks to address the research problem.
    - **Next Steps**: Define a research plan, including objectives, methodology, and potential datasets or tools.

    This structured approach will guide you in navigating and contributing to the existing body of knowledge.
    """


def invalid_question_prompt():
    return """
    This question doesn't appear to be research-related. Please ask questions that align with research topics
    such as theories, methodologies, or advancements in the field. You could ask about current trends, 
    innovations, or key challenges in research fields like AI or Data Science.
    """
