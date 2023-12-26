# Open LLM by BentoML

<img src="../img/bentoml.png" alt="trulens" width="250"/>

OpenLLM is an open-source platform designed to facilitate the deployment and operation of large language models (LLMs) in real-world applications. With OpenLLM, you can run inference on any open-source LLM, deploy them on the cloud or on-premises, and build powerful AI applications.

On the big picture, OpenLLM is developed by BentoML team, which also develops BentoML a framework for building reliable, scalable, and cost-efficient AI applications. It comes with everything you need for model serving, application packaging, and production deployment.


**My opinion:** I have a lot to say on BentoML. They developed an awesome tool to package any kind of model and deploy it in a blink. Their concepts are clear, you define a service, your runners, and your API is up and running with good performances. It supports adaptive batching, multithreading out of the box with integrations with Triton or VLLM. I already use it on a day to day basis and it saves you a lot of time and allow small teams to deploy their services without the need of more developers.

Now with the OpenLLM library, you can pick trending LLMs on hugging face and deploy them as you would do with any kind of models. The VLLM integration is here to enhance inference performances. However the biggest drawback for me now is the lack of support of fine-tuned model deployments. I think that [ONNX serving](https://github.com/vllm-project/vllm/issues/195) is still not supported by VLLM and is not a clear point on the roadmap, which would be highly beneficial.

