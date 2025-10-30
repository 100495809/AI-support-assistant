# AI-support-assistant

The goal was to design and implement a simple **AI-powered support assistant** that can automatically classify customer messages and analyze their sentiment using Natural Language Processing (NLP)

---
Overview

The use case simulates a logistics company that receives daily messages from drivers and clients.  
These messages typically involve questions about shipment status, delivery issues, or payment and invoice problems.  
The system automatically processes each message and assigns it to a category, while also detecting the sentiment (positive, negative, or neutral)

---
Features

- **Message Classification:**  
  Categorizes messages into one of three groups:
  - Shipment Status
  - Delivery Issue
  - Payment / Invoice

- **Sentiment Analysis:**  
  Used a pretrained **Hugging Face Transformer model**   to determine whether each message expresses a positive, negative, or neutral tone

- **Data Display:**  
  Shows all messages with their predicted categories and sentiments,  
  as well as a count of how many messages fall into each category

---
Project Structure

ai-support-assistant/
|
|-- data/
| -- messages.csv # Input messages
|
|-- src/
| -- main.py
| -- classifier.py # Logic for message classification
| -- sentiment.py # Hugging face sentiment analysis
| -- display.py # Output formatting
| -- utils.py # CSV reading
| 
|
|--requirements.txt # Dependencies
|-- Dockerfile # Containerization setup
|-- README.md # Documentation

---
## How to Run the Project

**Create and activate a virtual environment**

python -m venv .venv
.venv\Scripts\Activate.ps1


**Install dependencies**

pip install -r requirements.txt


**Run the program**

python src/main.py


**Example Output**

#### Classification Results ####
message                                         category           sentiment
Hi, can you tell me the status of shipment...  Shipment Status    Neutral
My delivery arrived late and the box was...    Delivery Issue     Negative
Everything went smoothly today, thank you!     Other              Positive

#### Category Counts ####
Delivery Issue       4
Shipment Status      3
Payment / Invoice    2
Other                1

---
Details

Programming Language: 
Python

Libraries Used:
    - pandas – for handling CSV data and tabular output

    - transformers – for loading the Hugging Face sentiment model
    
    - torch – used by the model