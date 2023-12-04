# Quivr

<img src="../img/quivr.png" alt="quivr_logo" width="300"/>

Quivr is your second brain. Or actually, your multiple second brains.

Quivr brings the power of generative AI on your [local machine in less than 10 minutes](https://www.youtube.com/watch?v=cXBa6dZJN48). Based on RAG, you can create multiple "Brains" with specific domain knowledge that you are able to query at will. [Here](https://github.com/StanGirard/quivr/blob/4c89812832860591fb344719e7ed1200c529910b/docs/docs/Developers/contribution/chains/qa.md?plain=1#L25) is an overview of Quivr chain, with Langchain and [Supabase
vector](https://supabase.com/vector). Supabase also presented Quivr in a short [article here](https://supabase.com/customers/quivr).

Quivr needs an openAI api key to work, or can also do the job with [Ollama]() running locally, which is a strong plus if you want to keep your data safe (and if your machine can handle it).

One of the current limitation of Quivr is that the maximum context size is pretty low, 32k tokens for gpt-4, 4096 tokens for LLaMa 2. Chunk sizes for embedded documents is usually 512 tokens. It means that we are able to get 62 chunks of documents. For local models, it can be a bigger issue. This is a temporary problems as models are accepting bigger and bigger context sizes.  
If this limitation is too restrictive, you can also look at [other types of LLM chains](https://python.langchain.com/docs/modules/chains/document/), like Refine, Map Reduce and Map re-rank. 

**My opinion :** Overall, Quivr is a neat library and RAG is very powerful so I may create a few brains in the upcoming days, it may be fun and satisfying. It could also have huge impact in companies, with brains shared across teams.
