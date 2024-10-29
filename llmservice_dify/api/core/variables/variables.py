from pydantic import Field

from core.helper import encrypter

from .segments import (
    ArrayAnySegment,
    ArrayNumberSegment,
    ArrayObjectSegment,
    ArrayStringSegment,
    FileSegment,
    FloatSegment,
    IntegerSegment,
    NoneSegment,
    ObjectSegment,
    Segment,
    StringSegment,
)
from .types import SegmentType


class Variable(Segment):
    """
    A variable is a segment that has a name.
    """

    id: str = Field(
        default="",
        description="Unique identity for variable. It's only used by environment variables now.",
    )
    name: str
    description: str = Field(default="", description="Description of the variable.")


class StringVariable(StringSegment, Variable):
    pass


class FloatVariable(FloatSegment, Variable):
    pass


class IntegerVariable(IntegerSegment, Variable):
    pass


class ObjectVariable(ObjectSegment, Variable):
    pass


class ArrayAnyVariable(ArrayAnySegment, Variable):
    pass


class ArrayStringVariable(ArrayStringSegment, Variable):
    pass


class ArrayNumberVariable(ArrayNumberSegment, Variable):
    pass


class ArrayObjectVariable(ArrayObjectSegment, Variable):
    pass


class SecretVariable(StringVariable):
    value_type: SegmentType = SegmentType.SECRET

    @property
    def log(self) -> str:
        return encrypter.obfuscated_token(self.value)


class NoneVariable(NoneSegment, Variable):
    value_type: SegmentType = SegmentType.NONE
    value: None = None


class FileVariable(FileSegment, Variable):
    pass
