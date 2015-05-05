# nodediff

version 0.1.0

This is command line tool.
Require two *.ma files arugument.

    $ nodediff a.ma b.ma

This tool parse node name and node type and hierarchy. and print different between two ".ma" files.

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

        + aa:group1(transform)
        +     aa:nurbsPlane2(transform)
        +         aa:nurbsPlaneShape2(nurbsSurface)
        + aa:group3(transform)
        +     aa:group2(transform)
        +         aa:pPyramid1(transform)
        +             aa:pPyramidShape1(mesh)
        + aa:makeNurbPlane1(makeNurbPlane)
        + aa:nurbsPlane1(transform)
        +     aa:nurbsPlaneShape1(nurbsSurface)
        + aa:pPipe1(transform)
        +     aa:pPipeShape1(mesh)
        + aa:polyPipe1(polyPipe)
        + aa:polyPyramid1(polyPyramid)
          defaultLayer(displayLayer)
          defaultRenderLayer(renderLayer)
          front(transform)
              frontShape(camera)
          group1(transform)
        +     nurbsHogePlane2(transform)
        +         nurbsHogePlaneShape2(nurbsSurface)
        -     nurbsPlane2(transform)
        -         nurbsPlaneShape2(nurbsSurface)
          group3(transform)
              group2(transform)
                  pPyramid1(transform)
                      pPyramidShape1(mesh)
        + group5(transform)
        +     group4(transform)
        +         group2(transform)
        +             pPyramid1(transform)
        +                 pPyramidShape1(mesh)
          layerManager(displayLayerManager)
          lightLinker1(lightLinker)
        + locator1(transform)
        +     locatorShape1(locator)
          makeNurbPlane1(makeNurbPlane)
        - makeNurbSphere1(makeNurbSphere)
          nurbsPlane1(transform)
              nurbsPlaneShape1(nurbsSurface)
        - nurbsSphere1(transform)
        -     nurbsSphereShape1(nurbsSurface)
          pPipe1(transform)
              pPipeShape1(mesh)
          persp(transform)
              perspShape(camera)
          polyPipe1(polyPipe)
          polyPyramid1(polyPyramid)
          renderLayerManager(renderLayerManager)
          sceneConfigurationScriptNode(script)
          side(transform)
              sideShape(camera)
          top(transform)
              topShape(camera)
          uiConfigurationScriptNode(script)
        
1. Print diff line only.

  ```shell
  $ nodediff -d testdata/diff-a.ma testdata/diff-b.ma
  $ nodediff --diffonly testdata/diff-a.ma testdata/diff-b.ma
  ```

        + aa:group1(transform)
        +     aa:nurbsPlane2(transform)
        +         aa:nurbsPlaneShape2(nurbsSurface)
        + aa:group3(transform)
        +     aa:group2(transform)
        +         aa:pPyramid1(transform)
        +             aa:pPyramidShape1(mesh)
        + aa:makeNurbPlane1(makeNurbPlane)
        + aa:nurbsPlane1(transform)
        +     aa:nurbsPlaneShape1(nurbsSurface)
        + aa:pPipe1(transform)
        +     aa:pPipeShape1(mesh)
        + aa:polyPipe1(polyPipe)
        + aa:polyPyramid1(polyPyramid)
        +     nurbsHogePlane2(transform)
        +         nurbsHogePlaneShape2(nurbsSurface)
        -     nurbsPlane2(transform)
        -         nurbsPlaneShape2(nurbsSurface)
        + group5(transform)
        +     group4(transform)
        +         group2(transform)
        +             pPyramid1(transform)
        +                 pPyramidShape1(mesh)
        + locator1(transform)
        +     locatorShape1(locator)
        - makeNurbSphere1(makeNurbSphere)
        - nurbsSphere1(transform)
        -     nurbsSphereShape1(nurbsSurface)

1. Print transform diff.

  ```shell
  $ nodediff -w transform testdata/diff-a.ma testdata/diff-b.ma
  $ nodediff --whitelist transform testdata/diff-a.ma testdata/diff-b.ma
  ```

        + aa:group1(transform)
        +     aa:nurbsPlane2(transform)
        + aa:group3(transform)
        +     aa:group2(transform)
        +         aa:pPyramid1(transform)
        + aa:nurbsPlane1(transform)
        + aa:pPipe1(transform)
          front(transform)
          group1(transform)
        +     nurbsHogePlane2(transform)
        -     nurbsPlane2(transform)
          group3(transform)
              group2(transform)
                  pPyramid1(transform)
        + group5(transform)
        +     group4(transform)
        +         group2(transform)
        +             pPyramid1(transform)
        + locator1(transform)
          nurbsPlane1(transform)
        - nurbsSphere1(transform)
          pPipe1(transform)
          persp(transform)
          side(transform)
          top(transform)

1. Print transfrom and mesh diff.  

  ```shell
  $ nodediff -w transform,mesh testdata/diff-a.ma testdata/diff-b.ma
  $ nodediff --whitelist transform,mesh testdata/diff-a.ma testdata/diff-b.ma
  ```

        + aa:group1(transform)
        +     aa:nurbsPlane2(transform)
        + aa:group3(transform)
        +     aa:group2(transform)
        +         aa:pPyramid1(transform)
        +             aa:pPyramidShape1(mesh)
        + aa:nurbsPlane1(transform)
        + aa:pPipe1(transform)
        +     aa:pPipeShape1(mesh)
          front(transform)
          group1(transform)
        +     nurbsHogePlane2(transform)
        -     nurbsPlane2(transform)
          group3(transform)
              group2(transform)
                  pPyramid1(transform)
                      pPyramidShape1(mesh)
        + group5(transform)
        +     group4(transform)
        +         group2(transform)
        +             pPyramid1(transform)
        +                 pPyramidShape1(mesh)
        + locator1(transform)
          nurbsPlane1(transform)
        - nurbsSphere1(transform)
          pPipe1(transform)
              pPipeShape1(mesh)
          persp(transform)
          side(transform)
          top(transform)

1. Print transfrom and mesh diff and diffonly.  

  ```shell
  $ nodediff -d -w transform,mesh testdata/diff-a.ma testdata/diff-b.ma
  $ nodediff --diffonly --whitelist transform,mesh testdata/diff-a.ma testdata/diff-b.ma
  ```

        + aa:group1(transform)
        +     aa:nurbsPlane2(transform)
        + aa:group3(transform)
        +     aa:group2(transform)
        +         aa:pPyramid1(transform)
        +             aa:pPyramidShape1(mesh)
        + aa:nurbsPlane1(transform)
        + aa:pPipe1(transform)
        +     aa:pPipeShape1(mesh)
        +     nurbsHogePlane2(transform)
        -     nurbsPlane2(transform)
        + group5(transform)
        +     group4(transform)
        +         group2(transform)
        +             pPyramid1(transform)
        +                 pPyramidShape1(mesh)
        + locator1(transform)
        - nurbsSphere1(transform)

