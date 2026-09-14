protos=("echo")

for proto in "${protos[@]}"; do
    python3 -m grpc_tools.protoc -I. --python_out=src --pyi_out=src --grpc_python_out=src protos/$proto.proto
done
