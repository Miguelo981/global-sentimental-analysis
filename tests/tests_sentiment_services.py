from lib.sentiment_services import AnalyzedSetence


def test_lang_sentiment_analysis(lang="ja-JP", sentence=['ビットコインは10万ドルに到達し、世界的な準備資産になる＝ブルームバーグのシニアストラテジスト', '南アフリカの金融規制当局、バイナンスに対して警告']):
    analyzer = AnalyzedSetence(lang=lang)
    print(analyzer.analyze(sentence))

test_lang_sentiment_analysis()