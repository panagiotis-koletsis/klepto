#Create custom model first
ollama create Financial-Advisor-model -f model_fun/Financial-Advisor-llama3.py
ollama create Financial-Advisor-model -f model_fun/Financial-Advisor-phi3.py
ollama create Financial-Advisor-model -f model_fun/Financial-Advisor-gemma2-9b.py
ollama create Financial-Advisor-model -f model_fun/Financial-Advisor-gemma2-27b.py

pip install langchain_community
pip install pypdf