from pathlib import Path
import streamlit as st
from PIL import Image

# PATH SETTINGS
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"
profile_pic = current_dir / "assets" / "profile_pic.jpeg"


# GENERAL SETTINGS
PAGE_TITLE = "Digital Resume | Luis Ruiz-Santiago"
PAGE_ICON = ":wave:"
NAME = "Luis Ruiz-Santiago"
DESCRIPTION = """
I am a Data Analyst experienced in building intelligent systems. My work ranges from deploying serverless applications on AWS and developing AI agents with RAG capabilities, to creating interactive dashboards in Tableau and Streamlit. I leverage Python, Generative AI, and cloud platforms to drive data-driven decision-making and digital transformation.
"""

EMAIL = "ldruizsan@proton.me"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/luisruiz1",
    "Github": "https://www.github.com/ldruizsan",
    "Tableau Public": "https://public.tableau.com/app/profile/luis.ruiz.santiago"
}

PROJECTS = {
    "EPA Air Quality Data Collection & Visualization - Use autonomous AI agents to retrieve air quality data using the AQS API": {
        "link": "https://github.com/ldruizsan/lindy_agent",
        "tags": ["Python", "AI Agents", "Error handling", "API Requests", "Email Notifications"]
    },
    "Pet Medication Calendar - Flask app to track pet medication schedules": {
        "link": "https://github.com/ldruizsan/PetMedicationCalendar",
        "tags": ["Flask", "Python", "Data Visualization", "Web App", "HTML"]
    },
    "AI Agents in Chemical Engineering - Agent swarm for chemical engineering problem solving, with RAG system": {
        "link": "https://github.com/ldruizsan/chem_eng_agents",
        "tags": ["Python", "AI Agents", "RAG", "Chemical Engineering"]
    },
    "Airline Sentiment Analysis - Streamlit app showing sentiment analysis from user tweets": {
        "link": "https://airlines-sentiment-001.streamlit.app/",
        "tags": ["Streamlit", "Python", "NLP", "Sentiment Analysis"]
    },
    "Maven Analytics Toy Store Analysis - Tableau visualization analyzing store performance": {
        "link": "https://public.tableau.com/app/profile/luis.ruiz.santiago/viz/MavenMexicoToyStoreChallenge/MavenToyCompanyinMexico",
        "tags": ["Tableau", "Data Visualization", "Analytics"]
    },
    "Beta Parameter and CAPM Financial Analysis - Jupyter notebook analyzing stock valuation": {
        "link": "https://github.com/ldruizsan/python-capm-finance",
        "tags": ["Python", "Finance", "Jupyter Notebook"]
    },
    "Data Analysis and Visualization - Jupyter notebook analyzing US pollution data": {
        "link": "https://gist.github.com/ldruizsan/56cbce888b288daefd14a27d73c8b479",
        "tags": ["Python", "Data Analysis", "Visualization", "Jupyter Notebook"]
    },
    "Cloud deployment - Automated deployment of a serverless e-commerce store using AWS CodeBuild": {
        "link": "https://github.com/ldruizsan/cloudmart",
        "tags": ["AWS", "Docker", "AWS EC2", "Serverless", "AWS EKS", "Terraform", "DynamoDB","AWS CodeBuild"]
    },
    "Marketing Dashboard - Excel analysis of marketing campaign performance and customer segmentation": {
        "link": "https://1drv.ms/x/c/e99d4a59bb58b556/EXq6iWgyrapBrLc_Xmh95SoBp23rcHxgvq3396qM4pZkmA?e=EG4Obu",
        "tags": ["Excel", "Data Analysis", "Data Visualization","Marketing"]
        }
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("Welcome to my digital resume!")

# LOAD ASSETS AND CSS
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    pdfbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# HERO SECTION
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=350)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📄 Download Resume",
        data = pdfbyte,
        file_name = resume_file.name,
        mime = "application/octet-stream"
    )
    st.write(EMAIL)

# SOCIAL MEDIA LINKS
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

# EXPERIENCE AND QUALIFICATIONS
st.subheader("Experience & Qualifications")
st.write("""
         - ✅ Experience in digital transformation projects
         - ✅ Perform data mapping, data cleaning and validation, data analysis, and dashboards
         - ✅ Practical understanding of statistical principles to provide insights
         - ✅ Prioritize data protection
         - ✅ Certified in AWS, Azure, Databricks, and Lean Sig Sigma Yellow Belt
         """
         )
 # SKILLS
st.subheader("Skills")
st.write("""
         - Programming: Python (Pandas,Numpy, Scikit-learn), SQL
         - Data Visualization: Excel, Tableau, Plotly, Matplotlib, Seaborn, IBM Cognos
         - Databases: PostgreSQL, MongoDB, MySQL, DB2
         - Cloud platforms: AWS, Azure, Databricks, Snowflake, dbt, IBM
         - ITSM: Jira, ServiceNow
         - Generative AI: Prompt Engineering, ChatGPT, Claude, Gemini, DeepSeek, M365 Copilot
        """
)

# WORK HISTORY
st.write("---")
st.subheader("Work History")
st.write("**Technology Architect Analyst | Accenture**")
st.write("06/2022 - 12/2024")
st.markdown(
    """
    - Staffed across client engagements in digital transformation, cloud migration, and systems modernization for clients in the finance, fast food, and retails sectors
    - Spearheaded documentation and testing frameworks for a multiplatform SaaS application, including authoring dozens of user stories for QA teams, create a Product Playbook detailing feature entry points, cross-platform workflows, and ideal user paths to drive testing efficiency, and develop a Testing Matrix to standardize post-release validation, reduce duplication risk. Progress was tracked using Jira
    - Led data validation and cleanup for legacy system modernization, ensuring accuracy for cloud migration, identify data gaps by comparing transaction logs to application outputs
    - Revamped training documentation, and design a database workflow diagram to accelerate onboarding of client teams
    - Managed client-facing slides for sprint progress, risks, and blockers to improve transparency and maintain communication
    - Monitored 20+ Linux servers for SLA compliance to ensure uptime, resolve critical issues, and deploy patches as well as automate alerts via ServiceNow and reduce response time.
    """
, unsafe_allow_html=True) #, unsafe_allow_html=True # Add this if you are using st.markdown instead of st.write

st.write("**Fulfillment Center Associate I | Amazon**")
st.write("09/2021 - 04/2022")
st.write("""
    - Ensure fast and accurate transfer of 2000-2500 items per day from inventory to packaging with a low DPMO count
    - Stow items to add them to inventory, perform simple quality test to ensure the number of items in a bin match what is shown on the website, and pack the items securely for shipment
    - Follow 5S guidelines to maintain a clean and safe work station
        """)

# PROJECTS
st.write("---")
st.subheader("Projects")

# Create a grid with 3 columns
columns = st.columns(3, gap="medium")  # 3 columns with medium spacing

for index, (project, details) in enumerate(PROJECTS.items()):
    col = columns[index % 3]
    with col:
        st.markdown(
            f"""
            <div class="project-tile">
                <a href="{details['link']}" style="font-size: 16px; font-weight: bold; text-decoration: none; color: #d22682;">{project}</a>
                <p style="margin: 5px 0; font-size: 14px;"><strong>Tools:</strong> {", ".join(details["tags"])}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )