# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  @File    : config.py
  @Author  : Yue
  @Date    : 2026/3/29
  @Desc    :
"""
import os
from typing import Any

from .default_config import DEFAULT_CONFIG


def _get_env(key: str) -> Any:
    # read from .env, if absent get from default config
    return os.environ.get(key, DEFAULT_CONFIG.get(key))


def _get_bool_env(key: str) -> bool:
    value: str = _get_env(key)
    return value.lower() == "true" if value else False


class Config:
    def __init__(self):
        self.WTF_CSRF_ENABLED = _get_bool_env("WTF_CSRF_ENABLED")
        self.SQLALCHEMY_DATABASE_URI = _get_env("SQLALCHEMY_DATABASE_URI")
        self.SQLALCHEMY_ENGINE_OPTIONS = {
            "pool_size": int(_get_env("SQLALCHEMY_POOL_SIZE")),
            "pool_recycle": int(),
        }
        self.SQLALCHEMY_ECHO = _get_bool_env("SQLALCHEMY_ECHO")
