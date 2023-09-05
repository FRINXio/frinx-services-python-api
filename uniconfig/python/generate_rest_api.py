import re
import ast
import yaml
import inspect

from argparse import ArgumentParser
from argparse import Namespace
from string import Template
from typing import Optional
from typing import Iterable
from typing import Any

DEFAULT_SOURCE_FILE = 'frinx_api/uniconfig/__init__.py'
DEFAULT_OUTPUT_FILE = 'frinx_api/uniconfig/rest_api.py'
ENTER = '\n'
SPACE = ' '
TAB = '\t'
NAN = ''


class CustomTemplate(Template):
    delimiter = '_'


class UniconfigRest:
    uri: str
    method: str
    request: Optional[Any]
    response: Optional[Any]


def _set_globals_for_template_cls() -> None:
    global _request, _response
    _request, _response = None, None


_set_globals_for_template_cls()


class _cls(UniconfigRest):
    uri = '_uri'
    method = '_method'
    request = _request
    response = _response


def parse_swagger_scheme(scheme: dict[str, Any], req_res_refs: Iterable[str]
) -> tuple[list[str], list[str]]:
    
    uniconfig_rest = CustomTemplate(inspect.getsource(_cls))
    imports, definitions = [], []
    
    def _upformat(s: str, delimiters: list[str]) -> str:
        for x in delimiters:
            s = s.replace(x, SPACE)
        return NAN.join([x.capitalize() for x in s.split(SPACE)])
    
    def _get_cls(endpoint: str, method: str, *, request: bool=False, response: bool=False) -> str:
        base = _upformat(endpoint, ['/', '-']).split('=')[0] + method.capitalize()
        return base + {request: 'Request', response: 'Response'}.get(True)

    def _get_service_name(endpoint: str) -> str:
        service = endpoint.split('/')[-1]
        match = re.search(r'\{(.*?)\}', service)
        if match:
            param = match.groups()[0].capitalize()
            service = service.split('=')[0]
            return _upformat(service, ['-']) + _upformat(param, ['-'])
        return _upformat(service, ['-'])

    def get_inputs(endpoint: str, spec: dict[str, Any]) -> list[dict[str, Any]]:
        i, inputs = {}, []
        methods = list(spec.keys())
        for method in methods:
            if len(methods) > 1:
                i['cls']= _get_service_name(endpoint) + method.capitalize()
            else:
                i['cls']= _get_service_name(endpoint)
            i['uri'] = endpoint
            i['method'] = method.upper()

            # TODO: comment import and class if not in source-file
            i['request'] = _get_cls(endpoint, method, request=True)
            i['response'] = _get_cls(endpoint, method, response=True)
            imports.append(f'from . import {i["request"]}')
            imports.append(f'from . import {i["response"]}')

            inputs.append(i)
        return inputs
    
    for endpoint, spec in scheme['paths'].items():
        try:
            [
                definitions.append(uniconfig_rest.substitute(**i))
                for i in get_inputs(endpoint, spec)
            ]
        except Exception as e:
            ... # TODO: error handling
    return list(set(imports)), definitions


def generate_file(path: str | None, 
imports: Iterable[str], definitions: Iterable[str]) -> None:
    file = ENTER + ENTER.join(imports)
    file += 3 * ENTER + (2 *ENTER).join(definitions)
    path = DEFAULT_OUTPUT_FILE if not path else path
    try:
        with open(path, 'w+') as f:
            f.write(file)
        print(f'File {path} was successfully generated.')
    except Exception as e:
        print(f'Something went wrong while generating output file {path}', e, sep='\n')


def get_cli_args() -> Namespace:
    parser = ArgumentParser()
    parser.description = 'Python code-gen for Uniconfig Rest.'
    parser.add_argument(
        '--input', 
        type=str, 
        help='Path to OpenAPI-3 scheme in yaml format.', 
        required=True
    )
    parser.add_argument(
        '--output',
        type=str, 
        help=f'(Optional), path for output file. Default is {DEFAULT_OUTPUT_FILE}',
        required=False
    )
    return parser.parse_args()


def get_cls_def_names_from_source(source_file: str = DEFAULT_SOURCE_FILE) -> list[str]:
    loaded_file = None
    with open(source_file) as f:
        loaded_file = ast.parse(f.read())
    if loaded_file:
        return [x.name for x in loaded_file.body if isinstance(x, ast.ClassDef)]
    return []


def main() -> None:
    cli_args = get_cli_args()
    with open(cli_args.input) as f:
        scheme = yaml.safe_load(f)
    imports = ['from typing import Optional', 'from typing import Any']
    definitions = [inspect.getsource(UniconfigRest)]
    generated_classes = get_cls_def_names_from_source()
    rest_of_imports, rest_of_definitions = parse_swagger_scheme(scheme, generated_classes)
    imports += rest_of_imports
    definitions += rest_of_definitions
    generate_file(cli_args.output, imports, definitions)

    
if __name__ == '__main__':
    main()
