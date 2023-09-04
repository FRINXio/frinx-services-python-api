import json
import typing

from model import AddBlueprintInput
from model import AddBlueprintMutation
from model import AddBlueprintPayload
from model import Blueprint
from model import BlueprintConnection
from model import BlueprintEdge
from model import BlueprintsQuery
from pydantic import Field

from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.schema_converter import GraphqlJsonParser


class TestTaskGenerator:
    def test_render_json(self) -> None:
        reference_file = 'tests/model.py'
        json_schema = 'tests/schema.json'
        reference = open(reference_file).read()
        schema = json.loads(open(json_schema).read())
        converted = GraphqlJsonParser(input_json=schema).render()
        assert reference == converted

    def test_render_query(self) -> None:
        reference = '{ blueprints { edges { cursor node { createdAt name template updatedAt } } totalCount } }'
        query = BlueprintsQuery(
            payload=BlueprintConnection(
                edges=BlueprintEdge(
                    node=Blueprint(
                        name=True,
                        id=False
                    )
                )
            )
        ).render()
        assert reference == query

    def test_render_mutation(self) -> None:
        bp_inputs = 'name: "IOS", template: "{ "cli": { "cli-topology:host": "sample-topology" } }"'
        bp_payload = 'blueprint { createdAt name template updatedAt }'
        reference = f'mutation {{ addBlueprint ( input: {{ {bp_inputs} }}) {{ { bp_payload } }} }}'
        mutation = AddBlueprintMutation(
            input=AddBlueprintInput(
                name='IOS',
                template='{ "cli": { "cli-topology:host": "sample-topology" } }'
            ),
            payload=AddBlueprintPayload(
                blueprint=Blueprint(
                    createdAt=True,
                    id=False,
                    name=True,
                    template=True,
                    updatedAt=True
                )
            )
        ).render()
        assert reference == mutation

    def test_render_input(self) -> None:
        class DeviceSize(ENUM):
            SMALL = 'SMALL'
            MEDIUM = 'MEDIUM'
            LARGE = 'LARGE'

        class AddDeviceInput(Input):
            name: str
            zone_id: str = Field(alias='zoneId')
            label_ids: typing.Optional[list[str]] = Field(alias='labelIds')
            device_size: typing.Optional[DeviceSize] = Field(alias='deviceSize')
            mount_parameters: typing.Optional[str] = Field(alias='mountParameters')
            port: typing.Optional[int]
            booleans: typing.Optional[bool]
            dicts: typing.Optional[dict[typing.Any, typing.Any]]
            lists: typing.Optional[list[list[str]]]

        mutation = AddDeviceInput(
            name='name',
            zoneId='zoneId',
            mountParameters='{}',
            labelIds=['id', 'ud'],
            port=8080,
            deviceSize=DeviceSize.MEDIUM,
            booleans=True,
            dicts={
                'a': 'a',
                'b': 5,
                'c': {
                    'd': 'd'
                }
            },
            lists=[['aaa']]
        ).render()

        reference = 'name: "name", zoneId: "zoneId", labelIds: ["id", "ud"], ' \
                    'deviceSize: MEDIUM, mountParameters: "{}", port: 8080, booleans: true, ' \
                    'dicts: {a: {"a"}, b: {5}, c: {d: "d"}}], lists: [["aaa"]]'

        assert reference == mutation
