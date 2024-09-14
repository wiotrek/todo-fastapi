import uvicorn
from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from fastapi.middleware.cors import CORSMiddleware

from src.db.session import Base, engine
from src.core.config import settings
from src.graphql.queries import Query
from src.graphql.mutations import Mutation
from src.graphql.context import get_context


app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.on_event("shutdown")
def shutdown():
    pass

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:4200",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_app = GraphQLRouter(
    schema,
    context_getter=get_context,
)

app.include_router(graphql_app, prefix="/graphql")

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.FASTAPI_RELOAD,
        host=settings.FASTAPI_HOST,
        port=settings.FASTAPI_PORT,
    )
