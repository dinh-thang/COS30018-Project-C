from langchain import HuggingFaceHub

API_KEY = ""
MODEL_SRC = "ThangDinh/qthang-finetuned"

llm = HuggingFaceHub(repo_id=MODEL_SRC, huggingfacehub_api_token=API_KEY)

print(llm("Tell me a joke about data scientist"))
