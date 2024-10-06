# <a name="ai-resumemate"></a> ResumeMate: AI-Powered Resume Analyzer and Career Advisor

## Table of Contents
- [Detailed Breakdown of the Code](#detailed-breakdown) 
- [Code Breakdown by Segments](#code-breakdown-by-segments)
- [Technologies Used](#technologies-used)
- [How To Run the Code](#how-to-run-the-code)
- [Contributing](#contributing)

## <a name="detailed-breakdown"></a> Detailed Breakdown of the Code
This code creates a Streamlit application called ResumeMate, which leverages Google's Generative AI (Gemini) to analyze resumes, identify strengths and weaknesses, and recommend job roles based on the candidate's CV. The application also provides a text-to-speech feature, allowing users to listen to resume insights aloud.

The app is interactive and has two major functionalities:

1. **Home Page:** A user-friendly interface introducing the tool and its capabilities, including a contact form for inquiries.
2. **Analyze Resume:** Users upload their resume and provide a job description. The AI then analyzes the resume, offering a summary, identifying strengths and weaknesses, recommending suitable roles, and even providing final thoughts and CV improvement suggestions.

## Code Breakdown by Segments

1. **Imports and Setup:**
   
<img width="722" alt="AI ResuemMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/11.png?raw=true">

This segment imports the necessary libraries and initializes the environment:

* **Streamlit:** Used for building the web interface.
* **Google Generative AI:** To process text input (such as resume analysis).
* **PyPDF2:** For extracting text from uploaded PDF resumes.
* **pyttsx3:** For text-to-speech conversion.
* **dotenv:** To securely manage API keys.

2. **Core Functionality**

<img width="722" alt="AI ResuemMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/12.png?raw=true">

This function interacts with the Gemini AI model, sending the resume data as input and receiving relevant responses.

3. **Resume Analysis Functions**

These functions define specific tasks to analyze the resume text, such as summarizing the resume, identifying strengths/weaknesses, and suggesting job roles.

<img width="722" alt="AI ResumeMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/13.png?raw=true">

4. **Text-to-Speech**

<img width="722" alt="AI ResumeMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/14.png?raw=true">

This function uses pyttsx3 to convert text (such as resume summaries or recommendations) to speech, making it accessible for users who prefer auditory feedback.

5. **Streamlit User Interface**

The following section builds the interactive web application using Streamlit. There are two pages:

* **Home:** Describes the tool's purpose and capabilities, includes contact information.
* **Analyze Resume:** Allows users to upload a resume, input a job description, and receive AI-driven insights.

<img width="722" alt="AI ResumeMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/15.png?raw=true">

This section provides a seamless user experience, guiding the user through resume analysis tasks like summarizing or matching the resume with job descriptions.

## Technologies Used
1. **Streamlit:** A powerful Python library used for building interactive web apps quickly.
2. **Google Generative AI (Gemini):** Used to process and analyze natural language input, allowing the extraction of meaningful insights from resumes.
3. **PyPDF2:** Helps extract text from PDF resumes.
4. **pyttsx3:** Used to add text-to-speech capabilities, making the app accessible to a broader audience.
5. **Python-dotenv:** Handles the loading of environment variables, particularly for secure API key management.

## How To Run the Code
1. **Clone the Project:** Ensure you have a local copy of the project repository.

2. **Install Required Libraries:** The requirements.txt file contains all the necessary dependencies. To install them, run:

<img width="722" alt="AI ResumeMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/8.png?raw=true">

3. **Set Up API Keys:**

* Create a .env file in the project root.
* Add your Google API key for Generative AI in the .env file as follows:

<img width="722" alt="AI Voice Translator" src="https://github.com/Dev-Godswill/picture-files/blob/main/17.png?raw=true">

4. **Run the Application:** To launch the Streamlit app, execute the following command in your terminal:
   
<img width="722" alt="AI ResumeMate" src="https://github.com/Dev-Godswill/picture-files/blob/main/18.png?raw=true">

5. **Upload a Resume:**

* Navigate to the "Analyze Resume" page.
* Upload a PDF version of your resume.
* Paste the job description in the provided area.
* Use the available buttons to analyze your resume, extract insights, or receive feedback.

## Contributing
Contributions to this project is welcome! If you'd like to contribute, please follow these steps:
- Fork the project repository. 
- Create a new branch: git checkout -b feature/your-feature-name. 
- Make your changes and commit them: git commit -am 'Add your commit message'. 
- Push the changes to your branch: git push origin feature/your-feature-name. 
- Submit a pull request detailing your changes.

*Feel free to modify and adapt the project to your needs. If you have any questions or suggestions, please feel free to contact me: godswillodaudu@gmail.com*.
