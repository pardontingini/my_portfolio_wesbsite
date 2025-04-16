import streamlit as st
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl

# Function to send email
def send_email(name, email, message):
    try:
        # Email configuration
        sender_email = "tinginipardon@gmail.com"  # Replace with your email
        receiver_email = "tinginipardon@gmail.com"  # Your email where you want to receive messages
        password = "Tingini@123"  # Get password from Streamlit secrets
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = f"New Contact Form Message from {name}"
        
        # Email body
        body = f"""
        Name: {name}
        Email: {email}
        
        Message:
        {message}
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Create secure SSL context
        context = ssl.create_default_context()
        
        # Send email
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(sender_email, password)
            server.send_message(msg)
        
        return True
    except Exception as e:
        st.error(f"Error sending email: {str(e)}")
        return False

# Set page configuration
st.set_page_config(
    page_title="Pardon Tingini Portfolio",
    page_icon="👨‍💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to create header
def create_header():
    st.markdown("""
    <div style='background-color: #2c3e50; padding: 1rem; border-radius: 10px; margin-bottom: 2rem;'>
        <div style='display: flex; justify-content: center; gap: 2rem;'>
            <a href='#home' style='color: white; text-decoration: none;'>Home</a>
            <a href='#about' style='color: white; text-decoration: none;'>About</a>
            <a href='#projects' style='color: white; text-decoration: none;'>Projects</a>
            <a href='#skills' style='color: white; text-decoration: none;'>Skills</a>
            <a href='#contact' style='color: white; text-decoration: none;'>Contact</a>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Add custom CSS for better styling
st.markdown("""
    <style>
    .main {
        padding: 0.5rem;
        background-color: #f8f9fa;
    }
    
    .stButton>button {
        width: 100%;
        margin-top: 1rem;
        background-color: #4CAF50;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    
    .stButton>button:hover {
        background-color: #45a049;
    }
    
    .sidebar .sidebar-content {
        background-color: #2c3e50;
        color: white;
    }
    
    .sidebar .sidebar-content .sidebar-section {
        padding: 1rem;
    }
    
    .sidebar .sidebar-content .sidebar-section .sidebar-title {
        color: #ecf0f1;
        font-size: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .stRadio > div {
        background-color: #34495e;
        padding: 1rem;
        border-radius: 5px;
    }
       
    .stRadio > div > div {
        color: white;
    }
    
    .stTitle {
        color: #2c3e50;
        font-size: 2.5rem;
        margin-bottom: 2rem;
    }
    
    .stMarkdown {
        background-color: white;
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-bottom: 2rem;
    }
    
    .stImage {
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .stMarkdown h1 {
        color: #2c3e50;
        border-bottom: 2px solid #4CAF50;
        padding-bottom: 0.5rem;
    }
    
    .stMarkdown ul {
        list-style-type: none;
        padding-left: 0;
    }
    
    .stMarkdown li {
        padding: 0.5rem 0;
        border-bottom: 1px solid #eee;
    }
    
    .stMarkdown li:last-child {
        border-bottom: none;
    }
    
    /* Style for intro section text */
    .stMarkdown p, .stMarkdown h3 {
        color: #2c3e50;
    }
    
    /* Style for About page text */
    .stMarkdown ul {
        color: #2c3e50;
        font-size: 1.1rem;
        line-height: 1.6;
    }
    
    .stMarkdown ul li {
        margin-bottom: 0.5rem;
    }
    </style>
""", unsafe_allow_html=True)

# Create a sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Projects", "Skills", "Contact"])

# Home page
if page == "Home":
    create_header()
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(os.path.join(os.getcwd(), "static", "pardon1.jpg"), use_container_width=True)
    with col2:
        st.title("Hi👋, I'm Pardon Tingini🤓")
        st.markdown("""
        ### Welcome to My Portfolio Site! 😎
        
        Once Again, Hi there! Loosen up😉, I'm so excited to share my journey in technology with you.
        So Feel free to explore different sections of my life so far, atleast the proffesional bits. 
        Make use of the navigation menu on the left.
        """)
    
    # Add footer
    st.markdown("---")  # Horizontal line
    current_year = datetime.now().year
    footer = f"""
    <div style='text-align: center; padding: 20px; background-color: #f8f9fa; border-radius: 10px;'>
        <p>© {current_year} Pardon Tingini. All rights reserved.</p>
        <p>
            <a href='https://www.linkedin.com/in/pardon-tingini' target='_blank'>LinkedIn</a> |
            <a href='https://github.com/pardontingini' target='_blank'>GitHub</a> |
            <a href='https://twitter.com/tinginipardon' target='_blank'>Twitter</a>
        </p>
    </div>
    """
    st.markdown(footer, unsafe_allow_html=True)

# About page
elif page == "About":
    create_header()
    st.title("About Me")
    
    # Create two columns for About section
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### My Background
        I am a passionate tech enthusiast who began my journey with a degree in Information Systems at Midlands State University. 
        My internship at Regency Hotels provided foundational experience in IT support, networking, database management, and most important, people skills among other things. 
        A year after graduating, I took on a role as a project administrator in rural Chirumanzu, focusing on digital literacy and setting up a library and computer resource center. 
        This role expanded my skills in system design, user-centered approaches, and community engagement, inspiring me to pursue an MBA to have a holitic approach to organisations. 
        Along the way, I’ve also worked on freelance projects in consulting, networking, web development, and hardware/software repairs among others. I also learned to harness cloud technologies aong others.
        My career has been a rewarding journey of growth, and I’m excited for what’s next!!!.
        """)
        
        st.markdown("""
        ### Professional Journey
        - #Educational background
                    
                    Masters in Business Administration (MBA)
                        Midlands State University | 2025

                    Bachelor of Science (Honors) in Information Systems
                        Midlands State University | 2020
        - #Career milestones
                    
        - Key achievements
        - Future aspirations
        """)
    
    with col2:
        st.markdown("""
        ### Personal Interests
        - Hobbies and passions
                    
                -Discovering new tech
                -Art
                -Music
                -Cinematography
                -Sports and Fitness
                -Chess

        - Community involvement
                    
                -Teaching Computer literacy
                -Organising Chess tournaments
                -Literacy advocacy
                                -
        - Personal projects
        """)

# Projects page
elif page == "Projects":
    create_header()
    st.title("My Projects")
    
    # Project 1
    st.markdown("""
    ### Featured Project 1
    """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/300x200", use_container_width=True)
    with col2:
        st.markdown("""
        **Project Description:**  
        Detailed description of your project here.
        
        **Technologies Used:**  
        - Technology 1
        - Technology 2
        - Technology 3
        
        **Links:**  
        [GitHub Repository](#) | [Live Demo](#)
        """)
    
    # Project 2
    st.markdown("""
    ### Featured Project 2
    """)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("https://via.placeholder.com/300x200", use_container_width=True)
    with col2:
        st.markdown("""
        **Project Description:**  
        Detailed description of your project here.
        
        **Technologies Used:**  
        - Technology 1
        - Technology 2
        - Technology 3
        
        **Links:**  
        [GitHub Repository](#) | [Live Demo](#)
        """)

# Skills page
elif page == "Skills":
    create_header()
    st.title("Skills & Expertise")
    
    # Create three columns for different skill categories
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.markdown("""
        ### Programming Languages
        - Python
        - PHP
        - Java
        - C#
        """)
    
    with col2:
        st.markdown("""
        ### Frameworks & Libraries
        - Streamlit
        - Django
        - TensorFlow
        """)
    
    with col3:
        st.markdown("""
        ### Tools & Technologies
        - Git
        - Docker
        - AWS
        - SQL
        """)
    
    with col4:
        st.markdown("""
        ### Cloud Platforms
        - AWS
        - Azure
        """)
    
    with col5:
        st.markdown("""
        ### Additional Skills
        - Project Management
        - Team Collaboration
        - Problem Solving
        - Technical Writing
        """)

# Contact page
elif page == "Contact":
    create_header()
    st.title("Get in Touch")
    
    # Contact information in a two-column layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Connect With Me
        Feel free to reach out through any of these channels:
        
        **Email:** tinginipardon@gmail.com  
        **Phone:** +263 776 000 395  
        **Location:** Harare, Zimbabwe
        """)
    
    with col2:
        st.markdown("""
        ### Professional Profiles
        - [Linkedin Profile](https://www.linkedin.com/in/pardon-tingini)
        - [GitHub Profile](https://github.com/pardontingini)
        - [Portfolio Website](https://www.tinginipardon.com)
        - [Twitter Handle](https://twitter.com/tinginipardon)
        """)
    
    # Contact form
    st.markdown("""
    ### Send a Message
    """)
    with st.form("contact_form"):
        name = st.text_input("Name", placeholder="Enter your name")
        email = st.text_input("Email", placeholder="Enter your email")
        message = st.text_area("Message", placeholder="Enter your message here...", height=150)
        submit = st.form_submit_button("Send Message")
        
        if submit:
            # Validation
            errors = []
            
            # Name validation
            if not name.strip():
                errors.append("Please enter your name")
            
            # Email validation
            if not email.strip():
                errors.append("Please enter your email")
            elif "@" not in email or "." not in email:
                errors.append("Please enter a valid email address")
            
            # Message validation
            if not message.strip():
                errors.append("Please enter your message")
            elif len(message.strip()) < 10:
                errors.append("Message should be at least 10 characters long")
            
            # Display errors or success message
            if errors:
                for error in errors:
                    st.error(error)
            else:
                if send_email(name, email, message):
                    st.success("Thank you for your message! I'll get back to you soon.")
                else:
                    st.error("There was an error sending your message. Please try again later.")