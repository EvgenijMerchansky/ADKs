from pydantic import BaseModel, Field


# --- Schemas ---

class CommentOutput(BaseModel):
    id: int
    postId: str
    name: str
    email: str
    body: str


# --- Outputs ---

class SingleCommentOutput(BaseModel):
    comment: CommentOutput = Field(description="Comment")


class CommentsOutput(BaseModel):
    comments: list[CommentOutput] = Field(description="List of comments")
