# DIとは

Dependency Injection の略です。
これをそのまま訳して依存性の注入とか言われることが多いですが、それでは理解ができません。

「依存する**オブジェクト**をブチ込む」みたいなテンションでいきましょう

カレントディレクトリ内のsample内にサンプルを置いたので見てみてください。
コードを読めばなんとなくわかると思います。

説明を略記すると
```
1. 抽象クラスと具象クラスを作成する
2. 型の解決を行うためのconfigメソッド config(binder: Binder) を作成し、その中でbind(型, to=具象) する
3. Injectorを作成し、configメソッドを吸い込む(codeをみてください)
3'. injectしようとしているメソッドに対して@injectによるデコレータをつける
4. Injector.getで呼び出す
```

以上です。超絶雑なのでreferenceのリンク（公式ドキュメント）を見てみると良いと思います。

# reference
- https://injector.readthedocs.io/en/latest/api.html