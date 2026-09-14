for proto in protos/*.proto; do
    python3 -m grpc_tools.protoc -I. --python_out=src --pyi_out=src --grpc_python_out=src "$proto"
done
