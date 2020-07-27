#!/usr/bin/env python

"""Tests for `s3_bids_layout` package."""

import pytest

from click.testing import CliRunner

from s3_bids_layout import s3_bids_layout
from s3_bids_layout import cli


# @pytest.fixture
# def response():
#     """Sample pytest fixture.

#     See more at: http://doc.pytest.org/en/latest/fixture.html
#     """
#     # import requests
#     # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


# def test_content(response):
#     """Sample pytest test function with the pytest fixture as an argument."""
#     # from bs4 import BeautifulSoup
#     # assert 'GitHub' in BeautifulSoup(response.content).title.string


# def test_command_line_interface():
#     """Test the CLI."""
#     runner = CliRunner()
#     result = runner.invoke(cli.main)
#     assert result.exit_code == 0
#     assert 's3_bids_layout.cli.main' in result.output
#     help_result = runner.invoke(cli.main, ['--help'])
#     assert help_result.exit_code == 0
#     assert '--help  Show this message and exit.' in help_result.output


def test_parse_s3_uri():
    # Test for correct parsing with the "s3://" prefix
    parsed = s3_bids_layout._parse_s3_uri("s3://bucket/key")
    assert parsed["bucket"] == "bucket"
    assert parsed["key"] == "key"

    #Test without it
    parsed = s3_bids_layout._parse_s3_uri("bucket/key")
    assert parsed["bucket"] == "bucket"
    assert parsed["key"] == "key"

    # Test for ValueError on incorrect formatting
    with pytest.raises(ValueError):
        s3_bids_layout._parse_s3_uri("foo")
