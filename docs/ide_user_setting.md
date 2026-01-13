## Ide user settings (json)

Below is a standard configuration for an IDE  ctr + shift + p. Open user settings (JSON)

```json
{
    "mssql.connectionGroups": [
        {
            "name": "ROOT",
            "id": "C489522A-E9AC-404D-B042-864654750628"
        },
        {
            "name": "Local Development",
            "description": "staging,development database",
            "color": "#2C701B",
            "id": "666896FD-75A2-4783-BCD5-4009021BE858",
            "parentId": "C489522A-E9AC-404D-B042-864654750628"
        }
    ],
    "mssql.connections": [
        {
            "authenticationType": "SqlLogin",
            "connectTimeout": 30,
            "applicationName": "vscode-mssql",
            "applicationIntent": "ReadWrite",
            "profileName": "Local IMT",
            "groupId": "666896FD-75A2-4783-BCD5-4009021BE858",
            "server": "192.168.0.27",
            "trustServerCertificate": true,
            "user": "imt",
            "password": "",
            "savePassword": true,
            "id": "F27D0299-90FC-47A4-A70C-C7D0D88D7F8E",
            "database": "internaltoolset",
            "commandTimeout": 30,
            "profileSource": 0,
            "encrypt": "Mandatory"
        }
    ],
    "[python]": {        
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.fixAll": "explicit",
        "source.fixAll.ruff": "explicit"
    }     
},
"editor.accessibilitySupport": "off",
"files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true
}
}



## .vscode/settings.json  (in your project root)

```json
{  
  "python.analysis.typeCheckingMode": "strict"
}



## ruff setting for static code analysis

```toml
[tool.ruff]
line-length = 88
# Exclude common directories
exclude = [".git", ".mypy_cache", ".ruff_cache", "venv", ".venv", "dist"]

[tool.ruff.lint]
# E: pycodestyle, F: Pyflakes, I: isort, UP: pyupgrade, B: flake8-bugbear
select = ["E", "F", "I", "UP", "B","ANN"]
ignore = ["E501"]  # Ignore line-length violations (let the formatter handle it)
fixable = ["ALL"]

[tool.ruff.format]
# Standard settings that mimic Black's behavior
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.ruff.lint.flake8-annotations]
# Optional: Ignore missing types for 'self' and 'cls' to reduce noise
allow-star-arg-any = true
ignore-fully-untyped = false
suppress-none-returning = false 

[tool.mypy]
python_version = "3.13"
strict = true  # Enables almost all optional strictness flags
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_return_any = true
warn_unreachable = true

# Handle third-party libraries that might not have type hints
ignore_missing_imports = true

# Ensure your explicit type checks are actually used
disallow_untyped_defs = true
disallow_incomplete_defs = true




## complete toml exmaple

```toml
[project]
name = "flightdeck-etl"
version = "0.1.0"
description = "This is a flightdeck etl project"
authors = [
    {name = "Sudip Ranabhat",email = "sudip.ranabhat@omc.com"}
]
readme = "README.md"
requires-python = ">=3.13, <4.0"

[tool.poetry]
packages = [{include = "flightdeck_etl", from = "src"}]

[tool.poetry.dependencies]
pydantic = "^2.6.0" 
pydantic-settings = "^2.2.1" 
httpx = "^0.27.0" 
structlog = "^24.1.0" 
openai = "^1.52.0" 
psycopg2-binary = "^2.9.10" 
abs2rel = "^1.1.0"
python-dateutil = "^2.9.0.post0"
rodi = "^2.0.8"
pyodbc = "^5.3.0"
snowflake-connector-python = {extras = ["pandas"], version = "^4.2.0"}
databricks-sql-connector = "^4.2.4"
aiosmtplib = "^5.0.0"


[tool.poetry.group.dev.dependencies] 
ruff = "^0.5.0" 
black = "^24.8.0" 
isort = "^5.13.2" 
mypy = "^1.11.1" 
pytest = "^8.3.3" 
pre-commit = "^3.8.0" 

[tool.ruff]
line-length = 88
# Exclude common directories
exclude = [".git", ".mypy_cache", ".ruff_cache", "venv", ".venv", "dist"]

[tool.ruff.lint]
# E: pycodestyle, F: Pyflakes, I: isort, UP: pyupgrade, B: flake8-bugbear
select = ["E", "F", "I", "UP", "B","ANN"]
ignore = ["E501"]  # Ignore line-length violations (let the formatter handle it)
fixable = ["ALL"]

[tool.ruff.format]
# Standard settings that mimic Black's behavior
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"

[tool.ruff.lint.flake8-annotations]
# Optional: Ignore missing types for 'self' and 'cls' to reduce noise
allow-star-arg-any = true
ignore-fully-untyped = false
suppress-none-returning = false 

[tool.mypy]
python_version = "3.13"
strict = true  # Enables almost all optional strictness flags
warn_unused_configs = true
warn_redundant_casts = true
warn_unused_ignores = true
warn_return_any = true
warn_unreachable = true

# Handle third-party libraries that might not have type hints
ignore_missing_imports = true

# Ensure your explicit type checks are actually used
disallow_untyped_defs = true
disallow_incomplete_defs = true

[build-system]
requires = ["poetry-core>=2.0.0,<3.0.0"]
build-backend = "poetry.core.masonry.api"

