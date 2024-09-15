
# AI Researcher Pro - Your Research Companion

AI Researcher Pro is an AI-powered research assistant designed to streamline your research workflow. The app uses Groq API for intelligent research assistance and Google Scholar to retrieve relevant papers based on user queries. The tool helps researchers ask domain-specific questions and get AI-driven answers, along with recommended papers from the research community.

## Features
- **AI-Powered Research**: Ask research questions in specific domains like Computer Science, Medical, Engineering, and more.
- **Research Paper Suggestions**: Get suggested papers directly from Google Scholar based on your question and selected sub-fields.
- **Customizable Fields**: Choose from multiple research domains and their respective sub-fields to narrow down your research.
- **Interactive User Interface**: User-friendly interface with enhanced styling and tooltips for better user experience.
- **Secure API Handling**: Uses `st.secrets` to securely handle API keys, making the app ready for hackathon environments.

## Tech Stack
- **Streamlit**: For creating the interactive web interface.
- **Groq API**: To generate AI-powered research responses.
- **Google Scholar**: For fetching research papers based on the query.
- **Python**: Core language used for application development.
- **st.secrets**: Used for secure environment variable management.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/ai-researcher-pro.git
   cd ai-researcher-pro
   ```

2. **Set Up Environment Variables**
   - Create a `secrets.toml` file in the `.streamlit` directory (if it doesn't exist):
     ```bash
     mkdir -p .streamlit
     nano .streamlit/secrets.toml
     ```
   - Add your Groq API key in the `secrets.toml` file:
     ```toml
     [general]
     GROQ_API_KEY = "your-groq-api-key-here"
     ```

3. **Install Dependencies**
   Use `pip` to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   Start the Streamlit app by running the following command:
   ```bash
   streamlit run app.py
   ```

## Usage

1. **Select a Research Field**: Choose a broad research field from the sidebar (e.g., Computer Science, Medical, Engineering, etc.).
2. **Select Sub-fields**: Based on the chosen research field, you can select specific sub-fields like AI, Data Science, Quantum Mechanics, and more.
3. **Enter Research Question**: Type a clear, research-related question in the provided text box.
4. **Submit**: Click the **Submit** button to get AI-generated answers and suggested research papers.
5. **View Results**: Check the AI response in the **AI Response** tab and view suggested research papers in the **Suggested Papers** tab.

## Example Queries
- "What are the latest trends in Machine Learning?"
- "How to improve model accuracy in Natural Language Processing?"
- "Current advancements in Quantum Mechanics?"
  
The app will return a tailored response based on your query and the sub-fields selected.

## Troubleshooting

- **No Internet Connection**: If the app shows a "No internet connection" error, ensure your device is connected to the internet.
- **Missing API Key**: If you encounter an error related to the API key, double-check your `secrets.toml` file for the correct `GROQ_API_KEY`.

## Contribution

Feel free to fork this project and submit a pull request if you'd like to contribute. You can also open an issue if you find bugs or have feature requests.

## License

This project is licensed under the MIT License.

---

