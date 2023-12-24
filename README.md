# Todoink

Todoink is a simple Flask application written in python that displays Todoist tasks on an e-ink display.
It is designed to run on a Raspberry Pi. Additional drivers for other e-ink displays can be added by implementing the `Display` class.

## API tokens
API tokens for Todoist are required. These can be obtained from the [Todoist developer page](https://developer.todoist.com/appconsole.html).
Once available, they shall be added in a file named config.yaml in the root directory of the project. The file should look like this:
```yaml
TODOIST:
    client_id: <client_id>
    client_secret: <client_secret>
```
