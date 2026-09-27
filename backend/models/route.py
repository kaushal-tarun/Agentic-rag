from pydantic import BaseModel


class RouteDecision(BaseModel):
    route: str