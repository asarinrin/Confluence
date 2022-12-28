# Artifactsの利用方法
wandbでのArtifactsについて説明します。

## 1. Artifactとは

wandbにおいて、Artifactは何かしらのデータやモデルのことを指します。  
Artifactを利用すると、データやモデルをWandb上にセーブすることができます。

## 2. Artifactの構築

Artifactの一連の流れは、
1. どんなArtifactかを宣言する。
2. そのArtifactのUriを教える。
3. セーブする。

以上になります。
難しくありませんね。
以下に例を示します。

```
import wandb

run = wandb.init(project="artifacts-tutorial", job_type="job-type")

artifact = wandb.Artifact(name="tutorial_v0", type="dataset")
artifact.add_file(local_path="./tutorial.csv")

run.log_artifact(artifact)
```

## 3. 具体的な話

artifactは、`wandb.Artifact()`のようにして作成します。

引数には、
- Name str型
- Type str型

があります。

Nameにはuniqueになるように命名します。覚えやすくて、説明性のある命名を心がけましょう。  
Typeは`dataset`か`model`のどちらかを選択します。

以下が例です。
```
import wandb

artifact = wandb.Artifact(name="tutorial_v0", type="dataset")
```

続いて、uriによってリソース（データセットとかモデル）を指定して、登録(?)します。
以下が例です。

```
artifact.add_file(local_path="./tutorial.csv")
```
引数には`name`というものがあり、これを指定するとWandBのUI上でartifactのpathを決定できます。  
以下のようにすると、UI上のArtifactは tutorial/tutorial.csv に存在することになります。
```
artifact.add_file(local_path="./tutorial.csv", name="tutorial/tutorial.csv")
```

ちなみに、`artifact.add_dir`や`artifact.new_file`というようなことをできたりします。
さらに`artifact.add_reference`で外部サービス上のリソースを追加できます。

最後に、セーブをします。
`wandb.init()`によってrunインスタンスを作成し、`run.log_artifact()`をすることでWandBにセーブします。

```
run = wandb.init(project="artifacts-tutorial", job_type="job-type")
run.log_artifact(artifact)
```