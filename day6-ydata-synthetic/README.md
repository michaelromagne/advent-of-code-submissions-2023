# Ydata-synthetic

<img src="../img/ydata.png" alt="ydata_logo" width="250"/>

Ydata is a package to generate synthetic tabular and time-series data leveraging the state of the art generative models.

**My opinion :**
That's the kind of library I was looking for in my previous job on Fraud Detection in e-commerce at Ubisoft. I tested approches like AnoGAN there like the one showcased by LogicalClocks [here](https://developer.nvidia.com/blog/detecting-financial-fraud-using-gans-at-swedbank-with-hopsworks-and-gpus/), [and the associated git repo](https://github.com/logicalclocks/aml_end_to_end). It was working but the fact that we can decouple the model from data augmentation and master it properly
is much more appealing.

However, I would not recommend Ydata-synthetic for production use cases, it's not robust enough : no working CI, no unit test, some pull requests have been pending for 2 years,... I think they prefer to maintain their other library that is more successful, ydata-profiler.

Moreover, the "State of the art" generative models are GANs, they could do better with LLMs now, it's a bit outdated as the field moves so fast.


TODO 
tuto ydata + video ?

