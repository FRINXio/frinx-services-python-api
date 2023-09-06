# frinx-services-python-api

This repository serves as a central hub for the Frinx Machine backend service APIs, represented in Pydantic format. 
Its primary objectives are to maintain a historical record of API alterations, enhance the visibility of 
version-to-version changes, and bolster compatibility maintenance within conductor workers.


## API to Pydantic Transformation

### Transforming REST APIs
To transform REST APIs, we rely on Swagger as our source of truth. We employ the [datamodel-codegen](https://github.com/koxudaxi/datamodel-code-generator) tool for this 
transformation process.

### Transforming GraphQL Schemas
When it comes to transforming GraphQL schemas, we extract the JSON schema directly from the service.
To accomplish this, we make use of the [graphql-pydantic-converter](https://github.com/FRINXio/frinx-services-python-api/tree/main/utils/graphql-pydantic-converter) tool.

## Release process

In this repository is housed several Python packages. Each of these packages serves as a Pydantic representation of either a REST API or a GraphQL schema, tailored to a specific backend service.

### Workflow:

- Whenever a new version of the backend service is released, it triggers an automatic GitHub action. This action initiates the transformation process, converting the API from either REST or GraphQL format.

- Upon successful transformation, a GitHub action generates a Pull Request (PR) containing the changes.

- Subsequently, tests are expected to be executed on this PR to ensure the integrity and functionality of the newly transformed code.

- After the PR is reviewed and approved, it is merged into the main branch.

- Once merged, another GitHub action is triggered, responsible for releasing a package with an associated tag to maintain version control. Only changes in RELEASE.md invoke tag creation.

## Installation

The best course of action would be to refer to your package manager's documentation for comprehensive guidance. 
However, here are some straightforward examples of usage with Poetry.


```bash
# inventory package, example with branch usage
poetry add git+ssh://git@github.com/FRINXio/frinx-services-python-api.git.git@main#subdirectory=inventory/python

# inventory package, example with tag usage
poetry add git+ssh://git@github.com/FRINXio/frinx-services-python-api.git.git@v2.0.0#subdirectory=inventory/python
```

## Usage
Once you've installed the apis, you can use them in your Python projects. 
Import the required modules and use the provided functionality to build requests with input validation.

```python
import requests
from typing import Any

from frinx_api.uniconfig.rest_api import DryrunCommit
from frinx_api.uniconfig.dryrun.manager.dryruncommit import Input
from frinx_api.uniconfig.dryrun.manager.dryruncommit import TargetNodes


def class_to_json(dataclass: Any) -> Any:
    return dataclass.json(exclude_none=True, by_alias=True, exclude_defaults=True)


response = requests.request(
    url='http://uniconfig:8181/rests' + DryrunCommit.uri,
    method=DryrunCommit.method,
    data=class_to_json(
        DryrunCommit.request(
            input=Input(
                do_rollback=True,
                target_nodes=TargetNodes(
                    node=['IOS01']
                )
            )
        )
    )
)
```
