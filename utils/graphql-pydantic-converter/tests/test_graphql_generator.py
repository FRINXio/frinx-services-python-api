import json
import typing

from pydantic import Field

import graphql_pydantic_converter.graphql_types
from graphql_pydantic_converter.graphql_types import ENUM
from graphql_pydantic_converter.graphql_types import Input
from graphql_pydantic_converter.graphql_types import QueryForm
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
from .render_models import CreateScheduleInput
from .render_models import CreateScheduleMutation
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
from .render_models import DeleteScheduleMutation
from .render_models import DeleteScheduleQuery


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
        ).render(form='inline')
        assert reference == query.query

    def test_render_mutation(self) -> None:
        bp_inputs = 'name: "IOS", template: "{ \\"cli\\": { \\"cli-topology:host\\": \\"sample-topology\\" } }"'
        bp_payload = 'blueprint { createdAt name template updatedAt }'
        reference = f'mutation {{ addBlueprint ( input: {{ {bp_inputs} }}) {{ {bp_payload} }} }}'
        mutation = AddBlueprintMutation(
            input=AddBlueprintInput(
                name='IOS',
                template='{ "cli": { "cli-topology:host": "sample-topology" } }'
            ),
            payload=AddBlueprintPayload(
                blueprint=Blueprint(
                    created_at=True,
                    id=False,
                    name=True,
                    template=True,
                    updated_at=True
                )
            )
        ).render(form='inline')

        assert reference == mutation.query

        reference = ('mutation { ClaimResource ( poolId: "00000000001",  description: "<description>",  userInput: '
                     '{ address: "0.0.0.0", port: 80 }) { Properties AlternativeId id } }')
        mutation = ClaimResourceMutation(
            pool_id='00000000001',
            description='<description>',
            user_input=dict(address='0.0.0.0', port=80),
            payload=Resource(
                id=True,
                properties=True,
                alternative_id=True
            )
        ).render(form='inline')
        assert reference == mutation.query

        reference = 'mutation deleteSchedule($name: String!) { deleteSchedule(name: $name)  }'
        mutation = DeleteScheduleMutation(
            payload=True,
            name="ScheduledWF"
        ).render()
        assert reference == mutation.query

        reference = 'mutation { deleteSchedule ( name: "ScheduledWF")  }'
        mutation = DeleteScheduleMutation(
            payload=True,
            name="ScheduledWF"
        ).render(form='inline')
        assert reference == mutation.query

        reference = 'query deleteScheduleQuery($name: String!) { deleteScheduleQuery(name: $name)  }'
        mutation = DeleteScheduleQuery(
            payload=True,
            name="ScheduledWF"
        ).render()
        assert reference == mutation.query

        reference = '{ deleteScheduleQuery ( name: "ScheduledWF" )  }'
        mutation = DeleteScheduleQuery(
            payload=True,
            name="ScheduledWF"
        ).render(form='inline')
        assert reference == mutation.query

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

        add_device_mutation = AddDeviceInput(
            name='name',
            zone_id='zoneId',
            mount_parameters='{}',
            label_ids=['id', 'ud'],
            port=8080,
            device_size=DeviceSize.MEDIUM,
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

        assert reference == add_device_mutation

        json_blueprint = 'tests/blueprint.json'
        with open(json_blueprint) as json_file:
            device_import_json = json_file.read()
            template = device_import_json

            add_blueprint_mutation = AddBlueprintMutation(
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
            ).render(form='inline')

            reference = ('mutation { addBlueprint ( input: { name: "blueprint", template: "{\\n\\t\\"cli\\": '
                         '{\\n\\t\\t\\"cli-topology:host\\": \\"sample-topology\\",\\n\\t\\t\\"cli-topology:port\\":'
                         ' \\"{{port}}\\",\\n\\t\\t\\"cli-topology:transport-type\\": \\"ssh\\",'
                         '\\n\\t\\t\\"cli-topology:device-type\\": \\"{{device_type}}\\",\\n\\t\\t\\"cli-topology:'
                         'device-version\\": \\"{{device_version}}\\",\\n\\t\\t\\"cli-topology:password\\": '
                         '\\"{{password}}\\",\\n\\t\\t\\"cli-topology:username\\": \\"{{username}}\\"'
                         ',\\n\\t\\t\\"cli-topology:journal-size\\": 500,\\n\\t\\t\\"cli-topology:'
                         'dry-run-journal-size\\": 180,\\n\\t\\t\\"cli-topology:parsing-engine\\": '
                         '\\"tree-parser\\"\\n\\t}\\n}" }) { blueprint { id name template } } }')

            assert reference == add_blueprint_mutation.query

    def test_render_input_advanced(self) -> None:
        query = SearchPoolsByTagsQuery(
            tags=TagOr(
                matches_any=[
                    TagAnd(
                        matches_all=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        name=True,
                        pool_properties=True,
                        pool_type=True,
                        id=True,
                        allocation_strategy=AllocationStrategy(
                            description=True,
                            lang=True,
                            name=True,
                            script=True,
                            id=True
                        )
                    )
                ),
                total_count=True
            )
        ).render(form='inline')

        reference = '{ SearchPoolsByTags ( tags: { matchesAny: [  { matchesAll: [ "root_pool" ] }  ]  } ) ' \
                    '{ edges { node { AllocationStrategy { Description Lang Name Script id } ' \
                    'Name PoolProperties PoolType id } } totalCount } }'

        assert reference == query.query

        query_render = SchedulesQuery(
            payload=ScheduleConnection(
                page_info=PageInfoSchedule(
                    has_next_page=True,
                    has_previous_page=True,
                    start_cursor=True,
                    end_cursor=True
                ),
                edges=ScheduleEdge(
                    node=Schedule(
                        name=True,
                        cron_string=True,
                        enabled=True
                    ),
                    cursor=True
                ),
                total_count=True
            ),
            after='aaa',
            first=10,
            filter=SchedulesFilterInput(
                workflow_name='TEST_A',
                workflow_version='1'
            )
        ).render(form='inline')

        reference = '{ schedules ( after: "aaa", first: 10, filter: { workflowName: "TEST_A" ,' \
                    ' workflowVersion: "1"  } ) { edges { node { name enabled' \
                    ' cronString } cursor } pageInfo ' \
                    '{ hasNextPage hasPreviousPage startCursor endCursor } totalCount } }'

        assert reference == query_render.query

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

    def test_concatenate_query(self) -> None:

        query_first = SearchPoolsByTagsQuery(
            tags=TagOr(
                matches_any=[
                    TagAnd(
                        matches_all=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        name=True,
                        id=True,
                        pool_properties=True,
                        pool_type=True,
                        allocation_strategy=AllocationStrategy(
                            name=True
                        )
                    )
                ),
                total_count=True
            )
        )

        query_second = SchedulesQuery(
            payload=ScheduleConnection(
                typename=True,
                page_info=PageInfoSchedule(
                    typename=True,
                    has_next_page=True,
                    has_previous_page=True,
                    start_cursor=True,
                    end_cursor=True
                ),
                edges=ScheduleEdge(
                    node=Schedule(
                        name=True,
                        cron_string=True,
                        enabled=True
                    ),
                    cursor=True
                ),
                total_count=True
            ),
            after='aaa',
            first=10,
            filter=SchedulesFilterInput(
                workflow_name='TEST_A',
                workflow_version='1'
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

    def test_multiple_query(self) -> None:

        query_first = SearchPoolsByTagsQuery(
            tags=TagOr(
                matches_any=[
                    TagAnd(
                        matches_all=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        name=True,
                        id=True,
                        pool_properties=True,
                        pool_type=True,
                        allocation_strategy=AllocationStrategy(
                            name=True
                        )
                    )
                ),
                total_count=True
            )
        )

        query_second = SchedulesQuery(
            payload=ScheduleConnection(
                typename=True,
                page_info=PageInfoSchedule(
                    typename=True,
                    has_next_page=True,
                    has_previous_page=True,
                    start_cursor=True,
                    end_cursor=True
                ),
                edges=ScheduleEdge(
                    node=Schedule(
                        name=True,
                        cron_string=True,
                        enabled=True
                    ),
                    cursor=True
                ),
                total_count=True
            ),
            after='aaa',
            first=10,
            filter=SchedulesFilterInput(
                workflow_name='TEST_A',
                workflow_version='1'
            )
        )

        queries = [
            query_first,
            query_second
        ]

        reference_first = ('{ SearchPoolsByTags ( tags: { matchesAny: [  { matchesAll: [ "root_pool" ] } '
                           ' ]  } ) { edges { node { AllocationStrategy { Name } '
                           'Name PoolProperties PoolType id } } totalCount } }')

        reference_second = ('{ schedules ( after: "aaa", first: 10, filter: '
                            '{ workflowName: "TEST_A" , workflowVersion: "1"  } ) '
                            '{ __typename edges { node { name enabled ' 'cronString } cursor } pageInfo '
                            '{ __typename hasNextPage hasPreviousPage startCursor endCursor } totalCount } }')

        merged_query: list[QueryForm] = graphql_pydantic_converter.graphql_types.render(queries, form='inline')

        assert reference_first == merged_query[0].query
        assert reference_second == merged_query[1].query

        reference_first_var = {'tags': {'matchesAny': [{'matchesAll': ['root_pool']}]}}
        reference_first_query = ('query SearchPoolsByTags($tags: TagOr) { SearchPoolsByTags(tags: $tags) { edges { node'
                                 ' { AllocationStrategy { Name } Name PoolProperties PoolType id } } totalCount } }')

        reference_second_query = ('query schedules($after: String, $first: Int, $filter: SchedulesFilterInput) '
                                  '{ schedules(after: $after, first: $first, filter: $filter) { __typename edges '
                                  '{ node { name enabled cronString } cursor } pageInfo '
                                  '{ __typename hasNextPage hasPreviousPage startCursor endCursor } totalCount } }')
        reference_second_var = {'after': 'aaa', 'first': 10, 'filter':
                                {'workflowName': 'TEST_A', 'workflowVersion': '1'}}

        merged_query = graphql_pydantic_converter.graphql_types.render(queries, form='extracted')

        assert reference_first_query == merged_query[0].query
        assert reference_first_var == merged_query[0].variable

        print(merged_query[1].query)
        print(merged_query[1].variable)

        assert reference_second_query == merged_query[1].query
        assert reference_second_var == merged_query[1].variable

    def test_extracted_render(self) -> None:

        query = SearchPoolsByTagsQuery(
            tags=TagOr(
                matches_any=[
                    TagAnd(
                        matches_all=[
                            'root_pool'
                        ]
                    )
                ]
            ),
            payload=ResourcePoolConnection(
                edges=ResourcePoolEdge(
                    node=ResourcePool(
                        name=True,
                        id=True,
                        pool_properties=True,
                        pool_type=True,
                        allocation_strategy=AllocationStrategy(
                            name=True
                        )
                    )
                ),
                total_count=True
            )
        )

        query_str = query.render(form='extracted')

        reference_variable: typing.Any = {'tags': {'matchesAny': [{'matchesAll': ['root_pool']}]}}
        reference_mutation = ('query SearchPoolsByTags($tags: TagOr) '
                              '{ SearchPoolsByTags(tags: $tags) { edges { node { AllocationStrategy { Name } '
                              'Name PoolProperties PoolType id } } totalCount } }')

        assert reference_mutation == query_str.query
        assert reference_variable == query_str.variable

        mutation = CreateScheduleMutation(
            payload=Schedule(
                name=True,
                enabled=True,
                workflow_name=True,
                workflow_version=True,
                cron_string=True
            ),
            input=CreateScheduleInput(
                name='name',
                workflow_name='workflowName',
                workflow_version='workflowVersion',
                cron_string='* * * * *',
                enabled=True,
                parallel_runs=False,
            )
        )

        mutation_str = mutation.render(form='extracted')
        reference_variable = {
            'input': {
                'name': 'name',
                'workflowName': 'workflowName',
                'workflowVersion': 'workflowVersion',
                'cronString': '* * * * *',
                'enabled': True,
                'parallelRuns': False}
        }

        reference_mutation = ('mutation createSchedule($input: CreateScheduleInput!) { createSchedule(input: $input) '
                              '{ name enabled workflowName workflowVersion cronString } }')

        assert reference_mutation == mutation_str.query
        assert reference_variable == mutation_str.variable

