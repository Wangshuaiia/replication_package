### Replication Package Description

This replication package provides the necessary resources to reproduce the main components of our project, which was developed within the context of a truck manufacturing company. Due to confidentiality constraints, we are unable to share details regarding the APIs, API specifications, CAN signals, and Virtual Vehicle information used in our project. However, this package includes the implementation of core methodologies, the prompts and templates utilized, and workflow diagrams illustrating the processes.

All prompts have been carefully sanitized to ensure the removal of sensitive information. The package also includes runnable example scripts that demonstrate how these prompts and templates can be applied, enabling users to effectively reproduce the described methods.

### Package Directory Structure
```
.
├── README.md
├── prompt
│   ├── TestCaseGeneration_demo.py
│   ├── info_match_demo.py
│   ├── signature_data.py
│   └── spapi_signatures.py
├── template
│   ├── gen_code_demo.py
│   ├── get.py.jinja
│   └── post_put.py.jinja
└── workflow_figure
    ├── doc-retrieval.pdf
    └── spapi-workflow.pdf
```

### Directory Contents

#### 1. `prompt` Directory
The `prompt` directory contains the prompts used for invoking large language models (LLMs) and runnable example scripts demonstrating their application. 

- **Prompt Optimization:** Using the DSPy framework, we optimized the prompts and encapsulated the DSPy signatures in `spapi_signatures.py`. These signatures define consistent input-output formats for each step of the process.
- **Templates Integration:** To ensure reproducibility, templates defining the fixed formats for input and output are included within `signature_data.py`.
- **Usage Example:**
  - `info_match_demo.py` demonstrates the integration of DSPy signatures and templates.
  - `TestCaseGeneration_demo.py` showcases the Chain-of-Thought approach for generating test cases, with detailed constraints and generation logic.

#### 2. `template` Directory
The `template` directory contains Jinja templates for generating test code from test cases:

- **Templates:**
  - `get.py.jinja`: Template for APIs using GET methods.
  - `post_put.py.jinja`: Template for APIs using POST or PUT methods.
- **Usage Example:** `gen_code_demo.py` demonstrates how to use these Jinja templates to generate test code effectively.

#### 3. `workflow_figure` Directory
The `workflow_figure` directory provides visual references for the project workflows:

- `spapi-workflow.pdf`: An overview of the complete workflow.
- `doc-retrieval.pdf`: A detailed diagram of the document retrieval process.

### Reproducibility and Support
This replication package has been meticulously organized to facilitate easy and accurate reproduction of our methods. If you encounter any issues or have further questions, please feel free to contact us.

