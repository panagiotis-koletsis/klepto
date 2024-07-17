import sys
from files import load_data, write_to_doc, pdf_reader
from model_fun import model


def main():
    print("Enter the text (press Ctrl+D or Ctrl+Z then Enter to finish):")
    text = sys.stdin.read()
    #load json as list
    prompts = load_data()

    res1 = model.ask_model1(text)
    print("Summary------\n")
    print(res1)

    analysis = """Analysis \n------ """
    for i in range(len(prompts)):
        response = model.ask_model(prompts[i],text)
        print(response,"\n")
        analysis = analysis + "Prompt \n------" + prompts[i] + "LLM Resonse \n------" + str(response) + "\n------"
        
#    print(analysis)  
    
    write_to_doc(analysis)
   
    
    
    
    
    # x = pdf_reader()
    # print(x)

    






if __name__ == "__main__":
    main()