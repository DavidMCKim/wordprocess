from channel.KMA import KMA
from channel.Google import GoogleTrend
from channel.Wordprocess import Wordprocess

if __name__ == '__main__':
    # google = GoogleTrend()
    # word_df = google.Search_TrendWord()
    # words = list(word_df[0].values)
    # word_dict = {}
    # for word in words:
    #     result = google.Search_WordVolume(word)
    #     word_dict.update(result)

    #     print()
    
    # kma = KMA()
    # weather = kma.Parsing_Weather()
    # temparatuer = kma.Parsing_Temparature()

    wordprocess = Wordprocess()
    wordprocess.WriteBlog()


    
    