# llm-arc





Access [volcengine.com](https://volcengine.com)(火山方舟) models via API

## Installation

Install this plugin in the same environment as [LLM](https://llm.datasette.io/).

```bash
llm install llm-ark
```

## Usage

Obtain a [Fireworks API key](https://fireworks.ai/api-keys) and save it like this:

```bash
llm keys set ark
# <Paste key here>
```

Run `llm models` to get a list of models.

Run prompts like this:

```bash
llm -m doubao-seed-1.6-250615 'five great names for a pet ocelot'
```

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

```bash
cd llm-ark
python3 -m venv venv
source venv/bin/activate
```

Now install the dependencies and test dependencies:

```bash
llm install -e '.[test]'
```

To run the tests:

```bash
pytest
```
