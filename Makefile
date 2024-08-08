docker.build:
	docker build \
	    --no-cache \
	    -t todo-fastapi:latest \
	    -f Dockerfile .