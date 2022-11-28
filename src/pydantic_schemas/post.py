from pydantic import BaseModel, validator, Field


class Post(BaseModel):
    id: int = Field(le=3)
    title: str

    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v):
    #     if v > 2:
    #         raise ValueError('ID is not less than two')
    #     else:
    #         return v
