# ghostty

## Description

This repository contains spec files for building `ghostty` terminal emulator RPM packages and its dependencies.

Packages are built and published by [spec-package-builder](https://github.com/damex-el-packages/spec-package-builder) pipeline.

Currently, packages and their corresponding spec files are built and tested only for `Red Hat Enterprise Linux 10` and its derivatives like `Alma Linux 10` and `Rocky Linux 10`.

Packages are built only for `x86_64`.
`zig` in `EPEL` is available only for `x86_64`.

[Follow here if you want to use prebuilt packages](#using-prebuilt-packages).

## Using prebuilt packages

### Add damex-ghostty repository with prebuilt packages

To add `damex-ghostty` repository to `Red Hat Enterprise Linux 10` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/ghostty/el/10/x86_64/damex-ghostty-release-0.1.0-1.el10.x86_64.rpm
```

Alternatively, it can be done manually by adding the following configuration to `/etc/yum.repos.d/damex-ghostty.repo`:

```sh
[damex-ghostty]
name = damex-ghostty
baseurl = https://yum-repositories.damex.org/ghostty/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/ghostty/ghostty-2036-09-27.asc
```

### List of prebuilt packages

| Package                | Repository    | Architecture | Distributives               |
|------------------------|---------------|--------------|-----------------------------|
| ghostty-tip            | damex-ghostty | x86_64       | Red Hat Enterprise Linux 10 |
| gtk4-layer-shell       | damex-ghostty | x86_64       | Red Hat Enterprise Linux 10 |
| gtk4-layer-shell-devel | damex-ghostty | x86_64       | Red Hat Enterprise Linux 10 |

`ghostty-tip` is rebuilt weekly from upstream `tip`.
Package version is build date.
`ghostty-tip` provides `ghostty` and conflicts with other `ghostty` packages.
