# MD&AAnalysisFlow

このレポジトリは、学士卒業論文の際に投稿した「新型コロナウイルス感染症前後のテキスト情報比較」でおこなった
有価証券報告書内に記載されているMD＆Aのデータ分析フローをまとめたモノです。

## Description

加藤、五島（2020）を参考に以下の分析方法で取得した流れを記載しています。(下記の文章は自身の学士論文から抜粋)


4.3.1 EDNETが提供しているEDINET APIから有価証券報告書のデータを取得

4.3.2 有価証券報告書内のMD＆Aが記載されているhtmファイルを抽出 

4.3.3 htmファイルからMD＆A情報としてみなされる文章のみを抽出 

4.3.4 抽出した文章群から日本語極性辞書にマッチする単語を特定しトーンを算出

4.3.5 算出したトーンを期間ごとで差の検定で分析

## Requirement

- Dockerを利用し分析することを想定しています

## HowToUse

1. `docker-compose up -d` でdockerコンテナを起動。
2. `localhost:8888`　にアクセスし、任意のipynbファイルを実行。

1~4の順番で各ファイルを実行すると正常に動作すると思われます。

## DirectoryStructure
```
.
├── Dockerfile
├── LICENSE
├── README.md
├── docker-compose.yml
└── src
    ├── 1CallingEdinetApi
    │   ├── EdinetIdxFiles
    │   │   ├── edinet_hirenketsu.csv
    │   │   └── edinet_renketsu.csv
    │   └── calling_edinet_api.ipynb
    ├── 2UnzippingHtm
    │   └── unzipping_htm.ipynb
    ├── 3FetchingMDandA
    │   └── fetching_md_and_a.ipynb
    └── 4AnalysingText
        ├── analyzing_text.ipynb
        ├── composition_of_industries_in_the_sample.ipynb
        └── statistics_on_word_count.ipynb
```

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Reference
加藤 大輔・五島 圭一, 2020, 「有価証券報告書のテキスト分析： 経営者による将来見通しの開示と将来業績」, 『金融研究』, 40巻 3号, 45-75頁。