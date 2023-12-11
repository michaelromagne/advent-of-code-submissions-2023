# Phoenix

<img src="../img/arize.png" alt="arize" width="300"/>

Phoenix brings monitoring tools for your models and LLM Applications with very little configuration. You can do embedding analysis based on Umap, identify clusters and dig into them, to interpret drift or compare different model versions. 

[How UMAP works](https://umap-learn.readthedocs.io/en/latest/how_umap_works.html#how-umap-works)

<img src="../img/umap.png" alt="umap" width="800"/>

It's also possible to debug your RAG with traces, which help you to understand the internals of your application (search and retrieval in vector stores, embedding generation, external tools...):

<img src="../img/traces.png" alt="traces" width="800"/>

It's even possible to go further by visualizing your vector store. You just have to upload a corpus of your knowledge base along with your LLM application's inferences to help you troubleshoot hard to find bugs with retrieval. Bugs could be gaps in your documentation, queries that gave bad responses or failures to retrieve relevant context. It's a perfect tool for anyone using RAG.

<img src="../img/rag.png" alt="rag" width="800"/>


**My opinion:** I used Umap and hdbscan in the past but it feels like Arize AI really brang these "raw" libraries to life with this product. It helps so much to understand what is going on with such complex models !
