# python-grpc-service-template

Requires the `uv` Python package manager

## Development

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
