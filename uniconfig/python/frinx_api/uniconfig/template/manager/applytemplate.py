# generated by datamodel-codegen

from __future__ import annotations

from typing import Optional
from typing import Union

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field


class Type(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    leaf_list_values: Optional[list[str]] = Field(None, alias='leaf-list-values')
    """
    List of values that can be applied to the leaf-list.
    """


class TypeModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    leaf_value: Optional[str] = Field(None, alias='leaf-value')
    """
    Value that can be applied to leaf.
    """


class Value(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    leaf_list_values: Optional[list[str]] = Field(None, alias='leaf-list-values')
    """
    List of values that can be applied to the leaf-list.
    """


class ValueModel(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    leaf_value: Optional[str] = Field(None, alias='leaf-value')
    """
    Value that can be applied to leaf.
    """


class TypedLeafValue(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: Optional[str] = None
    """
    Type qualifier for this value.
    Used in case the same variable is used under different types
    """
    value: Optional[Union[Value, ValueModel]] = None


class TypeModel1(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    typed_leaf_values: Optional[list[TypedLeafValue]] = Field(
        None, alias='typed-leaf-values'
    )


class VariableItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    type: Optional[Union[Type, TypeModel, TypeModel1]] = None
    variable_id: Optional[str] = Field(None, alias='variable-id')
    """
    Variable identifier.
    """


class UniconfigNodeItem(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    uniconfig_node_id: Optional[str] = Field(None, alias='uniconfig-node-id')
    """
    Identifier of the target Uniconfig node.
    """
    variable: Optional[list[VariableItem]] = None
    """
    List of variables with associated values.
    """


class Input(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
    )
    template_node_id: str = Field(..., alias='template-node-id')
    """
    Identifier of the template.
    """
    uniconfig_node: Optional[list[UniconfigNodeItem]] = Field(
        None, alias='uniconfig-node'
    )
