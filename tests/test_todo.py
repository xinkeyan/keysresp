import pytest
import todo


def test_add_task(tmp_path, monkeypatch):
    """测试正常添加任务"""

    # 使用临时文件保存测试数据
    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(todo, "DATA_FILE", data_file)

    task = todo.add_task("学习 Git")

    assert task["id"] == 1
    assert task["title"] == "学习 Git"
    assert task["completed"] is False

    # 检查数据是否真正保存
    assert todo.load_tasks() == [task]


def test_add_empty_task(tmp_path, monkeypatch):
    """测试不能添加空任务"""

    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(todo, "DATA_FILE", data_file)

    with pytest.raises(ValueError):
        todo.add_task("")


def test_task_id_increment(tmp_path, monkeypatch):
    """测试任务编号自动递增"""

    data_file = tmp_path / "tasks.json"
    monkeypatch.setattr(todo, "DATA_FILE", data_file)

    task1 = todo.add_task("学习 Python")
    task2 = todo.add_task("学习 Git")

    assert task1["id"] == 1
    assert task2["id"] == 2