# Union-Findとは

- グループ分けを効率的に管理するデータ構造であり、根付き木の構造を用いる
- 多くのグラフに関する問題の多くを解ける
- 以下のクエリを高速に処理するもの
  - issame(x,y)：要素x,yが同じグループに属するか判定
    - root(x)とroot(y)とが等しいかどうかを判定する
  - unite(x,y)：要素xを含むグループと、要素yを含むグループとを併合する
    - rx = root(x), ry = root(y) として、頂点rx が 頂点ryの子頂点となるようにつなぐ

## 計算量削減の工夫

1. union by size 

  unite()でのグループ併合時に、サイズが小さい方の根を頂点とする

2. 経路圧縮

  xから上に進んでいき根に到達するまでの経路中の頂点に対して、その親を根に張り替える