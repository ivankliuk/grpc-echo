# gRPC echo server

A simple gRPC echo server. Returns [metadatum](https://grpc.github.io/grpc/python/glossary.html#term-metadatum) in each response.

## Local execution

Build stubs and install dependencies:
```bash
git clone git@github.com:ivankliuk/grpc-echo.git
cd grpc-echo/
python -m grpc_tools.protoc -I proto/ --python_out=. --grpc_python_out=. proto/grpc_echo.proto
pip install -r requirements.txt
```

Run client and server locally:
```bash
python server.py &
python client.py
```

## Cloud execution

Build and publish Docker image:
```bash
docker build --platform=linux/amd64 -t grpc_echo .
docker images # get image hash
docker tag 8fac6a20b893 ivankliuk/grpc_echo:0.0.1
docker push ivankliuk/grpc_echo:0.0.1
```

Clean up Kubernetes environment:
```bash
K8S_NS=my-namespace
kubectl delete namespace $K8S_NS
kubectl delete ingressclass nginx
```

To fix the error:
> Error from server (InternalError): error when creating "kubernetes.yaml": Internal error occurred: failed calling 
> webhook "validate.nginx.ingress.kubernetes.io": 
> Post "https://ingress-nginx-1671457309-controller-admission.my-namespace.svc:443/networking/v1/ingresses?timeout=10s": 
> no endpoints available for service "ingress-nginx-1671457309-controller-admission"

Delete validating webhook configurations:
```bash
kubectl get validatingwebhookconfigurations
kubectl delete validatingwebhookconfigurations ingress-nginx-1671457309-controller-admission
```

Installation on a Kubernetes cluster:
```bash
K8S_NS=my-namespace
kubectl create namespace $K8S_NS
helm install ingress-nginx/ingress-nginx --generate-name -f helm_values.yaml -n $K8S_NS
kubectl apply -f kubernetes.yaml -n $K8S_NS
```

## Test scenario

- Header `Test-Header` is not present neither in `nginx.ingress.kubernetes.io/cors-allow-headers` nor in `nginx.ingress.kubernetes.io/cors-expose-headers`
- Header `X-Grpc-Web` is present only in `nginx.ingress.kubernetes.io/cors-allow-headers`
- Header `Grpc-Status` is present only in `nginx.ingress.kubernetes.io/cors-expose-headers`

Get load balancer IP and run grpcurl:
```bash
LB=$(kubectl get svc -n $K8S_NS | grep LoadBalancer | awk '{print $3}')
grpcurl -authority my-example-host.com \
        -H 'Test-Header: test-header' \
        -H 'X-Grpc-Web: grpc-web' \
        -H 'Grpc-Status: grpc-status' \
        -d '{"payload": "payload!"}' \
        -insecure \
        --proto proto/grpc_echo.proto \
        $LB:443 \
        grpc_echo.Echo/Ping
```

Server log and client output:
```json
{
  "payload": "payload!",
  "invocationMetadata": {
    "user-agent": "grpcurl/1.8.7 grpc-go/1.48.0",
    "x-request-id": "6de2e450dbc98ab8f3770ae94c1fc00f",
    "x-real-ip": "10.7.13.26",
    "x-forwarded-for": "10.7.13.26",
    "x-forwarded-host": "my-example-host.com",
    "x-forwarded-port": "443",
    "x-forwarded-proto": "https",
    "x-forwarded-scheme": "https",
    "x-scheme": "https",
    "test-header": "test-header",
    "x-grpc-web": "grpc-web"
  }
}
```
