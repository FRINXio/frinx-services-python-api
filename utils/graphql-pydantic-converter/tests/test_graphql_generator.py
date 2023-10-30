import json
import typing

from pydantic import Field

import graphql_pydantic_converter.graphql_types
from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.schema_converter import GraphqlJsonParser

from .model import AddBlueprintInput
from .model import AddBlueprintMutation
from .model import AddBlueprintPayload
from .model import Blueprint
from .model import BlueprintConnection
from .model import BlueprintEdge
from .model import BlueprintsQuery
from .model import BlueprintsQueryResponse
from .render_models import AllocationStrategy
from .render_models import ClaimResourceMutation
from .render_models import PageInfoSchedule
from .render_models import Resource
from .render_models import ResourcePool
from .render_models import ResourcePoolConnection
from .render_models import ResourcePoolEdge
from .render_models import Schedule
from .render_models import ScheduleConnection
from .render_models import ScheduleEdge
from .render_models import SchedulesFilterInput
from .render_models import SchedulesQuery
from .render_models import SearchPoolsByTagsQuery
from .render_models import TagAnd
from .render_models import TagOr


class TestTaskGenerator:
    def test_render_json(self) -> None:
        reference_file = 'tests/model.py'
        json_schema = 'tests/schema.json'
        reference = open(reference_file).read()
        schema = json.loads(open(json_schema).read())
        converted = GraphqlJsonParser(input_json=schema).render()
        assert reference == converted

    def test_render_query(self) -> None:
        reference = '{ blueprints { edges { node { name } } } }'
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
        reference = f'mutation {{ addBlueprint ( input: {{ {bp_inputs} }}) {{ {bp_payload} }} }}'
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

        reference = ('mutation { ClaimResource ( poolId: "00000000001",  description: "<description>",  userInput: '
                     '{ address: "0.0.0.0", port: 80 }) { Properties AlternativeId id } }')
        mutation = ClaimResourceMutation(
            poolId='00000000001',
            description='<description>',
            userInput={'address': '0.0.0.0', 'port': 80},
            payload=Resource(
                id=True,
                Properties=True,
                AlternativeId=True
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

        json_blueprint = 'tests/blueprint.json'

        with open(json_blueprint) as json_file:
            device_import_json = json_file.read()
            template = device_import_json

            mutation = AddBlueprintMutation(
                payload=AddBlueprintPayload(
                    blueprint=Blueprint(
                        id=True,
                        name=True,
                        template=True
                    )
                ),
                input=AddBlueprintInput(
                    name='blueprint',
                    template=template,
                )
            ).render()

        reference = ('mutation { addBlueprint ( input: { name: "blueprint", template: "{\n\t\"cli\": '
                     '{\n\t\t\"cli-topology:host\": \"sample-topology\",\n\t\t\"cli-topology:port\": '
                     '\"{{port}}\",\n\t\t\"cli-topology:transport-type\": \"ssh\",\n\t\t\"cli-topology:device-type\": '
                     '\"{{device_type}}\",\n\t\t\"cli-topology:device-version\": '
                     '\"{{device_version}}\",\n\t\t\"cli-topology:password\": '
                     '\"{{password}}\",\n\t\t\"cli-topology:username\": '
                     '\"{{username}}\",\n\t\t\"cli-topology:journal-size\": '
                     '500,\n\t\t\"cli-topology:dry-run-journal-size\": 180,\n\t\t\"cli-topology:parsing-engine\": '
                     '\"tree-parser\"\n\t}\n}" }) { blueprint { id name template } } }')

        assert reference == mutation

    def test_render_input_advanced(self) -> None:
        query = SearchPoolsByTagsQuery(
            tags=TagOr(
                matchesAny=[
                    TagAnd(
                        matchesAll=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        Name=True,
                        PoolProperties=True,
                        PoolType=True,
                        id=True,
                        AllocationStrategy=AllocationStrategy(
                            Description=True,
                            Lang=True,
                            Name=True,
                            Script=True,
                            id=True
                        )
                    )
                ),
                totalCount=True
            )
        ).render()

        reference = '{ SearchPoolsByTags ( tags: { matchesAny: [  { matchesAll: [ "root_pool" ] }  ]  } ) ' \
                    '{ edges { node { AllocationStrategy { Description Lang Name Script id } ' \
                    'Name PoolProperties PoolType id } } totalCount } }'

        assert reference == query

        query_render = SchedulesQuery(
            payload=ScheduleConnection(
                pageInfo=PageInfoSchedule(
                    hasNextPage=True,
                    hasPreviousPage=True,
                    startCursor=True,
                    endCursor=True
                ),
                edges=ScheduleEdge(
                    node=Schedule(
                        name=True,
                        cronString=True,
                        enabled=True
                    ),
                    cursor=True
                ),
                totalCount=True
            ),
            after='aaa',
            first=10,
            filter=SchedulesFilterInput(
                workflowName='TEST_A',
                workflowVersion='1'
            )
        ).render()

        reference = '{ schedules ( after: "aaa", first: 10, filter: { workflowName: "TEST_A" ,' \
                    ' workflowVersion: "1"  } ) { edges { node { name enabled' \
                    ' cronString } cursor } pageInfo ' \
                    '{ hasNextPage hasPreviousPage startCursor endCursor } totalCount } }'

        assert reference == query_render

    def test_parse_response(self) -> None:

        response: typing.Any = {
            'data': {
                'blueprints': {
                    'edges': [
                        {
                            'node': {
                                'name': 'cli_device_import',
                                'id': 'Qmx1ZXByaW50OjkyMjJmNTcwLTllNTktNDQxYi1iNzk4LTY2ZTEyY2YwZGQ5OQ'
                            }
                        }
                    ]
                }
            }
        }

        response = BlueprintsQueryResponse(**response)

        assert 'cli_device_import' == response.data.blueprints.edges[0].node.name

    def test_multiple_query(self) -> None:

        query_first = SearchPoolsByTagsQuery(
            tags=TagOr(
                matchesAny=[
                    TagAnd(
                        matchesAll=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        Name=True,
                        id=True,
                        PoolProperties=True,
                        PoolType=True,
                        AllocationStrategy=AllocationStrategy(
                            Name=True
                        )
                    )
                ),
                totalCount=True
            )
        )

        query_second = SchedulesQuery(
            payload=ScheduleConnection(
                __typename=True,
                pageInfo=PageInfoSchedule(
                    __typename=True,
                    hasNextPage=True,
                    hasPreviousPage=True,
                    startCursor=True,
                    endCursor=True
                ),
                edges=ScheduleEdge(
                    node=Schedule(
                        name=True,
                        cronString=True,
                        enabled=True
                    ),
                    cursor=True
                ),
                totalCount=True
            ),
            after='aaa',
            first=10,
            filter=SchedulesFilterInput(
                workflowName='TEST_A',
                workflowVersion='1'
            )
        )

        queries = [
            query_first,
            query_second
        ]

        reference = '{  SearchPoolsByTags ( tags: { matchesAny: [  { matchesAll: [ "root_pool" ] }  ]  } ) ' \
            '{ edges { node { AllocationStrategy { Name } ' \
            'Name PoolProperties PoolType id } } totalCount }  schedules ( after: "aaa", first: 10, filter: ' \
            '{ workflowName: "TEST_A" , workflowVersion: "1"  } ) { __typename edges { node { name enabled ' \
            'cronString } cursor } ' \
            'pageInfo { __typename hasNextPage hasPreviousPage startCursor endCursor } totalCount }  }'

        merged_query = graphql_pydantic_converter.graphql_types.concatenate_queries(queries)
        assert reference == merged_query
