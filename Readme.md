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
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma
  ```

1. Print diff line only.
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -d
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --diffonly
  ```

1. Print transform diff.
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -w transform
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --whitelist transform
  ```

1. Print transfrom and mesh diff.  
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -w transform mesh
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --whitelist transform mesh
  ```
