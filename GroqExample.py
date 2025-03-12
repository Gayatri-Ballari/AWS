from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
os.environ["HUGGINGFACEHUB_API_TOKEN"]=HUGGINGFACEHUB_API_TOKEN

# Initialize model
def result(): 
repo_id="mistralai/Mistral-7B-Instruct-v0.2"
llm=HuggingFaceEndpoint(repo_id=repo_id,max_length=128,temperature=0.7,token=HUGGINGFACEHUB_API_TOKEN)
    prompt= "write a poem about ocean"
    response=llm.invoke(prompt) #y invoke.? or is there any other way to use invoke
    return response.get("result")

def main():
    final_result = result()
    print(final_result)

if __name__ == "__main__":
    main()
