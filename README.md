# monitoring-node

Install monitoring-node package.

## Requirements

This role requires Ansible 2.5 or higher,
and platform requirements are listed in the metadata file.

## Testing

This role use [Molecule](https://github.com/metacloud/molecule/) to run tests.

Local tests runs on Docker by default.
See molecule documentation to use other backend.

Currently, tests are done on:
- CentOS 7
- Debian Stretch
- Ubuntu Bionic

and use:
- Ansible 2.5.x
- Ansible 2.6.x

### Running tests

#### Using Docker driver

```
$ tox
```

You can also configure molecule options and molecule command using environment variables:
* `MOLECULE_OPTIONS` Default: "--debug"
* `MOLECULE_COMMAND` Default: "test"

```
$ MOLECULE_OPTIONS='' MOLECULE_COMMAND=converge tox
```

## Role Variables

### Default role variables

``` yaml
```

## Dependencies

None

## Example Playbook

``` yaml
- hosts: servers
  roles:
    - { role: infopen.monitoring-node }
```

## License

''

## Author Information

Alexandre Chaussier (for Infopen company)
- https://infopen.pro
- alexandre.chaussier [at] infopen.pro
