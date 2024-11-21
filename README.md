### Replication Package Overview

This replication package contains all necessary resources to reproduce our study, structured for clarity and ease of use. Below is a detailed explanation of the directory structure and the purpose of each component:

#### **Directory Structure**
```plaintext
.
├── prompt
│   ├── TestCaseGeneration.py
│   ├── signature_data.py
│   └── spapi_signatures.py
├── README.md
├── template
│   ├── get.py.jinja
│   └── post_put.py.jinja
└── workflow_figure
    ├── doc-retrieval.pdf
    └── spapi-workflow.pdf
```

#### **File Descriptions**

1. **Prompt Folder**
   - The `prompt` folder stores all the prompts used for each invocation of the Large Language Model (LLM). These prompts have been optimized using the DSPy framework. Specifically:
     - The file `spapi_signatures.py` contains the DSPy signatures used in our implementation. These signatures are designed to standardize the input and output formats for each step.
     - Templates to ensure consistent formatting of inputs and outputs are also defined in `signature_data.py`.
   - For test case generation, we adopted a Chain-of-Thought reasoning approach. The specific constraints and methods for generating test cases are detailed in the `TestCaseGeneration.py` file.

2. **Template Folder**
   - The `template` folder includes Jinja templates for generating test code from test cases. 
     - `get.py.jinja`: A template specifically tailored for GET API calls.
     - `post_put.py.jinja`: A template designed for POST or PUT API calls.

3. **Workflow Figure Folder**
   - The `workflow_figure` folder contains reference diagrams illustrating the workflow:
     - `spapi-workflow.pdf`: Provides an overview of the entire workflow process.
     - `doc-retrieval.pdf`: Details the specific procedures involved in the document retrieval phase.

This package has been carefully organized to facilitate replication and comprehension of our study. Each folder and file plays a distinct role in demonstrating the integration of DSPy-based prompt optimization, test case generation, and workflow visualization.
