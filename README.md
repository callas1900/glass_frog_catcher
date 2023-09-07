# Glass Frog Tools

Glass Frog is a holacracy support tool. This tool bagan with motivation just for making metrics for my team.

## How to use

1. First, get your API token from glass flog.
2. prep python (I recommend installing [asdf](https://github.com/asdf-vm/asdf) for installing python)

```
python --version
3.10.11
```
### One shot usage

1. set your API token

```
export GLASS_FLOG_TOKEN={your api token}
```

### Normal usage (recommend)

1. install [direnv](https://github.com/direnv/direnv) 

2. set your API token
```
cp .envrc_sample .envrc
```

3. edit .envrc with your api token from .envrc_sample


