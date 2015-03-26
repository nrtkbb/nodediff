# nodediff

version 0.0.1

## How to install

1. download python file.  
  [Download link](https://raw.githubusercontent.com/nrtkbb/nodediff/master/nodediff)

1. Change mode.  
  ```shell
  $ chmod 755 nodediff
  ```

1. Move to your bin path.  
  ```shell
  $ mv nodediff /your/bin/path
  ```

## How to use

1. Print nodename and nodetype diff.
  ```shell
  $ nodediff filea.ma fileb.ma
  ```

1. Print diff line only.
  ```shell
  $ nodediff filea.ma fileb.ma -d
  $ nodediff filea.ma fileb.ma --diffonly
  ```

1. Print transform diff.
  ```shell
  $ nodediff filea.ma fileb.ma -w transform
  $ nodediff filea.ma fileb.ma --whitelist transform
  ```

1. Print transfrom and mesh diff.  
  ```shell
  $ nodediff filea.ma fileb.ma -w transform mesh
  $ nodediff filea.ma fileb.ma --whitelist transform mesh
  ```
