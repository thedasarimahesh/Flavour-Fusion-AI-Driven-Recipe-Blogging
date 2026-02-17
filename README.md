🍲 Flavour Fusion: AI-Driven Recipe Blogging
Flavour Fusion is a cloud-based AI web application that generates customized, engaging, and well-structured recipe blogs using Google’s Generative AI. The platform allows users to input a recipe topic and desired word count, and the AI produces a detailed blog post tailored to their needs — all while entertaining users with a programmer joke during content generation.
________________________________________
📌 Project Overview
Flavour Fusion revolutionizes recipe blogging by automating content creation through Generative AI. Built using Streamlit and Google Gemini 2.5 Flash, the application enables food bloggers, chefs, and content creators to instantly generate high-quality recipe blogs.
Users simply enter a topic (e.g., Vegan Cake, Gluten-Free Bread) and specify word length. The AI then produces structured content including introduction, ingredients, preparation steps, tips, and serving suggestions.
To enhance user experience, the system displays a programmer joke while generating the blog — making the wait interactive and fun.
This project demonstrates practical implementation of LLMs in content automation and blogging workflows.
________________________________________
 Project Architecture
FLAVOUR-FUSION/
├── app.py                # Main Streamlit application
├── requirements.txt     # Project dependencies
├── README.md            # Documentation
└── venv/                # Virtual environment
________________________________________
🔧 Technologies Used
•	🧠 LLM Model: Google Gemini 2.5 Flash
•	🌐 Generative AI API: Google Generative AI (Vertex AI)
•	🖥️ Frontend + Backend: Streamlit
•	🐍 Programming Language: Python
•	📦 Environment: venv
•	🔑 API Integration: Gemini API Key 
________________________________________
💫 Project Workflow
1️⃣ User Input
•	User opens Streamlit app
•	Enters recipe topic
•	Specifies word count
Example:
•	Vegan Chocolate Cake — 1200 words
•	Quick Weeknight Dinners — 800 words
________________________________________
2️⃣ AI Processing
•	Input sent to Gemini 2.5 Flash
•	Prompt dynamically structured
•	Model generates blog content
________________________________________
3️⃣ Content Generation
AI creates:
•	Title
•	Introduction
•	Ingredients
•	Step-by-step preparation
•	Tips & variations
•	Serving suggestions
________________________________________
4️⃣ Joke Feature 🎭
While AI generates content:
•	App displays random programmer joke
•	Improves user engagement
Example:
“Why don’t programmers like nature? Too many bugs.”
________________________________________
5️⃣ Output Display
•	Generated blog shown in Streamlit UI
•	User can:
o	Copy content
o	Edit blog
o	Export for publishing
________________________________________
🧪 Real-World Use Case Scenarios
🥗 Scenario 1: Vegan Recipe Blogger
A vegan blogger inputs “Vegan Chocolate Cake – 1200 words.”
AI generates a detailed plant-based recipe blog ready for publishing.
________________________________________
🍝 Scenario 2: Busy Professional
User enters “Quick Weeknight Dinners – 800 words.”
AI produces concise, easy dinner recipes for daily planning.
________________________________________
🍞 Scenario 3: Gluten-Free Baker
Baker inputs “Gluten-Free Bread – 1500 words.”
AI delivers an in-depth gluten-free baking guide.
________________________________________
⚙️ Implementation Steps
1️⃣ Initialize Gemini 2.5 Flash
•	Generate Gemini API key
•	Configure authentication
________________________________________
2️⃣ Model Initialization
•	Load pre-trained Gemini 2.5 Flash model
•	Configure prompt parameters
________________________________________
3️⃣ Interfacing with Model
•	Pass topic + word count
•	Format structured prompt
________________________________________
4️⃣ Blog Generation
•	AI generates full recipe blog
•	Ensures readability + structure
________________________________________
5️⃣ Model Deployment
•	Integrated into Streamlit backend
•	Real-time response generation
________________________________________
6️⃣ Application Deployment
Deploy using Streamlit:
streamlit run app.py
________________________________________
▶️ How to Run the Project Locally
1️⃣ Clone Repository
git clone https://github.com/yourusername/flavour-fusion.git
cd flavour-fusion
________________________________________
2️⃣ Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
________________________________________
3️⃣ Install Dependencies
pip install -r requirements.txt
________________________________________
4️⃣ Configure API Key
Create .env file:
GEMINI_API_KEY=your_api_key
MODEL=gemini-2.5-flash
________________________________________
5️⃣ Run Application
streamlit run app.py
________________________________________
📚 Prior Knowledge Required
🧠 Large Language Models (LLMs)
LLMs are AI systems trained on massive text datasets to understand and generate human language.
Applications include:
•	Text generation
•	Chatbots
•	Translation
•	Summarization
•	Code generation
Examples:
•	ChatGPT
•	BERT
•	Gemini
________________________________________
🖥️ Streamlit
Required knowledge:
•	Building UI apps in Python
•	Widgets (text input, sliders)
•	API integration
•	Output rendering
________________________________________
🙌 Contributions
Contributions are welcome!
Steps:
1.	Fork repo
2.	Create branch
3.	Commit changes
4.	Raise PR 🚀
________________________________________
📬 Contact
📧 Email: dasarim9392@gmail.com
________________________________________
⭐ Star this repo if you found it useful
________________________________________

