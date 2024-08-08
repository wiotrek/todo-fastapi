## Useful commands

Run app as dev
```
uvicorn src.main:app --reload --port 3000 --host 0.0.0.0
```

Set workdir
```
export PYTHONPATH=${PATH}/todo-fastapi/src
```

Build docker image - todo-fastapi:latest
```
make docker.build
```

## About 
Simple crud app to check fastapi framework with graphql

## Stack:
- FastApi
- Strawberry Graphql
- JWT
- Uvicorn
