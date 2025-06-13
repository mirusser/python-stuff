### How to create python lambda using AWS SAM

Watch this [video](https://www.youtube.com/watch?v=fEZE3rm8Ma8) for reference
# Prerequisites
Install:
[[AWS CLI]] and configure profile (authenticate w/ AWS)
[AWS SAM](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html)
[[Docker]]

Create a directory for a project:
```bash
mkdir <project-directory>
```

Go to that directory:
```bash
cd <project-directory>
```

# Init

Inside project directory use (interactive) command to create lambda:
```bash
sam init
```

Use `HelloWorld` template, python and zip

# Build

To build/rebuild project use:
```bash
sam build
```
# Deploy

First time:
```bash
sam deploy --guided --profile mirusser
```

Subsequent deploys:
```bash
sam deploy
```

# Invoke

## Local invoke (local testing)

Create `event.json` file in `events` directory
Use command:
```bash
sam local invoke <function-handler> -e events/event.json
```
# Delete stack
```bash
aws cloudformation delete-stack --stack-name <stack-name>
```

or
```bash
sam delete --stack-name <stack-name>
```


# Debug locally

Have these installed (globally or locally):
```bash
sudo pacman -S python-debugpy
pip install --target . debugpy
```


`requirements.txt` file should have entry: 
```
...
requests
debugpy
...
```

In VS Code `launch.json` debug configuration should look something like this:
```json
{

	"version": "0.2.0",

	"configurations": [

		{

			"name": "Attach to SAM Python Lambda",

			"type": "debugpy",

			"request": "attach",

			"connect": {

				"host": "127.0.0.1",

				"port": 5678

			},

			"pathMappings": [

			{

				"localRoot": "${workspaceFolder}/basic",

				"remoteRoot": "/var/task"

			}]

		}

	]

}
```

In console (in root directory of a project):
to build:
```bash
sam build --use-container
```

to run locally (in docker):
```bash
DEBUGGER_ARGS="-Xfrozen_modules=off" sam local invoke <function-handler> -d 5678 --event events/event.json
```

then in VS Code attach debugger



















