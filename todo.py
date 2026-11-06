import json
from pathlib import Path

# 获取当前项目目录
BASE_DIR = Path(__file__).resolve().parent

# 数据文件路径
DATA_FILE = BASE_DIR / "data" / "tasks.json"


def load_tasks():
    """读取已有任务"""
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def save_tasks(tasks):
    """保存任务"""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, ensure_ascii=False, indent=2)


def add_task(title):
    """添加任务"""
    title = title.strip()

    if not title:
        raise ValueError("任务内容不能为空")

    tasks = load_tasks()

    # 自动生成任务编号
    next_id = max(
        (task["id"] for task in tasks),
        default=0
    ) + 1

    task = {
        "id": next_id,
        "title": title,
        "completed": False
    }

    tasks.append(task)
    save_tasks(tasks)

    return task


def main():
    print("===== Todo CLI =====")

    title = input("请输入待办事项：")

    try:
        task = add_task(title)
        print(f"添加成功：[{task['id']}] {task['title']}")
    except ValueError as error:
        print(f"错误：{error}")


if __name__ == "__main__":
    main()
