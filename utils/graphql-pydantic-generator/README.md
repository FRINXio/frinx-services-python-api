# GraphQL Pydantic Generator

## Overview

A utility wrapper for datamodel-code-generator that generates Pydantic v2 model from single GraphQL schema file, or 
from directory that contains multiple GraphQL schema files including any nested subdirectories with other GraphQL
schema files.

## Usage

1. Activate or create a new virtualenv
```bash
user@ntb:~$ cd frinx-services-python-api/utils/graphql-pydantic-generator
user@ntb:~/frinx-services-python-api/utils/graphql-pydantic-generator$ poetry env use 3.10
```

2. Install the project dependencies
```bash
user@ntb:~/frinx-services-python-api/utils/graphql-pydantic-generator$ poetry install
```

3. Generate Pydantic model from GraphQL schema
```bash
user@ntb:~/frinx-services-python-api/utils/graphql-pydantic-generator$ poetry run generate --input_path ~/topology-discovery/topology_discovery/api/graphql/schemas/ --output_path ~/frinx-services-python-api/topology-discovery/python/frinx_api/topology_discovery/__init__.py
```

4. Fix 'Incompatible types in assignment' mypy error
```example
typename__: Optional[Literal['SynceDevice']] = Field(
    'SynceDevice', alias='__typename'
) # type: ignore
```