# python-grpc-service-template

Requires the `uv` Python package manager

## Quickstart

### Install all dependencies

```bash
uv sync --all-groups
```
And activate the environment:
```bash
source .venv/bin/activate
```

### Generate protobuf files

```bash
./scripts/generate_protos.sh
```

### Rename the app

```bash
./scripts/rename.sh new-name
```

Note that this will only work once.

### Run the server

```bash
uv run serve
```

### Unit tests

```bash
uv run test
```

### Component 'Test'

You'll need [grpcurl](https://github.com/fullstorydev/grpcurl) to run this command. First, run the server, then run:

```bash
grpcurl -plaintext -proto protos/echo.proto -d '{"content": "Echo!"}' 127.0.0.1:8080 echo.Echo/Call
```
