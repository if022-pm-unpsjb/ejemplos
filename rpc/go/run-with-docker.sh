#! /bin/sh

echo docker run --rm --network host -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang:1.24 go run $1
docker run --rm --network host -v "$PWD":/usr/src/myapp -w /usr/src/myapp golang:1.24 go run $1

