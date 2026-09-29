# -*- coding: utf-8 -*-
"""Syllabus se English + Roman Urdu chapters generate karta hai.
Chalane ka tareeqa:  python scripts/gen_content.py
Chapters ko baad mein aap khud bhi edit/expand kar sakti hain."""
import os, textwrap

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EN_DIR = os.path.join(ROOT, "docs")
UR_DIR = os.path.join(ROOT, "i18n", "ur-Latn", "docusaurus-plugin-content-docs", "current")

# Har topic: (naam, English explanation, Roman Urdu explanation)
M = [
 dict(slug="module-01-python-foundations", pos=1, wr="2-6",
  t=("Python Foundations", "Python Ki Buniyad"),
  intro=("Learn the core of Python: syntax, control flow, functions, data structures, files, errors and OOP.",
         "Is module mein Python ki buniyad seekhengay: syntax, control flow, functions, data structures, files, errors aur OOP."),
  weeks=[
   ("Week 2", [
    ("Variables, Data Types, Operators", "Understand data types, declare variables, and use arithmetic, logical and comparison operators.", "Alag alag data types, variables banana, aur arithmetic, logical aur comparison operators ka istemal."),
    ("Conditional Statements", "Use if, elif and else to make decisions in programs.", "Programs mein faisla karne ke liye if, elif aur else ka istemal."),
   ]),
   ("Week 3", [
    ("Loops & Iterations", "Repeat tasks with for and while loops, plus break and continue.", "for aur while loops se kaam dohrana, sath break aur continue."),
    ("Functions, Lambda, Modules", "Write reusable code blocks, anonymous (lambda) functions, and import Python modules.", "Dobara istemal hone wala code (functions), lambda functions, aur modules import karna."),
   ]),
   ("Week 4", [
    ("Python Data Structures", "Organize data with lists, tuples, dictionaries and sets.", "Lists, tuples, dictionaries aur sets se data ko munazzam karna."),
    ("File Handling", "Read from and write to files for persistent storage.", "Data ko mehfooz rakhne ke liye files parhna aur likhna."),
   ]),
   ("Week 5", [
    ("Exception Handling", "Handle errors gracefully with try, except and finally.", "try, except aur finally se errors ko saleeqe se sambhalna."),
    ("Object-Oriented Programming", "Classes, objects, inheritance and encapsulation.", "Classes, objects, inheritance aur encapsulation ka taaruf."),
   ]),
  ],
  cls=["Student Grading System (OOP)", "Salary/Billing System (OOP)"],
  home=["Employee Record System (file handling)", "Library Management System (file handling)"]),

 dict(slug="module-02-python-for-data-science", pos=2, wr="7-10",
  t=("Python for Data Science", "Data Science Ke Liye Python"),
  intro=("Work with NumPy, Pandas and visualization libraries to explore and present data.",
         "NumPy, Pandas aur visualization libraries se data ko explore aur present karna."),
  weeks=[
   ("Week 7", [
    ("NumPy Core Operations", "Arrays, vectorized operations and mathematical functions for fast numerical work.", "Arrays, vectorized operations aur mathematical functions se tez numerical kaam."),
    ("Pandas DataFrames", "Create, index and manipulate tabular data.", "Tabular data ko banana, index karna aur badalna."),
   ]),
   ("Week 8", [
    ("Data Cleaning & Transformation", "Clean, normalize and prepare data for analysis.", "Data ko saaf karna, normalize karna aur analysis ke liye tayyar karna."),
    ("Handling Missing Values", "Find and manage missing or null values.", "Missing ya null values ko dhoondna aur handle karna."),
   ]),
   ("Week 9", [
    ("Merging, GroupBy", "Combine datasets and aggregate them for analysis.", "Datasets ko jorna aur aggregation karna."),
    ("Data Visualization (Matplotlib, Seaborn, Plotly)", "Build charts, plots and interactive visuals.", "Charts, plots aur interactive visualizations banana."),
   ]),
  ],
  cls=["COVID Dataset Exploratory Data Analysis (EDA)", "Sales Dashboard using Pandas + Plotly"],
  home=["E-commerce Customer EDA", "Weather Data Analysis Notebook"]),

 dict(slug="module-03-statistics-and-math-for-ml", pos=3, wr="11-14",
  t=("Statistics and Math for ML", "ML Ke Liye Statistics Aur Math"),
  intro=("The statistics, probability and linear algebra that machine learning is built on.",
         "Statistics, probability aur linear algebra jin par machine learning khari hai."),
  weeks=[
   ("Week 11", [
    ("Descriptive Statistics", "Summarize data with mean, median, mode, variance and standard deviation.", "Mean, median, mode, variance aur standard deviation se data ka khulasa."),
    ("Probability & Distributions", "Probability basics and the Normal, Binomial and Poisson distributions.", "Probability ki basics aur Normal, Binomial, Poisson distributions."),
   ]),
   ("Week 12", [
    ("Hypothesis Testing", "Use statistical tests to make data-driven decisions.", "Statistical tests se data ki bunyad par faisle karna."),
    ("Covariance & Correlation", "Measure relationships between variables.", "Variables ke darmiyan taalluq napna."),
   ]),
   ("Week 13", [
    ("Linear Algebra Basics", "Vectors, matrices and the operations ML relies on.", "Vectors, matrices aur ML mein kaam aane wale operations."),
    ("Cost Functions & Gradients", "Loss functions and gradient-based optimization.", "Loss functions aur gradient par mabni optimization."),
   ]),
  ],
  cls=["Company Sales Statistical Report", "Correlation Study (any dataset)"],
  home=["Hypothesis Testing Assignment", "Finance/Stock Statistical Exploration"]),

 dict(slug="module-04-machine-learning", pos=4, wr="15-21",
  t=("Machine Learning", "Machine Learning"),
  intro=("The full ML workflow plus core supervised and unsupervised algorithms.",
         "Poora ML workflow aur bunyadi supervised aur unsupervised algorithms."),
  weeks=[
   ("Week 15", [
    ("ML Pipeline", "The end-to-end workflow from data collection to deployment.", "Data jama karne se deployment tak poora workflow."),
    ("Feature Engineering", "Create, transform and select features that improve models.", "Aise features banana, badalna aur chunna jo model behtar karein."),
    ("Data Preprocessing", "Handle missing values, encode categoricals and scale features.", "Missing values, categorical encoding aur feature scaling."),
   ]),
   ("Week 16", [
    ("Train/Test Split & Cross Validation", "Split data to evaluate models and avoid overfitting.", "Model parakhne aur overfitting se bachne ke liye data ki taqseem."),
    ("Linear Regression", "Predict continuous values using a linear relationship.", "Linear taalluq se continuous values ki peshgoi."),
   ]),
   ("Week 17", [
    ("Logistic Regression", "Predict categories and model probabilities.", "Categories ki peshgoi aur probabilities ki modeling."),
    ("Decision Trees", "Tree-based models for classification and regression.", "Classification aur regression ke liye tree-based models."),
   ]),
   ("Week 18", [
    ("Random Forest", "An ensemble of trees for better accuracy and less overfitting.", "Trees ka majmua jo accuracy barhata aur overfitting kam karta hai."),
    ("Gradient Boosting (XGBoost/LightGBM)", "Advanced boosting for high-performance predictions.", "Behtareen performance ke liye advanced boosting algorithms."),
   ]),
   ("Week 19", [
    ("K-Nearest Neighbors (KNN)", "Instance-based learning for classification and regression.", "Instance-based learning, classification aur regression dono ke liye."),
    ("Support Vector Machine (SVM)", "Maximum-margin classifiers for complex data.", "Pechida data ke liye maximum-margin classifiers."),
   ]),
   ("Week 20", [
    ("K-Means Clustering", "Partition data into clusters by similarity.", "Mushabihat ki bunyad par data ko clusters mein baantna."),
    ("Hierarchical Clustering", "Build a hierarchy of clusters (agglomerative or divisive).", "Clusters ka hierarchy banana (agglomerative ya divisive)."),
   ]),
   ("Week 21", [
    ("Principal Component Analysis (PCA)", "Reduce dimensions while keeping key information.", "Ahem maloomat rakhte hue dimensions kam karna."),
   ]),
  ],
  cls=["House Price Prediction", "Customer Segmentation (K-Means)", "Loan Eligibility Prediction", "Fraud Detection Model"],
  home=["Churn Prediction", "Sales Forecasting", "Credit Risk Scoring Model", "HR Attrition Prediction"]),

 dict(slug="module-05-deep-learning", pos=5, wr="22-26",
  t=("Deep Learning", "Deep Learning"),
  intro=("Neural networks, computer vision and sequence models for text and time series.",
         "Neural networks, computer vision aur text/time-series ke liye sequence models."),
  weeks=[
   ("Week 22", [
    ("Perceptron, Forward & Backpropagation", "The basic neural unit and how weights update during learning.", "Neural network ki bunyadi ikai aur seekhte waqt weights ka update hona."),
    ("Activation & Loss Functions", "Non-linearity and error measurement for optimization.", "Non-linearity aur error napne ke functions."),
   ]),
   ("Week 23", [
    ("Convolutional Neural Networks (CNNs)", "Networks specialized for images and feature extraction.", "Images aur feature extraction ke liye khaas networks."),
    ("Transfer Learning", "Reuse pre-trained models like ResNet and VGG for new tasks.", "ResNet, VGG jaise pehle se trained models ko naye kaam ke liye istemal karna."),
   ]),
   ("Week 24", [
    ("Text Cleaning", "Preprocess text before feeding it to models.", "Text ko model mein dene se pehle saaf karna."),
    ("Embeddings", "Turn text into numeric vectors that capture meaning.", "Text ko aise numeric vectors mein badalna jo matlab samajhte hain."),
   ]),
   ("Week 25", [
    ("RNN, LSTM, GRU", "Sequential models for time series and text.", "Time series aur text ke liye sequential models."),
   ]),
  ],
  cls=["CNN-Based Image Classifier", "LSTM Movie Review Sentiment Analyzer", "Transfer Learning (ResNet/VGG)"],
  home=["Dogs vs Cats Classification", "Spam Detection using Deep Learning"]),

 dict(slug="module-06-mlops", pos=6, wr="27-30",
  t=("MLOps", "MLOps"),
  intro=("Take models to production: APIs, containers, tracking, CI/CD and monitoring.",
         "Models ko production tak pohanchana: APIs, containers, tracking, CI/CD aur monitoring."),
  weeks=[
   ("Week 27", [
    ("ML Deployment Concepts", "How models are deployed into production.", "Models production mein kaise deploy hote hain."),
    ("FastAPI for ML Deployment", "Build APIs that serve real-time predictions.", "Real-time predictions dene wali APIs banana."),
   ]),
   ("Week 28", [
    ("Docker Containers", "Package ML apps for consistent, scalable deployment.", "ML apps ko yaksan aur scalable deployment ke liye package karna."),
    ("MLflow for Tracking", "Track experiments, metrics and models.", "Experiments, metrics aur models ko track karna."),
   ]),
   ("Week 29", [
    ("CI/CD Introduction", "Continuous Integration and Deployment for ML pipelines.", "ML pipelines ke liye Continuous Integration aur Deployment."),
    ("Logging & Monitoring", "Track model performance in production.", "Production mein model ki performance par nazar rakhna."),
   ]),
  ],
  cls=["Build and Deploy an ML Model with FastAPI", "MLflow Tracking Implementation"],
  home=["Dockerized ML Microservice", "Full Deployment Pipeline with Monitoring"]),

 dict(slug="module-07-big-data-and-cloud", pos=7, wr="31-34",
  t=("Big Data and Cloud", "Big Data Aur Cloud"),
  intro=("Process large datasets with Hadoop and Spark, and run workloads on the cloud.",
         "Hadoop aur Spark se bara data process karna aur cloud par kaam chalana."),
  weeks=[
   ("Week 31", [
    ("Hadoop Concepts", "Distributed storage and processing with Hadoop.", "Hadoop ke zariye distributed storage aur processing."),
    ("HDFS, MapReduce, YARN", "Hadoop's storage, processing and resource-management parts.", "Hadoop ke storage (HDFS), processing (MapReduce) aur resource management (YARN) hissay."),
   ]),
   ("Week 32", [
    ("RDDs", "Fault-tolerant, parallel data processing in Spark.", "Spark mein fault-tolerant, parallel data processing."),
    ("DataFrames", "Work with structured data efficiently in Spark.", "Spark mein structured data ke sath kaam."),
    ("Spark SQL", "Query structured data with SQL-like operations.", "SQL jaise operations se data query karna."),
    ("Spark MLlib", "Scalable machine learning with MLlib.", "MLlib ke sath scalable machine learning."),
   ]),
   ("Week 33", [
    ("S3 Storage", "Scalable object storage in the cloud.", "Cloud mein scalable object storage."),
    ("EC2 Basics", "Virtual servers and compute in the cloud.", "Cloud mein virtual servers aur compute."),
    ("Databricks / EMR", "Cloud platforms for Spark and Hadoop workloads.", "Spark aur Hadoop ke liye cloud platforms."),
    ("Deploying ML Models on Cloud", "Serve ML models on cloud infrastructure.", "ML models ko cloud par deploy karna."),
   ]),
  ],
  cls=["ETL Pipeline using PySpark", "Spark MLlib Model Training", "Cloud-Based Data Processing Workflow"],
  home=["Big Data Batch Processing", "Cloud-Based Data Lake Setup", "Real-Time Processing Mini Project (optional)"]),

 dict(slug="module-08-generative-ai-llms", pos=8, wr="35-38",
  t=("Generative AI (LLMs)", "Generative AI (LLMs)"),
  intro=("Transformers, LLMs, prompting, fine-tuning and Retrieval-Augmented Generation (RAG).",
         "Transformers, LLMs, prompting, fine-tuning aur Retrieval-Augmented Generation (RAG)."),
  weeks=[
   ("Week 35", [
    ("Transformers", "The core architecture behind modern language models.", "Jadeed language models ke peeche bunyadi architecture."),
   ]),
   ("Week 36", [
    ("BERT and GPT (Conceptual)", "Principles of popular NLP models.", "Mash-hoor NLP models ke usool."),
    ("Tokenization", "Break text into tokens for model processing.", "Text ko tokens mein todna taake model samajh sake."),
   ]),
   ("Week 37", [
    ("Prompt Engineering", "Write effective prompts to steer LLM output.", "LLM ke jawab ko sahi rukh dene ke liye behtar prompts likhna."),
    ("Fine-Tuning (LoRA/QLoRA)", "Adapt pre-trained models with lightweight techniques.", "Halki phulki techniques se pehle se trained models ko apne kaam ke mutabiq dhalna."),
    ("RAG Systems", "Retrieval-Augmented Generation for context-aware answers.", "Context ke mutabiq jawab dene ke liye Retrieval-Augmented Generation."),
    ("Vector Databases (FAISS/Pinecone)", "Store and search embeddings for semantic retrieval.", "Embeddings ko store karna aur semantic search karna."),
   ]),
  ],
  cls=["ChatGPT-style Q/A Bot", "RAG System with Vector Database"],
  home=["Domain-Fine-Tuned Q/A LLM", "Text Summarization or Content Generator"]),

 dict(slug="module-09-agentic-ai", pos=9, wr="39-41",
  t=("Agentic AI", "Agentic AI"),
  intro=("Build AI agents that use tools, plan, remember and collaborate.",
         "Aise AI agents banana jo tools istemal karein, plan karein, yaad rakhein aur mil kar kaam karein."),
  weeks=[
   ("Week 39", [
    ("What are AI Agents?", "Autonomous AI agents and what they can do.", "Khud-mukhtar AI agents aur unki salahiyatein."),
    ("Tool-Using Agents", "How agents call external tools to perform tasks.", "Agents kaam karne ke liye bahri tools kaise use karte hain."),
   ]),
   ("Week 40", [
    ("Reasoning & Planning", "Decision-making and multi-step task planning.", "Faisla sazi aur multi-step tasks ki planning."),
    ("LangChain Agents", "Build agents with the LangChain framework.", "LangChain framework se agents banana."),
    ("CrewAI & AutoGen", "Multi-agent orchestration platforms.", "Multi-agent orchestration platforms."),
    ("Memory-Enabled Agents", "Let agents store and recall context.", "Agents ko context yaad rakhne ke qabil banana."),
   ]),
   ("Week 41", [
    ("Multi-Agent Systems", "Coordinate several agents on collaborative tasks.", "Kayi agents ko milkar kaam par lagana."),
   ]),
  ],
  cls=["AI Autonomous Data Analyst", "Multi-Agent System (Researcher + Writer + Reviewer)"],
  home=["Personal AI Assistant with Tools", "Automated Email + Reporting Agent System"]),
]

L = {
 "en": dict(week="Weeks", proj="Projects", cls="Class-Based Projects", home="Home-Based Projects", topics="What you will learn", key="Key idea", prac="Practice", prac_txt="Write your own short example for each topic above and run it before moving on.", nxt="Next module"),
 "ur": dict(week="Haftay", proj="Projects", cls="Class Projects", home="Ghar ke Projects", topics="Aap kya seekhengay", key="Ahem nuqta", prac="Mashq", prac_txt="Upar diye har topic ki apni chhoti misaal likhein aur agay barhne se pehle chala kar dekhein.", nxt="Agla module"),
}

def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def module_md(m, lang):
    i = 0 if lang == "en" else 1
    lab = L["en" if lang == "en" else "ur"]
    out = ["---", f"sidebar_position: {m['pos']}", f"title: \"Module {m['pos']:02d}: {m['t'][i]}\"", "---", "",
           f"# Module {m['pos']:02d}: {m['t'][i]}", "", f"**{lab['week']} {m['wr']}**", "", m["intro"][i], ""]
    for wk, topics in m["weeks"]:
        out += [f"## {wk}", ""]
        for name, en, ur in topics:
            out += [f"### {name}", "", (en, ur)[i], ""]
    out += [f"## {lab['prac']}", "", lab["prac_txt"], "", f"## {lab['proj']}", "",
            f"**{lab['cls']}**", ""] + [f"- {p}" for p in m["cls"]] + ["", f"**{lab['home']}**", ""] + [f"- {p}" for p in m["home"]] + [""]
    return "\n".join(out)

INTRO = {
 "en": """---
sidebar_position: 0
slug: /
title: Introduction
---

# AI and Data Science Book

Based on the SMIT AI and Data Science syllabus by Miss Javeria Hassan.

- **Duration:** 10 months (can extend to 11)
- **Level:** Beginner to Advanced
- **Prerequisites:** Basic programming is preferred but not mandatory.

## Week 1

Course introduction, expectations, roadmap overview, Python installation and IDE setup.

## Roadmap

| Module | Topic | Weeks |
|---|---|---|
""" + "\n".join(f"| {m['pos']} | {m['t'][0]} | {m['wr']} |" for m in M) + """

Use the language menu in the top bar to switch between English and Roman Urdu. The **Chatbot** page answers questions from this book.
""",
 "ur": """---
sidebar_position: 0
slug: /
title: Taaruf
---

# AI aur Data Science Book

Yeh book SMIT ke AI aur Data Science syllabus (Miss Javeria Hassan) par mabni hai.

- **Muddat:** 10 mahine (11 mahine tak barh sakti hai)
- **Level:** Beginner se Advanced
- **Zaroorat:** Programming ki basic maloomat behtar hai, lazmi nahi.

## Week 1

Course ka taaruf, umeedein, roadmap ka jaiza, Python install karna aur IDE setup.

## Roadmap

| Module | Mauzoo | Haftay |
|---|---|---|
""" + "\n".join(f"| {m['pos']} | {m['t'][1]} | {m['wr']} |" for m in M) + """

Upar menu se English aur Roman Urdu ke darmiyan badlein. **Chatbot** page is book se sawalon ke jawab deta hai.
""",
}

EXTRAS = {
 "en": ("Extra Skills", ["LinkedIn Profile Optimization", "Personal Branding", "MS Office", "Google Docs / Slides / Sheets", "Canva", "Presentations after each module", "Freelancing (Upwork / Freelancer)"], "Beyond technical skills, the course also covers career skills:"),
 "ur": ("Additional Skills", ["LinkedIn Profile Optimization", "Personal Branding", "MS Office", "Google Docs / Slides / Sheets", "Canva", "Har module ke baad presentations", "Freelancing (Upwork / Freelancer)"], "Technical skills ke ilawa course mein career skills bhi shamil hain:"),
}

for lang, base in (("en", EN_DIR), ("ur", UR_DIR)):
    write(os.path.join(base, "intro.md"), INTRO[lang])
    for m in M:
        write(os.path.join(base, m["slug"] + ".md"), module_md(m, lang))
    title, items, lead = EXTRAS[lang]
    write(os.path.join(base, "extra-skills.md"),
          f"---\nsidebar_position: 10\ntitle: {title}\n---\n\n# {title}\n\n{lead}\n\n" + "\n".join(f"- {x}" for x in items) + "\n")
print("done")
