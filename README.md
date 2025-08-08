# python-mcp-server-demo

A Model Context Protocol (MCP) demo server written in Python.

## Prequisites
- [Python](https://docs.python.org/3/using/index.html) `>= 3.12` - We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to manage your Python environment.
- [pipx](https://pipxproject.github.io/pipx/installation/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/) 
- [Docker and Docker Compose](https://docs.docker.com/get-docker/) - Optional if running via stdio.
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector)

## Requirements

### Python

Please install python `>= 3.12` and `pipx` in your environment. This template uses [uv](https://github.com/astral-sh/uv) to manage the environment and dependencies.

```python
# install uv via pipx
pipx install uv

# sync dependencies
uv sync
```

This opinionated template uses the [`Fast API`](https://fastapi.tiangolo.com/) Python API framework.

### Environment Variable Configuration

The application uses Pydantic's `BaseSettings` for configuration management in `app/config.py`, automatically mapping environment variables to configuration fields.

In CDP, environment variables and secrets need to be set using CDP conventions.  See links below:
- [CDP App Config](https://github.com/DEFRA/cdp-documentation/blob/main/how-to/config.md)
- [CDP Secrets](https://github.com/DEFRA/cdp-documentation/blob/main/how-to/secrets.md)

For local development - see [instructions below](#local-development).

### Linting and Formatting

This project uses [Ruff](https://github.com/astral-sh/ruff) for linting and formatting Python code.

#### Running Ruff

To run Ruff from the command line:

```bash
# Run linting with auto-fix
uv run ruff check . --fix

# Run formatting
uv run ruff format .
```

## Running MCP Server
This MCP server can run in two modes:
1. **Streamable HTTP App**: Runs as a FastAPI application, serving HTTP requests.
2. **Standard Input/Output (stdio)**: Runs as a command-line application that reads from standard input and writes to standard output.

Both of these can be ran locally but the Streamable HTTP App can also be accessed via the Defra CDP platform.

### Streamable HTTP App

To run the Streamable HTTP App, follow the instructions in the [Docker Compose section](#using-docker-compose) or use the provided script.

### Standard Input/Output (stdio)
To run the MCP server in stdio mode, you will need to follow these steps:
1. Sync the dependencies using `uv sync`
2. Build the Python package using `uv build`
3. Install the package globally using `pipx install .` or `pipx install . --force` if you have previously installed it.

Both modes can be tested using the [MCP Inspector](https://github.com/modelcontextprotocol/inspector).

## Local development

### Setup & Configuration

Follow the convention below for environment variables and secrets in local development.

**Note** that it does not use `.env` or `python-dotenv` as this is not the convention in the CDP environment.

**Environment variables:** `compose/aws.env`.

**Secrets:** `compose/secrets.env`. You need to create this, as it's excluded from version control.

**Libraries:** Ensure the python virtual environment is configured and libraries are installed using `uv sync`, [as above](#python)

**Pre-Commit Hooks:** Ensure you install the pre-commit hooks, as above

### Development

This app can be run locally by either using the Docker Compose project or via the provided script `scripts/start_dev_server.sh`.

#### Using Docker Compose

To run the application using Docker Compose, you can use the following command:

```bash
docker compose --profile service up --build
```

If you want to enable hot-reloading, you can press the `w` key once the compose project is running to enable `watch` mode.

#### Using the provided script

To run the application using the provided script, you can execute:

```bash
./scripts/start_dev_server.sh
```

This script will:

- Check if Docker is running
- Start dependent services with Docker Compose (Localstack, MongoDB)
- Set up environment variables for local development
- Load configuration from compose/aws.env and compose/secrets.env
- Verify the Python virtual environment is set up
- Start the FastAPI application with hot-reload enabled

The service will then run on `http://localhost:8085`

### Testing

Ensure the python virtual environment is configured and libraries are installed using `uv sync`, [as above](#python)

Testing follows the [FastApi documented approach](https://fastapi.tiangolo.com/tutorial/testing/); using pytest & starlette.

To test the application run:

```bash
uv run pytest
```

## API endpoints

| Endpoint             | Description                    |
| :------------------- | :----------------------------- |
| `GET: /health`       | Health check endpoint          |

## Custom Cloudwatch Metrics

Uses the [aws embedded metrics library](https://github.com/awslabs/aws-embedded-metrics-python). An example can be found in `metrics.py`

In order to make this library work in the environments, the environment variable `AWS_EMF_ENVIRONMENT=local` is set in the app config. This tells the library to use the local cloudwatch agent that has been configured in CDP, and uses the environment variables set up in CDP `AWS_EMF_AGENT_ENDPOINT`, `AWS_EMF_LOG_GROUP_NAME`, `AWS_EMF_LOG_STREAM_NAME`, `AWS_EMF_NAMESPACE`, `AWS_EMF_SERVICE_NAME`

## Licence

THIS INFORMATION IS LICENSED UNDER THE CONDITIONS OF THE OPEN GOVERNMENT LICENCE found at:

<http://www.nationalarchives.gov.uk/doc/open-government-licence/version/3>

The following attribution statement MUST be cited in your products and applications when using this information.

> Contains public sector information licensed under the Open Government license v3

### About the licence

The Open Government Licence (OGL) was developed by the Controller of Her Majesty's Stationery Office (HMSO) to enable
information providers in the public sector to license the use and re-use of their information under a common open
licence.

It is designed to encourage use and re-use of information freely and flexibly, with only a few conditions.
