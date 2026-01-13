from typing import Any, Type, TypeVar,Optional
import json

T = TypeVar("T")


def serialize(obj: Any) -> str:
    return json.dumps(obj, default=lambda o: o.__dict__, indent=2)


def deserialize(json_str: str, cls: Optional[Type[T]] = None) -> Any:
    data = json.loads(json_str)
    if cls:
        # assumes cls can accept nested dicts directly
        return cls(**data)
    return data
