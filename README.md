# nmerror

A simple TCP server that listens for incoming connections on a specified host and port. When a client connects, it establishes a connection to the target host and port, and then echoes all data received from the client to the target host and vice versa.

## Create virtual environment


```
python3 -m venv .venv
```

## Enable virtual environment

On Windows, run via PowerShell:

```
.venv\bin\Activate.ps1
```

On Unix or MacOS, run:

```
source .venv/bin/activate
```

## Install dependencies

```
python -m pip install -r requirements.txt
```

## Usage

The command below will forward the traffic from `127.0.0.1:3003` to `aakodadi.com:443`

```
./nmirror.py --host 127.0.0.1 --port 3003 --target-host akodadi.com --target-port 443
```

You can now open https://127.0.0.1:3003 on a browser and (apart from the invalid certificate warning) it will be as if you visited https://akodadi.com directly.

If you prefer the short options, the command would look like this:

```
./nmirror.py -l 127.0.0.1 -p 3003 -L akodadi.com -P 443
```

Run `./nmirror.py --help` for more options.

## [Contributers] Update packages list

If a new package is used in the project installed via `pip install <package>`, update the packages list:

```
pip freeze > requirements.txt
```

## Disable virtual environment

```
deactivate .venv
```