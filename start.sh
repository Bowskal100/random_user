#!/bin/bash -x
app="random_user"
docker build -t ${app}:latest .
echo "Build completed, prepared to run"
docker run -d -p 5000:5000 ${app}
