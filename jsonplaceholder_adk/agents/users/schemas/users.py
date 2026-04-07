from pydantic import BaseModel, Field


# --- Schemas ---

class GeoOutput(BaseModel):
    lat: str
    lng: str


class AddressOutput(BaseModel):
    street: str
    suite: str
    city: str
    zipcode: str
    geo: GeoOutput


class CompanyOutput(BaseModel):
    name: str
    catchPhrase: str
    bs: str


class UserOutput(BaseModel):
    id: int
    name: str
    username: str
    email: str
    address: AddressOutput
    phone: str
    website: str
    company: CompanyOutput


# --- Outputs ---

class UsersOutput(BaseModel):
    users: list[UserOutput] = Field(description="List of users")


class SingleUserOutput(BaseModel):
    user: UserOutput = Field(description="User")
