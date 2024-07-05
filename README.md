# LangChain Basics - Requirements

First major draft: July 5, 2024

# Quick Start

The objective of this repository is to test basic Gen AI applications using the LangChain eco-system: https://python.langchain.com/v0.2/docs/tutorials/

I have installed the required packages, got the relevant API keys, and tested the provided Jupyter notebooks plus a Python code.

After you clone the repository in your IDE, you can run on your shell terminal the following:

pip install -r requirements.txt

You will need the following environmental variables in your .env file:

OPENAI_API_KEY=""<br>
LANGCHAIN_API_KEY=""<br>
TAVILY_API_KEY=""<br>
ANTHROPIC_API_KEY=""<br>

The applications are as follows:
- Build a simple LLM application with LCEL https://python.langchain.com/v0.2/docs/tutorials/llm_chain/
    - BuildLLMAApp.ipynb
    - serve.py
- Build a chatbot https://python.langchain.com/v0.2/docs/tutorials/chatbot/
    - BuildChatbot.ipynb
- Build vector stores and retrievers https://python.langchain.com/v0.2/docs/tutorials/retrievers/
    - BuildRetrievalTextApps.ipynb
- Build an Agent fom LangChain https://python.langchain.com/v0.2/docs/tutorials/agents/
    - BuildAgent.ipynb
    - Agent.py

# Notes on my Gen AI Journey

For the record, I have done plenty of academic and industry research in econometrics but I am not a developer by any means. <br>
Prior to January 2024, I had not coded in Python or used Gen AI apps other than on my iPhone or a CoPilot on Slack or other graphical user interface. <br> 
While I expect the usage of  structured Gen AI applications will get easier with time, running the basic codes has required some investment. <br>
Let me share some of the lessons that I have learned in the process, perhaps you can benefit. <br>

## Python 

I had done some coding in my research career (most recently in R) but had to learn Python from the scratch. <br>
Python is free and easy to get at https://www.python.org/downloads/. Note that versioning matters. For some AI applications, <br>
you may actually need to use an older version of Python to get them to work.

To get started with Python, I have used https://www.datacamp.com/. There are some useful courses such as:
- Introduction to Python 
- Intermediate Python 
- Intermediate Importing Data in Python

DataCamp is very practically oriented and provides you with the basic framework to get things going. <br>
Also, it lets you learn in a dedicated environment, so you do not need to worry about setting up your Python editor, packages, etc. <br>
Each course is accompanied by videos and pdf presentations. However, at some point I needed to test the code on my own set up. <br>
To do that, I had to manually copy/paste the code from the presentations - for obvious reasons, DataCamp does not let you to get the code directly. <br>
(That being said, if it happens to be possible and you know how, please let me know). As a result, you are likely to outgrow DataCamp relatively quickly.

## Integrated Development Environment (IDE)

You will need to edit and run your code. I have started with Visual Studio (VS) code as it has provided a good integration with GitHub Copilot. <br>
However, it turned out to be an overkill for my needs at the time and I switched to PyCharm (Professional version). PyCharm is quite intuitive and I like <br>
how it works with Git/GitHub (more on this later). You can also run Jupyter notebook on it. <br> 
I noticed that researchers with a 'classical' background (statistics, economics, maths) tend to use Pycharm,<br>
while developers gravitate to VS code. As my skills are improving, this appears to where I am headed as well. <br>
For comparison of Pycharm, VS Code and other IDEs, see a Medium article by Simeon Emanuilov:<br>
https://medium.com/@simeon.emanuilov/the-best-python-ide-in-2024-d4f536b6b6a2

Btw, definitely subscribe to https://medium.com/ as it publishes excellent articles including very useful code snippets.

The links to PyCharm and VS code are:<br>

https://www.jetbrains.com/pycharm/ <br>
https://code.visualstudio.com/ <br>

## Git/GitHub

At some point, it will be useful to create a repository on GitHub. <br>
Note that Git is essentially a versioning software tool while GitHub is a platform where you can store your codes. <br>
https://github.com/ 

Some DataCam courses to get you started:
- Introduction to Git 
- Git Hub Concepts

I find the way PyCharm uses Git and links to GitHub more intuitive than using commands in a shell terminal. <br>
https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html

## Environmental Variables

You will be using several API keys for LangChain, OpenAI, etc. It is a good practice to store them in a dedicated file .env. <br>

There is a good Medium article that describes how this is done, see <br>
https://medium.com/@tophamcherie/using-environment-variables-in-python-66e9ca50f146

See envVar.py as a code snippet how to retrieve a particular API key.

## Management of Python Packages

Once you have installed a few packages in Python using the PIP command, it will be useful to make your environment replicable. <br>
Using requirements.txt is a simple way of doing this. First, I have followed instructions in the PyCharm documentation to create <br>
the requirements.txt file:<br>
https://www.jetbrains.com/help/pycharm/managing-dependencies.html#configure-requirements

However, when I opened the file, it only contained two items, which was clearly incorrect. Running <br>
*pip freeze > requirements.txt* <br>
in the command line has generated the file. You can install the packages in your PyCharm project as follows: <br>
*pip install -r requirements.txt*

Once you are ready to get closer to a replicable production-level implementation, Poetry is the tool that you may choose to deploy. <br>
I have worked on projects where Poetry was set up by someone. This has been quite convenient and effective. <br>
However, I have found installing Poetry on my own a bit tricky. If you would like to do that, the links below should get you started<br>
https://realpython.com/dependency-management-python-poetry/ <br>
https://python-poetry.org/ 

For a comparison of Requirements.txt vs Poetry, see: <br>
https://medium.com/@onurbaskin/pythons-poetry-vs-requirements-txt-df3efd1c7c13 

## Gen AI Providers and Tools

Obviously, you will need to set up access to Open AI, so you will need an API key, which is relatively affordable (I spend some £20/week):<br>
https://openai.com/ <br>

Sometimes it takes a bit of time to find where you can get the API key on the website of the provider. For the Open AI, it is here:<br>
https://platform.openai.com/api-keys

Clearly, there are very many other providers of the Large Language Models (LLMs). Some examples in LangChain use Chat Anthropic:<br>
https://www.anthropic.com/ <br>
https://api.python.langchain.com/en/latest/chat_models/langchain_anthropic.chat_models.ChatAnthropic.html <br>
https://console.anthropic.com/settings/plans <br>

To leverage on the power of LLMs, you will need to connect it to the web. Tavily is a good tool that accomplishes that:
https://tavily.com/ <br>
When you log in, I recommend you use your GitHub credentials. <br>
When I did that, I received free 1,000 API calls at https://app.tavily.com/home which gives you a good start.

## LangChain/LangGraph/LangSmith (vs DSPy)

Finally, you are ready to actually run the examples that are provided on the LangChain website - see the Quick Start of this file for the relevant links.

LangChain eco-system is useful for structuring Gen AI applications and creating a process (a pipeline) that can be improved. <br>
I believe that it will dominate the industry for some time as it is fairly comprehensive, (relatively) easy to deploy, 
and has good documentation support.

An alternative to the standard process of optimizing the pipeline is DSPy. While I view DSPy more as an alternative to the <br>
LangChain framework, the two can actually be integrated - see https://python.langchain.com/v0.2/docs/integrations/providers/dspy/

As you can see, getting to the point of actually **deploying**  LangChain can be a time-consuming exercise when you are starting from scratch. <br>
Here is where Data Camp comes in handy. In the course
Developing LLM Applications with LangChain, <br>
you can get a sense of how LangChain works in principle in a pre-set environment. Note that some of the course may be slightly outdated.

## Glossary
IDE - Integrated Development Environment <br>
LLM - Large Language Model <br>
VS - Visual Studio <br>