# DVC

<img src="../img/dvc_logo.png" alt="dvc" width="250"/>


Data Version Control or DVC is a command line tool and VS Code Extension to help you develop reproducible machine learning projects:

    - Version your data and models. Store them in your cloud storage but keep their version info in your Git repo.
    - Iterate fast with lightweight pipelines. When you make changes, only run the steps impacted by those changes.
    - Track experiments in your local Git repo (no servers needed).
    - Compare any data, code, parameters, model, or performance plots.
    - Share experiments and automatically reproduce anyone's experiment.



**My opinion:** I have been using DVC for the last 2 years and this tool is the MUST HAVE in any MLOps stack. First, because their tool is minimal and the CLI tool is awesome. With git-like commands, you are able to version data, push and pull it in a blink. For collaboration, it's great.

Furthermore, Their method to handle storage is very smart. They use file hash values to create directories to store data, which makes it very fast to know if a file already exists in your cache. This way, when you use DVC to track your experiments, it saves you a lot of time by only running steps of your pipelines that have changed dependencies (inputs, script...).

Lastly, Iterative company as a whole is strong and has very well defined products : DVC, CML, MLEM, Studio... Congrats to this team !

