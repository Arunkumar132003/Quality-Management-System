import streamlit as st
from dotenv import load_dotenv
load_dotenv()
from tempfile import NamedTemporaryFile
import os
import google.generativeai as genai
from lyzr import VoiceBot

from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()

# Fetch the Google API key from the environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Configure the GenerativeAI library with the Google API ke
genai.configure(api_key=google_api_key)

# Initialize GenerativeAI model
model = genai.GenerativeModel('gemini-pro')

def pass_mp(audio_file):
    # Retrieve API key from environment variable
    voicebot_api_key = os.getenv('VOICEBOT_API_KEY')

    # Initialize VoiceBot with the API key
    vb = VoiceBot(api_key=voicebot_api_key)
    
    # Transcribe the audio file to text
    transcript = vb.transcribe(audio_file)

    # Generate insights from the transcript using the GenerativeAI model
    prompt = """Extract important insights from transcript"""
    insights = model.generate_content([prompt, transcript])
    # Displaying the important insights from the transcipted text 
    st.markdown(f'<div style="border: 2px solid black; padding: 10px; background-color: white; width: fit-content; border-radius:8px;"><div style="text-align: center; color:black; font-weight: bold;">Insights</div><div style="color:black; ">{insights.text}</div></div>', unsafe_allow_html=True)
    lng= model.generate_content(['If the text is not in English, then translate the text into English',transcript])

    # Passing the transcripted text to classify func 
    classify(lng.text)

    # Passing the transcripted text to callLevelApi func 
    callLevelApi(lng.text)

# Function responsible for classifying the text
def classify(inp):
    role = """
    If the input is in other language translate it into English and perform the below operations
    labels= ['Flight Cancellation', 'Reschedule Flight', 'Flight Refund Related','Flight Delay Complaint', 'Staff Behavior Complaint', 'Miscellaneous']  Read the given text and assign the appropriate label(s) from labels array. Must choose only from the labels array dont add extra labels"."""
    response = model.generate_content([role, inp])

    # Display the classified output
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; height: 80px; padding: 10px; background-color: orange; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Category</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{response.text}</div></div>', unsafe_allow_html=True)
    st.markdown('<h4 style="margin-top: 20px; border-radius:8px; text-align: center; font-weight: bold; background: linear-gradient(to left,purple,pink); color: black;">CALL-LEVEL KPI</h4>', unsafe_allow_html=True)

# Function to calculate call-level KPIs
def callLevelApi(inp):
    # Code performs evaluating the First Call Resolution (FCR)
    st.markdown('#### First Call Resolution (FCR)')
    fcr_cond = "  If the input is in other language translate it into English and perform the below operations  Calculate the First Call Resolution (FCR) score from the text. The FCR score indicates the percentage of calls resolved on the first interaction, showcasing the agent's ability to solve issues efficiently without follow-up. Analyze the sentiment of the user's text. If the overall sentiment of the text is positive, assign an FCR score from 6 to 10 randomly based on how much positive was the text is. Otherwise, assign an FCR score randomly from 1 to 5"
    fcr = model.generate_content([fcr_cond, inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">First Call Resolution (FCR)</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{fcr.text}</div></div>', unsafe_allow_html=True)

    # Code performs evaluating the Customer Satisfaction Score (CSAT)
    st.markdown('#### Customer Satisfaction Score (CSAT)')
    csat_cond = "If the input is in other language translate it into English and perform the below operations (Calculate the Customer Satisfaction Score (CSAT) score from the text. The CSAT score indicates the percentage of calls resolved on the first interaction, showcasing the agent's ability to solve issues efficiently without follow-up. Analyze the sentiment of the user's text. If the overall sentiment of the text is positive, assign an CSAT score between 6 to 10 based on how much positive was the text is. Otherwise, assign an CSAT score between 1 to 5."
    csat = model.generate_content([csat_cond, inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Customer Satisfaction Score (CSAT)</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{csat.text}</div></div>', unsafe_allow_html=True)

    # Code performs evaluating the Call Resolution Rate
    st.markdown('#### Call Resolution Rate')
    crr_cond = "If the input is in other language translate it into English and perform the below operations. Must assign a value between 1 to 100 based on the condition . Calculate the Call Resolution Rate from the text. The Call Resolution Rate represents the percentage of calls that result in the caller's issue being resolved, indicating the effectiveness of the agents' problem-solving skills. Analyze the sentiment of the user's text. If the overall sentiment of the text is positive and it seems like the user has already spoken to the agent, assign a Call Resolution Rate between 55% to 100%. Otherwise, if it seems like the user is expressing a new issue or the sentiment is not overwhelmingly positive, assign a Call Resolution Rate between 1% to 54%."
    crr = model.generate_content([crr_cond, inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Call Resolution Rate</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{crr.text}</div></div>', unsafe_allow_html=True)

    # Code performs evaluating the Call transfer rate
    st.markdown('#### Call Transfer Rate')
    calltransfer_cond =""" 
       calltransfer= ["I'll forward the call", "Let me transfer you to", "I'll connect you with", "Transferring your call to", "Please hold while I transfer you to", "Let me get you in touch with", "I'll redirect you to", "You'll be speaking with", "I'll pass you to", "Connecting you to", "Hold on while I transfer you to", "I'm transferring you to", "I'll get someone else to help you", "Let me find someone who can assist you", "I'll pass this on to someone who can help", "You'll need to speak with", "You'll need to contact", "I'll hand this over to", "You'll need to get in touch with", "I'll send you over to", "You'll need to reach out to", "I'll refer you to", "I'll direct you to","forward", "transfer", "connect", "redirect", "speak", "pass", "hand", "refer", "direct"]

       Evaluate the text and determine if it contains any words or phrases related to call transfer.If the text includes any of the following phrases or similar words, based on how many times the words occurs, calculate and return the result in output, if no words related to call transfer then return output as 0%.
    """ 
    calltransfer= model.generate_content([calltransfer_cond,inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Call Transfer Rate</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{calltransfer.text}</div></div>', unsafe_allow_html=True)


    # Code performs evaluating the Call Rating
    st.markdown('#### Call Rating')
    callrating_cond=""" 
        If the input is in other language translate it into English and perform the below operations
        poor_quality_labels = [
        "sorry", "i can't get you", "i can't hear your voice", "voice is not audible", "poor connection", "call dropped", "difficult to    understand", "background noise", "distorted voice", "echo", "muffled voice", "network issue", "bad audio quality","can't hear you clearly", "can you repeat that?", "losing connection", "static noise", "lagging", "breaking up", "trouble hearing", "audio distortion", "call quality", "can't understand", "dropped calls", "incomprehensible", "interference", "low volume", "noisy background", "signal strength", "technical difficulties", "weak signal", "call cut off", "call interruption", "call problems", "call trouble","communication issues", "disconnected call", "phone problem", "poor reception", "sound issues"
        ]
        Analyze the text, whether the text contains the words that's present in  poor_quality_labels or the words that was similar to in the words present in poor_quality_labels, based on the occurance of the words caculate the call rate in percentage from 1 to 100 , if no words was present , return any value greater than 90 (must return any value with symbol percentage).
        Important Note: Don't display the text or senetence just return only the call rate percentage.
    """
    callrate= model.generate_content([callrating_cond,inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Call Rate</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{callrate.text}</div></div>', unsafe_allow_html=True)

    # Code performs evaluating the Error Rate
    st.markdown('#### Error Rate')
    misinfo_cond=""" 
      If the input is in other language translate it into English and perform the below operations.
      misinformation_words = ["Incorrectly stated", "Mistakenly", "Erroneously", "Inaccurately", "Misinformed", "Wrongly", "Falsely", "Incorrect", "Not true", "Apologies, we were mistaken", "Correction", "Reevaluation", "Clarification", "Contrary to what was stated", "I misspoke", "I stand corrected", "Contrary to earlier information", "My earlier statement was inaccurate", "Upon further review", "Upon double-checking", "Falsehood", "Error", "Mistake", "Misinterpretation", "Misrepresentation", "Flawed", "In error", "Not accurate", "Not correct", "Contradictory", "Not factual", "Not reliable", "Misleading", "Misconception", "Inconsistency", "Inexact", "Misunderstanding"]

      Analyze the text ,like whether the text contains the words that is present in the misinformation_words or the words similar to words in misinformation_words , what you must return -> (must dont return any text return value only) assing a error rate between 10 to 100 , if no words match then return 0
    """
    misinfo= model.generate_content([misinfo_cond,inp])
    st.markdown(f'<div style="margin-top:20px; border: 2px solid white; padding: 10px; background-color: yellow; width: 700px; border-radius:8px;"><div style="text-align: center; color:white; font-weight: bold; background-color: black; padding: 5px;">Error Rate</div><div style="text-align: center; color:black; font-weight: bold; margin-bottom:20px;">{misinfo.text}</div></div>', unsafe_allow_html=True)


def main():
    st.markdown(
    "<h1 style='text-align: center;'>Quality Management System</h1>",
    unsafe_allow_html=True
    )
    uploaded_file = st.file_uploader("Upload an audio file", type=["mp3"])

    if uploaded_file is not None:
        with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
            temp_file.write(uploaded_file.getvalue())
            temp_filename = temp_file.name

        st.audio(uploaded_file, format='audio/mp3')

        if st.button("Process Audio"):
            pass_mp(temp_filename)
        
        temp_file.close()

if __name__ == "__main__":
    main()