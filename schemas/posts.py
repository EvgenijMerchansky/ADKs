from pydantic import BaseModel, Field

# --- Schemas ---

class PostOutput(BaseModel):
    id: int
    userId: str
    title: str
    body: str

# --- Outputs ---

class SinglePostOutput(BaseModel):
    post: PostOutput = Field(description="Post")

class PostsOutput(BaseModel):
    users: list[PostOutput] = Field(description="List of posts")