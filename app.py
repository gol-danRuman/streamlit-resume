from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Ruman Dangol"
PAGE_ICON = ":wave:"
NAME = "Ruman Dangol"
DESCRIPTION = """
Friendly software engineer starting journey from 2018 with proven cloud and security
skills. Seeking to deliver robust solutions. At
Fusemachines, I worked as a team member that
received the best in-house project of 2019. An
enthusiastic team player and deep creative
thinker.
"""
EMAIL = "rumancha12@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/ruman-dangol-013b0111a/",
    "GitHub": "https://github.com/gol-danRuman",
    "Twitter": "https://twitter.com/ruman_goldan",
}
PROJECTS = {
    "🏆 Dionysus: Development of a web and mobile application aimed at tracking mental health through social media channels",
    "🏆 Epistemic: Development of a web platform facilitating research and access to published papers, including automation of data retrieval using Python or Bash scripts",
    "🏆 Codehub: A coding platform utilized for completing course projects, offering educational resources and a mentor forum for students",
    "🏆 Fuse AI: An AI education program by Fusemachines, providing quality AI education globally to individuals, educational institutions, and organizations",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 5 years of experience as a Senior Software Engineer, specializing in delivering robust solutions and receiving recognition for the best in-house project of 2019.
- ✔️ Proficiency in React.JS, Python, and AWS, demonstrated through full-stack development and leadership roles in client projects.
- ✔️ Extensive experience in chatbot systems, Kubernetes Secret, Velero, and Scaffold in Codehub, showcasing versatility and expertise in diverse projects.
- ✔️ Bachelor of Software Engineering and pursuing Master in Computer Engineering, providing a strong educational foundation.
- ✔️ Actively participated in Everest Hackathon, demonstrating dedication to professional growth and collaboration.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Programming: Python, JavaScript, Java, PHP
- 📊 Data Visulization: Plotly, Seaborn
- 📚 Modeling: Logistic regression, linear regression, decition trees
- 🗄️ Databases: Postgres, MongoDB, MySQL, DynamoDB, Redis, ElasticSearch
- ☁️  Cloud: AWS, GCP, Azure
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History")
st.write("---")

# --- JOB 1
st.write("🚧", "**Senior Software Engineer | Fusemachines Inc.**")
st.write("02/2021 - Present")
st.write(
    """
- ► Led a team of 10 members as a Team Lead in a client project, demonstrating leadership and coordination skills 
- ► Utilized React.JS, Python, and AWS for client projects, showcasing proficiency in full-stack development and cloud computing
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Software Engineer | Fusemachines Inc.**")
st.write("01/2018 - 02/2021")
st.write(
    """
- ► Engaged in the fuse.ai project, providing students with an AI learning platform.
- ► Completed an ML intern training program focusing on Hand Recognition OCR.
- ► Gained proficiency in DevOps tools such as AWS and Docker.
"""
)



# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Accomplishments")
st.write("---")
for project in PROJECTS:
    st.write(f"{project}")