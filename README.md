
# GenAI-based Quality Management System for Airline Travel Call Centers

This web application is developed as a Quality Management System (QMS) specifically designed for airline travel call centers. The system utilizes Generative AI capabilities to process call recordings, extract meaningful insights, and evaluate the performance of call center operations. The application leverages the Lyzr AI API for transcription and the Google API for language processing.

# Note
Please provide only a single audio file in MP3 format. Avoid sending audio files within a ZIP archive to ensure easy access and compatibility. Thank you!

# Demo
Check out the live demo of the Quality Management System [here](https://qualitymanagementsystem.streamlit.app/).

## Preview
![3](https://github.com/Arunkumar132003/Web-development/assets/96881025/4c59203f-1718-484f-8649-3ccdab308d93)

![4](https://github.com/Arunkumar132003/Web-development/assets/96881025/2bd6d19e-d5a6-42c5-914b-0b20450dc262)

![5](https://github.com/Arunkumar132003/Web-development/assets/96881025/afe3a1c3-e224-4816-8a5f-037cd483c07a)

![6](https://github.com/Arunkumar132003/Gemini-Projects/assets/96881025/5046328b-8be4-4d3b-968d-1d1c89863240)


## Key Features

### Transcription of audio files to text

The system employs Lyzr VoiceBot, an advanced speech-to-text technology, to accurately transcribe audio recordings of calls made to airline travel call centers. By leveraging Lyzr VoiceBot, the system converts spoken words into written text, enabling easier analysis of call content and facilitating the extraction of valuable insights.

### Extraction of insights from transcriptions using Generative AI

With the assistance of the Gemini model, the system extracts crucial insights from transcribed call recordings. These insights encompass sentiment analysis, identification of key topics or issues, and patterns in customer-agent interactions. The Gemini model's advanced training enables nuanced analysis, facilitating the extraction of valuable insights from call conversations.

### Classification

The classify function translates the input text into English if needed and then assigns appropriate labels from a predefined array of categories. These categories include topics like 'Flight Cancellation', 'Reschedule Flight', 'Flight Refund Related', 'Flight Delay Complaint', 'Staff Behavior Complaint', and 'Miscellaneous'. The function ensures that only labels from this predefined array are assigned to the input text.

### Calculation of various Key Performance Indicators (KPIs)

The model analyzes a variety of Key Performance Indicators (KPIs) to evaluate call quality and agent performance. These KPIs encompass metrics such as First Call Resolution (FCR) , Customer Satisfaction Score (CSAT), Call Resolution Rate , Call Transfer Rate, Call Rating, Error Rate.By providing actionable insights, these KPIs enable call center managers to identify areas for improvement and optimize operations.


### Evaluation of call-level KPIs

Integrating call-level KPIs into a comprehensive Quality Management System empowers airline call centers to enhance customer service and agent performance. First Call Resolution (FCR) measures issue resolution efficiency, while Customer Satisfaction Score (CSAT) gauges customer happiness. Call Resolution Rate evaluates problem-solving success, Call Transfer Rate highlights training gaps, and Call Rating assesses call quality. Error Rate ensures information accuracy, collectively driving operational efficiency and customer satisfaction.

