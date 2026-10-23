from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

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

messages = [
    SystemMessage(content = 'You are a helpful assistant'),
    HumanMessage(content = 'Tell me about LangChain')
]

result = model.invoke(messages)
messages.append(AIMessage(content=result.content))

print(messages)