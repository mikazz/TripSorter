# Flask Redis Queue

Example of how to handle background processes with Flask, Redis Queue, and Docker

## Quick Start

Local (without Docker)
```sh
# Start MongoDB (Windows)
cd C:\Program Files\MongoDB\Server\4.2\bin
>enter command mongod
# by default, mongodb server will start at port 27017

# Start Redis (Windows)
cd _Redis-x64-3.2.100
redis-server.exe

# Start app
manage.py run

Start Worker (Windows or Linux)
manage.py run_windows_worker or manage.py run_worker
```

Spin up the containers (Docker)
```sh
$ docker-compose up --build
```

## Usage

To view the app open your browser to
```
# Docker
http://localhost

# Local
http://127.0.0.1:5000/
```

To view the RQ dashboard.
```
# Docker
http://localhost:9181

# Local
http://127.0.0.1/rq
```

To trigger new task (POST using JSON)
```
# Docker
http --json POST http://localhost/jobs type="1"

# Local
http --json POST http://127.0.0.1:5000/jobs type="1"
```

To check all enqueued tasks
```
# Docker
http GET http://localhost:5000/jobs

# Local
http GET http://127.0.0.1:5000/jobs
```
