# Python Service to Expose Custom Metrics
Custom Python application designed to run on a Kubernetes Cluster to monitor an internet url and provide prometheus metrics.

Assumptioms:
  Internlly the service runs on port 5000
  Port 5000 is mapped to 30000 through kubernetes service
  Port 30000 should be enabled in the firewall (if any) to access the application URL

# How to build and deploy
Clone this repository to the machine where you would like to build and deploy

```bash
$ git clone https://github.com/nareshbvemula/python_service_expose_metrics.git
```
## Contents 
* src/app.py - A python flask Application to expose custom prometheus metrics
* requirements.txt - Contains the list of moduled to be installed docker container
* Dockerfile - Docker file to build the application 
* deployment.yml - kubernetes deployment file, used to create a deployment in kubernetes
* service.yml - kubernetes service file, to expose application port on to the Node

## Procedure
Build docker image of the application
```bash
docker build -t metrics -f Dockerfile
```
Tag this docker image with full name of your Docker hub/repository
```bash
docker tag metrics:latest nareshvemula/python-flask
```
Login to docker hub/registory and push this image
```bash
docker login
```
```bash
docker push nareshvemula/python-flask
```
Deploy in kubernetes Cluster
Note: If the name of the Docker image is different , do please update in this file under "image: <Name of the docker image>"
```bash
kubectl apply -f deployment.yml
```
Verify if the pod is up and runnning 
```bash
kubectl get pods --all-namespaces
NAMESPACE     NAME                                          READY   STATUS    RESTARTS   AGE
default       python-flask-app-deployment-876d4b565-gdpqn   1/1     Running   0          41s
kube-system   coredns-6955765f44-779v8                      1/1     Running   0          2m39s
kube-system   coredns-6955765f44-n9wtl                      1/1     Running   0          2m39s
kube-system   etcd-ip-172-31-20-181                         1/1     Running   0          2m47s
kube-system   kube-apiserver-ip-172-31-20-181               1/1     Running   0          2m47s
kube-system   kube-controller-manager-ip-172-31-20-181      1/1     Running   0          2m47s
kube-system   kube-proxy-czqjk                              1/1     Running   0          2m39s
kube-system   kube-scheduler-ip-172-31-20-181               1/1     Running   0          2m47s
```
Create a kubernetes service to expose port on to the Node
```bash
kubectl apply -f service.yml 
```
## Verify
Access the URL to view the custom metrics
```bash
  http://<HOST IP>:30000/metrics
```

