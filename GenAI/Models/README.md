# Components in LangChain
### 1. Models
- Model component is designed to facilitate interactions with various language models and embedding models.
- It abstracts the complexity of working directly with different LLMs, chat models, and embedding models, providing a uniform interface to communicate with them.
- This makes it easier to build applications that rely on AI-generated text, text embeddings for similarity search, and RAG (retrieval-augmented generation).


### Language Models
AI systems designed to process, generate and understand natural language text.

- LLMs - General-purpose models that is used for raw text generation. They take in a string or plain text as input and returns a string or plain text. Older models.

- Chat Models - Models that are specialized for conversational tasks. They take a sequence of messages as inputs and return chat messages as outputs (as opposed to using plain text). Newer models.

### Note on API-Based Models:
Some models demonstrated in the tutorial required paid API access or available usage credits, such as Hugging Face Inference Providers and OpenAI API models. I skipped these paid API-based implementations and focused on the local alternatives, which run on my machine without per-request API charges. Local models may require additional Python packages and model downloads to work.