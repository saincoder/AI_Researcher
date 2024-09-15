import os
import streamlit as st
from dotenv import load_dotenv
import socket 
from groq import Groq
from scholarly import scholarly
from prompts import get_research_prompt, get_guidance_prompt, invalid_question_prompt

# Load environment variables from .env file
load_dotenv()

# Set up Groq client
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("GROQ_API_KEY not found. Please check your environment variables.")
else:
    client = Groq(api_key=api_key)

# Function to check internet connection
def is_connected():
    try:
        # Check if host is reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

# Streamlit UI Enhancements
st.set_page_config(page_title="AI Researcher Pro - Your Research Companion", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        font-family: 'Arial', sans-serif;
    }
    .stButton button {
        border-radius: 10px;
        padding: 10px 20px;
    }
    
    .big-title {
        font-size: 80px;
        font-weight: bold;
        color: #d84df1;
        text-align: center;
        background: linear-gradient(90deg, #4285f4, #ea4335, #fbbc05, #34a853);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .subtitle-style {
        font-size: 18px;
        text-align: center;
        margin-bottom: 20px;
    }
    .tooltip {
        color: gray;
        font-style: italic;
        font-size: 14px;
    }
    .sidebar-title {
        font-size: 18px;
        font-weight: bold;
        color: #c24838;
        margin-bottom: 10px;
    }
    .field-checkbox {
        margin-bottom: 10px;
    }
    .research-field {
        font-weight: bold;
        color: #c24838;
        font-size: 14px;
    }
    .alert-box {
        padding: 15px;
        margin-bottom: 20px;
        color: #c24838;
        background-color: #ffbaba;
        border-radius: 5px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle with custom styling
st.markdown("<h1 class='big-title'>AI Researcher Pro</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle-style'>Your AI-powered research assistant for all your research needs!</p>", unsafe_allow_html=True)

# Adding a tooltip with enhanced styling
st.markdown("""
    <p class='tooltip'>Tip: Ask specific research questions like "What are the latest trends in AI?" or "How to improve model accuracy in NLP?"</p>
    """, unsafe_allow_html=True)

# Connectivity Check
if not is_connected():
    st.error("⚠️ No internet connection. Please check your internet and try again.")
    st.stop()

# Define fields and their respective sub-fields
fields_dict = {
    "Computer Science": ["Artificial Intelligence", "Machine Learning", "Data Science", "Computer Vision", "Natural Language Processing"],
    "Medical": ["Biotechnology", "Genetics", "Neuroscience", "Immunology", "Medical Imaging"],
    "Physics": ["Quantum Mechanics", "Astrophysics", "Nuclear Physics", "Condensed Matter Physics", "Particle Physics"],
    "Chemistry": ["Organic Chemistry", "Inorganic Chemistry", "Biochemistry", "Physical Chemistry", "Analytical Chemistry"],
    "Engineering": ["Electrical Engineering", "Mechanical Engineering", "Civil Engineering", "Aerospace Engineering", "Biomedical Engineering"]
}

# Sidebar for selecting broad research fields
st.sidebar.markdown("<div class='sidebar-title'>Select a Broad Research Field</div>", unsafe_allow_html=True)
broad_field = st.sidebar.selectbox("Research Field", list(fields_dict.keys()))

# Show relevant sub-fields based on the broad field selected
st.sidebar.markdown(f"<div class='sidebar-title'>Select Sub-fields in {broad_field}</div>", unsafe_allow_html=True)
selected_subfields = []
for subfield in fields_dict[broad_field]:
    if st.sidebar.checkbox(f"🔍 {subfield}", key=subfield):
        selected_subfields.append(subfield)

# User input in the main layout
st.markdown("<div class='research-field'>Research Question</div>", unsafe_allow_html=True)
research_question = st.text_input("", "", help="Enter a clear research-related question")

# Function to get research papers from Google Scholar
def get_research_papers_from_scholar(topic, fields):
    papers = []
    for field in fields:
        search_query = scholarly.search_pubs(f"{topic} {field}")
        for i in range(5):  # Get top 5 results for each field
            try:
                paper = next(search_query)
                title = paper['bib']['title']
                abstract = paper.get('bib', {}).get('abstract', "No abstract available")
                url = paper.get('pub_url', "No URL available")
                papers.append({
                    "title": title,
                    "abstract": abstract,
                    "url": url,
                    "field": field
                })
            except StopIteration:
                break
    return papers

# Function to simulate AI researcher's response
def get_researcher_response(question, fields):
    subfields = ", ".join(fields)
    chat_completion = client.chat.completions.create(
        messages=[get_research_prompt(question, subfields)],
        model="llama3-groq-70b-8192-tool-use-preview",
    )
    answer = chat_completion.choices[0].message.content

    if "non-research" in answer.lower():
        return invalid_question_prompt(), None

    guidance = get_guidance_prompt(question, subfields)
    
    return answer, guidance


# Submit button with enhanced styling
if st.button("Submit"):
    if research_question and selected_subfields:
        with st.spinner(f"Researching your question in {', '.join(selected_subfields)}..."):
            answer, guidance = get_researcher_response(research_question, selected_subfields)
            
            if guidance:
                # Use Tabs with icons for better organization
                tab1, tab2 = st.tabs([f"🤖 AI Response", f"📄 Suggested Papers"])
                
                with tab1:
                    st.write("### Researcher's Answer:")
                    st.write(answer)
                    st.write("### Researcher's Guidance:")
                    st.write(guidance)
                
                with tab2:
                    st.write("### Suggested Research Papers:")
                    scholar_papers = get_research_papers_from_scholar(research_question, selected_subfields)
                    if scholar_papers:
                        for i, paper in enumerate(scholar_papers):
                            with st.expander(f"📄 Paper {i+1}: {paper['title']} ({paper['field']})"):
                                st.write(f"**Abstract**: {paper['abstract']}")
                                st.write(f"[Read Full Paper]({paper['url']})")
                    else:
                        st.info("No papers found, try a different query.")
            else:
                st.warning(answer)
    else:
        st.warning("Please enter a research question and select at least one sub-field before submitting.")
