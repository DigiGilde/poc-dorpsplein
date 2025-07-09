export COMPOSE_FILE := "docker-compose.yml"

# Default command to list all available commands.
default:
  @just --list

# Update dependencies.
update:
  echo "Updating project dependencies..."
  uv lock --upgrade
  echo "Updating pre-commit dependencies..."
  pre-commit autoupdate

# Run pre-commit checks.
lint:
  echo "Running pre-commit checks..."
  pre-commit run --all-files

# Build python image.
build *args:
  echo "Building python image..."
  docker compose build

# Start up containers.
up:
  echo "Starting up containers..."
  docker compose up --watch --remove-orphans

# Remove containers and their volumes.
prune *args:
  echo "Killing containers and removing volumes..."
  docker compose down --volumes {{args}}

# View container logs
logs *args:
  docker compose logs --follow --tail 100 {{args}}

# Executes `manage.py` command.
manage *args="--help":
  docker compose run --rm django python ./manage.py {{args}}
