# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  @File    : router.py.py
  @Author  : Yue
  @Date    : 2026/3/24
  @Desc    :
"""
from dataclasses import dataclass

from flask import Blueprint, Flask
from injector import inject

from internal.handler import AppHandler


@inject
@dataclass
class Router:
    """路由"""
    app_handler: AppHandler

    def register_router(self, app: Flask):
        """注册路由"""
        # 1. 创建一个蓝图
        bp = Blueprint("llmops", __name__, url_prefix="")

        # 2. 将url与对应的控制器方法做绑定
        # bp.add_url_rule("/ping", methods=["GET"], view_func=self.app_handler.ping)
        bp.add_url_rule("/apps/<uuid:app_id>/debug", methods=["POST"], view_func=self.app_handler.debug)
        # bp.add_url_rule("/app", methods=["POST"], view_func=self.app_handler.create_app)
        # bp.add_url_rule("/app/<uuid:id>", methods=["GET"], view_func=self.app_handler.get_app)
        # bp.add_url_rule("/app/<uuid:id>", methods=["POST"], view_func=self.app_handler.update_app)
        # bp.add_url_rule("/app/<uuid:id>/delete", methods=["POST"], view_func=self.app_handler.delete_app)

        # 3. 应用上注册blueprint
        app.register_blueprint(bp)
