from sentiment_ja.sentimentja import Analyzer
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
from textblob_fr import PatternTagger as PatternTaggerFr, PatternAnalyzer as PatternAnalyzerFr
from textblob_de import TextBlobDE, PatternTagger as PatternTaggerDe
from pysentimiento import SentimentAnalyzer, EmotionAnalyzer


class TextSentiment():
    def __init__(self, classification, positive, negative, emotions=dict()):
        self.classification = classification
        self.positive = positive
        self.neagative = negative
        self.emotions = emotions

class AnalyzedSetence():
    def __init__(self, lang="en"):
        self.lang = lang

        if self.lang == "es" or self.lang == "es-ES":
            self.es_emotion_analyzer = EmotionAnalyzer(lang="es")
            self.es_analyzer = SentimentAnalyzer(lang="es")
        elif self.lang == "ja" or self.lang == "ja-JP":
            self.analyzer = Analyzer()

    def analyze(self, sentence):
        if self.lang == "es" or self.lang == "es-ES":
            return self.analyze_es_sentence(sentence)
        elif self.lang == "ja" or self.lang == "ja-JP":
            return self.analyze_jp_sentence(sentence)
        elif self.lang == "en" or self.lang == "en-EN":
            return self.analyze_en_sentence(sentence)
        elif self.lang == "de" or self.lang == "de-DE":
            return self.analyze_de_sentence(sentence)
        elif self.lang == "fr" or self.lang == "fr-FR":
            return self.analyze_fr_sentence(sentence)

    def analyze_jp_sentence(self, sentence):
        t_sentiments = []
        sentiment = self.analyzer.analyze(sentence)
        for text in sentiment:
            max_key = max(text['emotions'], key=text['emotions'].get)
            t_sentiments.append(TextSentiment(max_key, 0, 0, text['emotions']))
        return t_sentiments

    def analyze_en_sentence(self, sentence):
        opinion = TextBlob(sentence, analyzer=NaiveBayesAnalyzer())
        sentiment = opinion.sentiment
        t_sentiment = TextSentiment(sentiment[0], sentiment[1], sentiment[2])
        return t_sentiment

    def analyze_es_sentence(self, sentence):
        return self.es_analyzer.predict(sentence)

    def analyze_es_joy(self, sentence):
        return self.es_emotion_analyzer.predict(sentence)

    def analyze_fr_sentence(self, sentence):
        opinion = TextBlob(sentence, pos_tagger=PatternTaggerFr(), analyzer=PatternAnalyzerFr())
        return opinion.sentiment

    def analyze_de_sentence(self, sentence):
        opinion = TextBlobDE(sentence, pos_tagger=PatternTaggerDe(include_punc=True))
        return opinion.sentiment