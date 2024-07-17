import json

from langchain_community.document_loaders.pdf import PyPDFDirectoryLoader


DATA_PATH = "/home/kpanag/kleptoPdf"
PATH = "analysis.doc"

def load_data():
    path = 'data/prompts.json'
    with open(path) as f:
        j = json.load(f)
    prompts = prompt_list(j)
    return prompts

def prompt_list(j):
    prompts = []
    for i in range(len(j['prompts'])):
        prompts.append(j['prompts'][i]['prompt'])
    return prompts

def write_to_doc(analysis):
    with open("example.txt", "w") as file:
        # Write the string to the file
        file.write(analysis)



def pdf_reader():
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    print(document_loader)
    return document_loader.load()