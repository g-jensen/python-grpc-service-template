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

### Component 'test'

You'll need [grpcurl](https://github.com/fullstorydev/grpcurl) to run this command. First, run the server, then run:

```bash
grpcurl -plaintext -proto idl/protos/echo.proto -d '{"content": "Echo!"}' 127.0.0.1:8080 echo.Echo/Call
```

### Adding a service

1. Create a new proto file for your service in `idl/protos/my_service.proto`
2. Regenerate proto files: `./scripts/generate_protos.sh`
3. Implement your service directory for your service in `src/servicers/my_service/` (take inspiration from `src/servicers/echo/`)
4. Register your service
    1. Add your service to the `stub_services_to_register` in `src/registrar_test.py`
    2. Assert that tests fail
    3. Add your service to the `services_to_register` in `src/registrar.py`
    4. Assert that tests now pass