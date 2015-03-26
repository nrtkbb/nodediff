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

  ```
  ___root___(None)
+     aa:group1(transform)
+         aa:nurbsPlane2(transform)
+             aa:nurbsPlaneShape2(nurbsSurface)
+     aa:group3(transform)
+         aa:group2(transform)
+             aa:pPyramid1(transform)
+                 aa:pPyramidShape1(mesh)
+     aa:makeNurbPlane1(makeNurbPlane)
+     aa:nurbsPlane1(transform)
+         aa:nurbsPlaneShape1(nurbsSurface)
+     aa:pPipe1(transform)
+         aa:pPipeShape1(mesh)
+     aa:polyPipe1(polyPipe)
+     aa:polyPyramid1(polyPyramid)
      defaultLayer(displayLayer)
      defaultRenderLayer(renderLayer)
      front(transform)
          frontShape(camera)
      group1(transform)
          nurbsPlane2(transform)
              nurbsPlaneShape2(nurbsSurface)
      group3(transform)
          group2(transform)
              pPyramid1(transform)
                  pPyramidShape1(mesh)
+     group5(transform)
+         group4(transform)
+             group2(transform)
+                 pPyramid1(transform)
+                     pPyramidShape1(mesh)
      layerManager(displayLayerManager)
      lightLinker1(lightLinker)
+     locator1(transform)
+         locatorShape1(locator)
      makeNurbPlane1(makeNurbPlane)
-     makeNurbSphere1(makeNurbSphere)
      nurbsPlane1(transform)
          nurbsPlaneShape1(nurbsSurface)
-     nurbsSphere1(transform)
-         nurbsSphereShape1(nurbsSurface)
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
  ```

1. Print diff line only.
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -d
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --diffonly
  ```

  ```
+     aa:group1(transform)
+         aa:nurbsPlane2(transform)
+             aa:nurbsPlaneShape2(nurbsSurface)
+     aa:group3(transform)
+         aa:group2(transform)
+             aa:pPyramid1(transform)
+                 aa:pPyramidShape1(mesh)
+     aa:makeNurbPlane1(makeNurbPlane)
+     aa:nurbsPlane1(transform)
+         aa:nurbsPlaneShape1(nurbsSurface)
+     aa:pPipe1(transform)
+         aa:pPipeShape1(mesh)
+     aa:polyPipe1(polyPipe)
+     aa:polyPyramid1(polyPyramid)
+     group5(transform)
+         group4(transform)
+             group2(transform)
+                 pPyramid1(transform)
+                     pPyramidShape1(mesh)
+     locator1(transform)
+         locatorShape1(locator)
-     makeNurbSphere1(makeNurbSphere)
-     nurbsSphere1(transform)
-         nurbsSphereShape1(nurbsSurface)
  ```

1. Print transform diff.
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -w transform
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --whitelist transform
  ```

  ```
+     aa:group1(transform)
+         aa:nurbsPlane2(transform)
+     aa:group3(transform)
+         aa:group2(transform)
+             aa:pPyramid1(transform)
+     aa:nurbsPlane1(transform)
+     aa:pPipe1(transform)
      front(transform)
      group1(transform)
          nurbsPlane2(transform)
      group3(transform)
          group2(transform)
              pPyramid1(transform)
+     group5(transform)
+         group4(transform)
+             group2(transform)
+                 pPyramid1(transform)
+     locator1(transform)
      nurbsPlane1(transform)
-     nurbsSphere1(transform)
      pPipe1(transform)
      persp(transform)
      side(transform)
      top(transform)
  ```

1. Print transfrom and mesh diff.  
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -w transform mesh
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --whitelist transform mesh
  ```

  ```
+     aa:group1(transform)
+         aa:nurbsPlane2(transform)
+     aa:group3(transform)
+         aa:group2(transform)
+             aa:pPyramid1(transform)
+                 aa:pPyramidShape1(mesh)
+     aa:nurbsPlane1(transform)
+     aa:pPipe1(transform)
+         aa:pPipeShape1(mesh)
      front(transform)
      group1(transform)
          nurbsPlane2(transform)
      group3(transform)
          group2(transform)
              pPyramid1(transform)
                  pPyramidShape1(mesh)
+     group5(transform)
+         group4(transform)
+             group2(transform)
+                 pPyramid1(transform)
+                     pPyramidShape1(mesh)
+     locator1(transform)
      nurbsPlane1(transform)
-     nurbsSphere1(transform)
      pPipe1(transform)
          pPipeShape1(mesh)
      persp(transform)
      side(transform)
      top(transform)
  ```

1. Print transfrom and mesh diff and diffonly.  
  ```shell
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma -d -w transform mesh
  $ nodediff testdata/diff-a.ma testdata/diff-b.ma --diffonly --whitelist transform mesh
  ```

  ```
+     aa:group1(transform)
+         aa:nurbsPlane2(transform)
+     aa:group3(transform)
+         aa:group2(transform)
+             aa:pPyramid1(transform)
+                 aa:pPyramidShape1(mesh)
+     aa:nurbsPlane1(transform)
+     aa:pPipe1(transform)
+         aa:pPipeShape1(mesh)
+     group5(transform)
+         group4(transform)
+             group2(transform)
+                 pPyramid1(transform)
+                     pPyramidShape1(mesh)
+     locator1(transform)
-     nurbsSphere1(transform)
  ```
