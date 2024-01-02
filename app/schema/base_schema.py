from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class BaseSchema(BaseModel):
    created_by: Optional[str] = Field(title="Creator Name")
    created_on: Optional[datetime] = Field(title="Created Date")
    modified_by: Optional[str] = Field(title="Last Modifier Name")
    modified_on: Optional[datetime] = Field(title="Last Modified Time")
