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
#### 4. 取得したい期間を指定  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L12-L26
#### 5. 取得したいクエリを設定  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L28
#### 6. アウトプットするファイル名を指定  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L33-L35
#### 7. アウトプットするフォルダパスを指定  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L37-L40
#### 8. プロジェクト内に指定したファイルを作成  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L33-L35
#### 9. 実行  
main()を実行します。  
https://github.com/YUTO-KOBAYASHI-CHUO/twittersearch/blob/7cfc44fde0120baa6c63091fdcbd38e3064a6cb5/twittersearch/__main__.py#L11
