
# Title Of Your Project
Add a catchy title to your project. Something that people immediately know what you are doing

# Introduction & Goals
- Introduce your project to the reader
- Orient this section on the Table of contents
- Write this like an executive summary
  - With what data are you working
  - What tools are you using
  - What are you doing with these tools
  - Once you are finished add the conclusion here as well

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
  - [Connect](#connect)
  - [Buffer](#buffer)
  - [Processing](#processing)
  - [Storage](#storage)
  - [Visualization](#visualization)
- [Pipelines](#pipelines)
  - [Stream Processing](#stream-processing)
    - [Storing Data Stream](#storing-data-stream)
    - [Processing Data Stream](#processing-data-stream)
  - [Batch Processing](#batch-processing)
  - [Visualizations](#visualizations)
- [Demo](#demo)
- [Conclusion](#conclusion)
- [Follow Me On](#follow-me-on)
- [Appendix](#appendix)


# The Data Set

The dataset used is sourced from Kaggle: ["Credit Card Transactions Fraud Detection Dataset"](https://www.kaggle.com/datasets/kartik2112/fraud-detection)
This is a simulated credit card transaction dataset containing legitimate and fraud transactions. It contains credit card transaction details of Customers owning Credit Cards by various Merchants. 
Having worked in the banking domain, this was a dataset i could leverage domain experience and further build upon. The original dataset sourced from Kaggle has card transaction details merged alongwith detailed customer information in a single file, which was a bit problematic for me. So within my code I've split the dataset into 2 -> in a manner that one would expect credit card transactions data to stream through from a bank's credit card system: purely the transaction information. While we expect customer information to most likely flow in through the bank's customer repository or CRM system.

# Used Tools

![image](https://github.com/melba365/data_engineering/assets/26708646/db482d15-9272-437e-8232-d6c8e7a788f9)

Setup:

  On Local machine:
    
    - Data Source python code
    - Postman
    
  Docker:
   
    - FASTApi code image
    - Kafka
    - Spark


## Data Preparation
The credit card transactions .csv data has been transformed into json format, using a python code, so the json can be POST as a request to an API.

## Sourcing Data
In this scenario, a data pipeline has been built to pull data from the API and further buffer it through Kafka. A python code has been written to leverage FASTApi for the purposes of hosting the API using Uvicorn. 

## Buffer
Postman was used to simulate a POST request to this API. This data was further produced via Kafka on a message topic.

## Processing
Apache Spark was used as the processing framework. Spark Structured Streaming was leveraged to read the incoming stream and further process it to be stored.

## Storage
## Visualization

# Pipelines
- Explain the pipelines for processing that you are building
- Go through your development and add your source code

## Stream Processing
![image](https://github.com/melba365/data_engineering/assets/26708646/b8b2fde6-8694-4cd8-8ed6-6f6f51fcc8e5)


### Storing Data Stream
### Processing Data Stream
## Batch Processing
## Visualizations

# Demo
- You could add a demo video here
- Or link to your presentation video of the project

# Conclusion
Write a comprehensive conclusion.
- How did this project turn out
- What major things have you learned
- What were the biggest challenges

# Follow Me On
Add the link to your LinkedIn Profile

# Appendix

[Markdown Cheat Sheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
