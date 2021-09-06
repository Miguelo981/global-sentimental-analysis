# install.sh
#!/usr/bin/env bash
python setup.py install
python -m textblob.download_corpora
git clone https://github.com/sugiyamath/sentiment_ja
python sentiment_ja/setup.py install