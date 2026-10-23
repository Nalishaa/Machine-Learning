from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
llm = HuggingFacePipeline.from_model_id(
    model_id="Qwen/Qwen2.5-0.5B-Instruct",
    task = "text-generation",
    pipeline_kwargs = dict(
        temperature = 0.3,
        max_new_tokens = 100,
        do_sample = True
    )
)

model = ChatHuggingFace(llm = llm)

chat_history = [
    SystemMessage(content = 'You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    result = model.invoke(chat_history)
    response = result.content
    response =  response.split("<|im_start|>assistant")[-1]
    response =  response.replace("<|im_end|>", "").strip()
    chat_history.append(AIMessage(content = response))
    print("AI:", response)
    
print(chat_history)
