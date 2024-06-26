import os
from dotenv import load_dotenv
# because this code is run as a dependency to Pacer-Scraper, we need to load the .env from the main project level
load_dotenv("/scrapyrt/src/.env")

# -*- coding: utf-8 -*-
"""Default scrapyrt settings."""

# Project settings module - found at server initialization
PROJECT_SETTINGS = None

# Path to server log file
LOG_FILE = os.environ.get("SCRAPYRT_SERVER_LOG_FILE")

# Spider logs will be kept in file with name set to timestamp in following
# format
SPIDER_LOG_FILE_TIMEFORMAT = '%Y-%m-%dT%H%M%S.%f'

# Path to spiders log directory
LOG_DIR = os.environ.get("SCRAPYRT_SERVER_LOG_DIR")

LOG_ENCODING = 'utf-8'

# Root server resource, should inherit from scrapyrt.resources.RealtimeAPI
SERVICE_ROOT = 'scrapyrt.resources.RealtimeApi'

# Resources list
RESOURCES = {
    'crawl.json': 'scrapyrt.resources.CrawlResource',
}

CRAWL_MANAGER = 'scrapyrt.core.CrawlManager'

# Limit spider run time
TIMEOUT_LIMIT = 1000
# disable in production
DEBUG = True

TWISTED_REACTOR = None

DEFAULT_ERRBACK_NAME = None
