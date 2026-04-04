# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  @File    : test_app_handler.py
  @Author  : Yue
  @Date    : 2026/3/30
  @Desc    :
"""
import pytest

from pkg.response import HttpCode


class TestAppHandler:

    @pytest.mark.parametrize("query", [None, "Hello, who is there?"])
    def test_completion(self, query, client):
        resp = client.post("/app/completion", json={"query": query})
        assert resp.status_code == 200
        if not query:
            assert resp.json.get("code") == HttpCode.VALIDATE_ERROR
        else:
            assert resp.json.get("code") == HttpCode.SUCCESS
