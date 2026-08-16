"""
  @File    : schema.py
  @Author  : Yue
  @Date    : 2026/5/23 11:12
  @Desc    : 
"""
from wtforms import Field


class ListField(Field):
    data: list = None

    def process_formdata(self, valuelist):
        if valuelist and isinstance(valuelist, list):
            self.data = valuelist

    def _value(self):
        return self.data if self.data else []
