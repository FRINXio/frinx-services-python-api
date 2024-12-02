from pathlib import Path

import click
from datamodel_code_generator import DataModelType, InputFileType
from datamodel_code_generator import generate as generate_pydantic
from graphql import build_schema, print_schema


@click.command()
@click.option('--input_path', '-i', required=True, type=click.Path(exists=True, file_okay=True),
              help='Path to single GraphQL file or folder with multiple GraphQL schemas.')
@click.option('--output_path', '-o', required=True, type=click.Path(),
              help='Path to where generated Pydantic classes will be placed.')
def generate(input_path: str, output_path: str):
    if not output_path.endswith('.py'):
        click.echo(f'Failed. The parameter --output_path has to contain python file.')
        return

    schema = join_graphql_files(input_path=input_path)
    if schema == "":
        click.echo(f'Failed. There are no GraphQL schema to generate Pydantic model.')
        return

    generate_pydantic(
        input_=schema,
        input_file_type=InputFileType.GraphQL,
        output=Path(output_path),
        output_model_type=DataModelType.PydanticV2BaseModel,
        snake_case_field=True,
        use_standard_collections=True,
    )
    click.echo(f'Successful')

def join_graphql_files(input_path: str) -> str:
    path = Path(input_path)

    schema: str
    if path.is_dir():
        schemas = []
        for file in path.glob("**/*.graphql"):
            with open(file, "r", encoding="utf-8") as f:
                schemas.append(f.read())
        schema = print_schema(build_schema("\n".join(schemas)))
    elif path.is_file():
        with open(path, "r", encoding="utf-8") as f:
            schema = print_schema(build_schema(f.read()))
    else:
        click.echo(f'Failed. Input has to by GraphQL file or directory with GraphQL files.')

    return schema


if __name__ == "__main__":
    generate()
