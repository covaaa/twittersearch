# twittersearch

TwitterのAPIを叩いて検索結果のツイート内容を取得するコードを書きました。  
また、検索結果が何ツイートあるかも同時に取得できます。  

### 環境
環境は vscode + pyenv + pipenv です。  
適宜ローカルに対応させてください。  
pythonのバージョン及び使用しているパッケージはpipfileを参照してください。  

### 実行手順

#### 1. Twitter の Developer Portal からトークンを取得 
#### 2. ローカル環境に clone を作成  
#### 3. .env を作成  
```
BEARER_TOKEN="ここにトークンを挿入"
```
#### 4. 取得したい[期間](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L12-L26)を指定  
#### 5. 取得したい[クエリ](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L28)を設定  
#### 6. アウトプットする[ファイル名](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L33-L35)を指定  
#### 7. アウトプットする[フォルダパス](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L37-L40)を指定  
#### 8. プロジェクト内に指定した[ファイル](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L33-L35)を作成  
#### 9. main()を[実行](https://github.com/covaaa/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L11)  
