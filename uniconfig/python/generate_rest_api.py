import ast
import inspect
import re
from argparse import ArgumentParser
from argparse import Namespace
from collections.abc import Iterable
from string import Template
from typing import Any

import yaml
from pydantic import BaseModel

DEFAULT_SOURCE_FILE = 'frinx_api/uniconfig/__init__.py'
SOURCE_FILE_PY_PATH = '.'
DEFAULT_OUTPUT_FILE = 'frinx_api/uniconfig/rest_api.py'

COMMENT_TAG = '# '
ENTER = '\n'
SPACE = ' '
TAB = '    '
NAN = ''


class CustomTemplate(Template):
    delimiter = '_'


class UniconfigRest:
    uri: str
    method: str
    request: BaseModel | None
    response: BaseModel | None


def _set_globals_for_template_cls() -> None:
    global _request, _response
    _request, _response = None, None


_set_globals_for_template_cls()


class _Cls(UniconfigRest):
    uri = '_uri'
    method = '_method'
    request = _request
    response = _response


def parse_swagger_scheme(scheme: dict[str, Any], req_res_refs: Iterable[str],
imports: list = [], definitions: list = []) -> tuple[list[str], list[str]]:
    
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
    
    uc_rest_template = CustomTemplate(inspect.getsource(_Cls))
    
    for endpoint, spec in scheme['paths'].items():
        methods, template_input = list(spec.keys()), {}
        for method in methods:
            if len(methods) > 1:
                template_input['Cls']= _get_service_name(endpoint) + method.capitalize()
            else:
                template_input['Cls']= _get_service_name(endpoint)

            template_input['uri'] = endpoint
            template_input['method'] = method.upper()

            req_ref = _get_cls(endpoint, method, request=True)
            res_ref = _get_cls(endpoint, method, response=True)

            if req_ref in req_res_refs:
                imports.append(f'from {SOURCE_FILE_PY_PATH} import {req_ref}')
                template_input['request'] = req_ref
            else:
                template_input['request'] = None
            if res_ref in req_res_refs:
                imports.append(f'from {SOURCE_FILE_PY_PATH} import {res_ref}')
                template_input['response'] = res_ref
            else:
                template_input['response'] = None

            definitions.append(uc_rest_template.substitute(**template_input))

    return imports, definitions


def generate_file(path: str | None, imports: Iterable[str], definitions: Iterable[str]) -> None:
    file = ENTER.join(imports)
    file += 3 * ENTER + (2 *ENTER).join(definitions)
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


def cls_def_names_from_src_file(source_file: str) -> list[str]:
    with open(source_file) as f:
        loaded_file = ast.parse(f.read())
        return [x.name for x in loaded_file.body if isinstance(x, ast.ClassDef)]


def main() -> None:
    cli_args = get_cli_args()

    with open(cli_args.input) as f:
        scheme = yaml.safe_load(f)

    generate_file(
        cli_args.output or DEFAULT_OUTPUT_FILE,
        *parse_swagger_scheme(
            scheme=scheme, 
            req_res_refs=cls_def_names_from_src_file(DEFAULT_SOURCE_FILE),
            imports=[
                'from __future__ import annotations',
                NAN, # empty line between imports
                'from pydantic import BaseModel', 
                NAN, # empty line between imports
            ],
            definitions=[inspect.getsource(UniconfigRest)]
        )
    )

    
if __name__ == '__main__':
    main()
