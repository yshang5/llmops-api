# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
  @File    : app_handler.py.py
  @Author  : Yue
  @Date    : 2026/3/24
  @Desc    :
"""
import os
from uuid import UUID
from dataclasses import dataclass

from flask import request
from injector import inject

from internal.exception import FailException
from internal.schema.app_schema import CompletionReq
from internal.service import AppService
from pkg.response import *

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser


@inject
@dataclass
class AppHandler:
    """应用控制器"""

    app_service: AppService

    def ping(self):
        raise FailException()

    def debug(self, app_id: UUID):
        """chat interface"""
        # 1. get input
        query = request.json.get('query')
        # 1.1 validate param
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)

        prompt_template = ChatPromptTemplate.from_template("{query}")
        # 2. construct openai request body
        llm = ChatOpenAI(
            base_url=os.getenv("APP_OPENAI_BASE_URL"),
            api_key=os.getenv("APP_OPENAI_API_KEY"),
            model="gpt-5.4-nano"
        )
        parser = StrOutputParser()
        chain = prompt_template | llm | parser

        # 3. full template | call llm | parse
        content = chain.invoke({"query": query})
        return success_json({"content": content})

    def create_app(self):
        app = self.app_service.create_app()
        return success_massage(f"app created successfully: {app.id}")

    def get_app(self, id: uuid.UUID):
        app = self.app_service.get_app(id)
        return success_json(f"app got successfully: {app.name}")

    def update_app(self, id: uuid.UUID):
        app = self.app_service.update_app(id)
        return success_json(f"app updated successfully: {app.name}")

    def delete_app(self, id: uuid.UUID):
        app = self.app_service.delete_app(id)
        return success_json(f"app deleted successfully: {app.id}")
