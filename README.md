# XOS TOSCA

Welcome to the XOS TOSCA.

## Documentation
You can find the documentation in the `docs` folder. It has been created using `gitbook` and can be consumed as a local website.
To bring it up, just open a termina pointing to this folder and execute: `gitbook serve`, then open a browser at `http://localhost:4000`

## Support

For support please refer to:

**Slack**<br/>
[slackin.opencord.org](https://slackin.opencord.org/)

**Mailing List**<br/>
[CORD Discuss](https://groups.google.com/a/opencord.org/forum/#!forum/cord-discuss)<br/>
[CORD Developers](https://groups.google.com/a/opencord.org/forum/#!forum/cord-dev)

**Wiki**<br/>
[wiki.opencord.org](https://wiki.opencord.org/)


## Testing

To run tests, you must first create a virtualenv with the XOS dependencies:

```shell
cd ../xos
./scripts/setup_venv.sh
source venv-xos/bin/activate
cd ../xos-tosca
make tests
```
