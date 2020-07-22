# py-brothers
Commands to run in terminal:
```shell
docker build -t py-brothers:2.0 -f Dockerfile1 .
```
```shell
docker run -p 8070:8070 py-brothers:2.0
```
To publish image to docker hub, run command in terminal:

```shell
 docker login -u #username# -p #docker-token# docker.io && docker push #username#/py-brothers:2.0
```
