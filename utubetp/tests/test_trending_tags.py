"""
Tests for the trending_tags module
"""

import unittest
import pandas as pd
from utubetp.trending_tags import time_fmt
from utubetp.trending_tags import split_tags
from utubetp.trending_tags import select_year_and_month


class TestTrendingTags(unittest.TestCase):

    @classmethod
    def test_smoke(self):
        """
        Simple smoke test to make sure function runs.
        """
        df = pd.read_csv("./utubetp/scaled_US_youtube_trending_data.csv", index_col=0)
        tag_df = select_year_and_month(df, 2020, 2020, 9, 9)
        return tag_df

    @classmethod
    def test_one_shot1(self):
        """
        One shot test for testing if split_tags has correct schema.
        """
        df = pd.read_csv("./utubetp/scaled_US_youtube_trending_data.csv", index_col=0)
        tdf = time_fmt(df)
        tag_df = split_tags(tdf)
        assert list(tag_df.columns) == ['frequency', 'tag_name', 'trending_date', 'tags']

    def test_one_shot2(self):
        """
        One shot test for testing if time_fmt has correct schema.
        """
        df = pd.read_csv("./utubetp/scaled_US_youtube_trending_data.csv", index_col=0)
        tdf = time_fmt(df)
        assert list(tdf.columns) == ['video_id', 'title', 'publishedAt', 'channelId', 'channelTitle',
                                     'categoryId', 'trending_date', 'tags', 'view_count', 'likes',
                                     'dislikes', 'comment_count', 'thumbnail_link', 'comments_disabled',
                                     'ratings_disabled']

    def test_edge_timefmt_not_df(self):
        """
        Edge test with wrong type of data input, to see the function can throw a TypeError.
        """
        df_raw = [1, 2, 3, 4, 5]
        with self.assertRaises(TypeError):
            time_fmt(df_raw)

    def test_edge_select_year_and_month_is_not_integer(self):
        """
        Edge test with wrong type of data input, to see the function can throw a TypeError.
        """
        df = pd.read_csv("./utubetp/scaled_US_youtube_trending_data.csv")
        input = [df, '2021', '2021', '11', '11']
        with self.assertRaises(TypeError):
            time_fmt(input)
