# Todo CLI

一个使用 Python 开发的命令行待办事项管理工具。

## 当前功能

- 添加待办事项
- 将任务保存到 JSON 文件

## 环境要求

- Python 3.10+

## 安装开发依赖

    python3 -m venv .venv
    source .venv/bin/activate
    python -m pip install -r requirements-dev.txt

## 运行程序

    python todo.py

## 运行测试

    pytest -v

## 数据存储

任务数据保存在 data/tasks.json。

## 项目结构

    keysresp/
    ├── data/
    ├── tests/
    ├── todo.py
    ├── requirements-dev.txt
    └── README.md

## 后续计划

- 查看待办事项
- 完成待办事项
- 删除待办事项
- 增加单元测试
