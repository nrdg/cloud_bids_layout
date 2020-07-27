#!/usr/bin/env python

"""Tests for `s3_bids_layout` package."""

import botocore
import os.path as op
import pytest
import s3fs
from click.testing import CliRunner
from glob import glob
from moto import mock_s3
from s3_bids_layout import s3_bids_layout as sbl
from s3_bids_layout import cli

DATA_PATH = op.join(op.abspath(op.dirname(__file__)), "data")
TEST_DATASET = "ds000102-mimic"
TEST_BUCKET = "test-bucket"
TEST_S3_KEY = "test-data"


@pytest.fixture
@mock_s3
def s3_setup():
    """pytest fixture to put test_data directory on mock_s3"""
    fs = s3fs.S3FileSystem()
    client = sbl._get_s3_client()
    client.create_bucket(Bucket=TEST_BUCKET)
    fs.put(op.join(DATA_PATH, TEST_DATASET),
           "/".join([TEST_BUCKET, TEST_S3_KEY]),
           recursive=True)


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 's3_bids_layout.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


@mock_s3
def test_get_s3_client():
    client_anon = sbl._get_s3_client(anon=True)
    assert isinstance(client_anon, botocore.client.BaseClient)
    assert client_anon.meta.service_model.service_id == "S3"
    assert client_anon.meta.config.signature_version == botocore.UNSIGNED

    client = sbl._get_s3_client(anon=False)
    assert isinstance(client, botocore.client.BaseClient)
    assert client.meta.service_model.service_id == "S3"
    assert isinstance(client.meta.config.signature_version, str)


def test_parse_s3_uri():
    # Test for correct parsing with the "s3://" prefix
    parsed = sbl._parse_s3_uri("s3://bucket/key")
    assert parsed["bucket"] == "bucket"
    assert parsed["key"] == "key"

    # Test without it
    parsed = sbl._parse_s3_uri("bucket/key")
    assert parsed["bucket"] == "bucket"
    assert parsed["key"] == "key"

    # Test for ValueError on incorrect formatting
    with pytest.raises(ValueError):
        sbl._parse_s3_uri("foo")


@mock_s3
def test_get_matching_s3_keys(s3_setup):
    fnames = [s for s in glob(DATA_PATH, recursive=True) if op.isfile(s)]
    print(fnames)
    matching_keys = list(sbl._get_matching_s3_keys(bucket=TEST_BUCKET, prefix=TEST_S3_KEY))
    print(matching_keys)

    assert set(fnames) == set(matching_keys)
