# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    with_details: Optional[bool] = Field(None, alias='with-details')
    """
    Flag for determine whether output will be detailed or not.
    """


class ComplexOutputItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    non_covered_parts: Optional[list[str]] = Field(None, alias='non-covered-parts')
    command: Optional[str] = None
    covered: Optional[bool] = None


class CliUnitGenericResult(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    complex_output: Optional[list[ComplexOutputItem]] = Field(
        None, alias='complex-output'
    )
    """
    Simple output contains commands marked with '+' if it is covered or '-' if not.
    """


class CliUnitGenericResultModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    simple_output: Optional[str] = Field(None, alias='simple-output')
    """
    Simple output contains commands marked with '+' if it is covered or '-' if not.
    """


class Output(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    cli_unit_generic_result: Optional[
        Union[CliUnitGenericResult, CliUnitGenericResultModel]
    ] = Field(None, alias='cli-unit-generic:result')
