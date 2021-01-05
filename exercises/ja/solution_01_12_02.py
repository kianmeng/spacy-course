import spacy
from spacy.matcher import Matcher

nlp = spacy.load("ja_core_news_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "松島、天橋立、宮島は日本三景として知られています。"
    "松島は宮城県、天橋立は京都府、宮島は広島県にそれぞれあります。"
)

# v2.3現在、日本語モデルではdoc.is_taggedが正しく設定されないので、
# 明示的に設定
# 参考: https://github.com/explosion/spaCy/issues/5802
doc.is_tagged = True

# 「固有名詞 + 県」からなるパターンを書きます
pattern = [{"POS": "PROPN"}, {"LEMMA": "県"}]

# パターンをmatcherに追加し、docに対してmatcherを適用します
matcher.add("PREFECTURE_PATTERN", None, pattern)
matches = matcher(doc)
print("Total matches found:", len(matches))

# 結果をイテレートし、スパンの文字列をプリントします
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)
