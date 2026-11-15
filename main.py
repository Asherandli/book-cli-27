# -*- coding: utf-8 -*-
"""
book-cli - 简易命令行图书管理工具
功能：图书增删改查、分类筛选、本地JSON持久化存储
"""

import json
import os

DATA_FILE = "books.json"


def load_books():
    """从JSON文件加载图书数据"""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []


def save_books(books):
    """将图书数据保存到JSON文件"""
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(books, f, ensure_ascii=False, indent=2)


def add_book(books):
    """添加图书"""
    name = input("请输入书名：").strip()
    author = input("请输入作者：").strip()
    category = input("请输入分类（如：计算机/文学/经管）：").strip()

    if not name or not author:
        print("书名和作者不能为空！")
        return

    book = {
        "name": name,
        "author": author,
        "category": category if category else "未分类"
    }
    books.append(book)
    save_books(books)
    print(f"《{name}》 添加成功！")


def list_books(books):
    """列出所有图书"""
    if not books:
        print("书库为空。")
        return
    print("\n===== 图书列表 =====")
    for i, book in enumerate(books, 1):
        print(f"{i}. 《{book['name']}》 - {book['author']} [{book['category']}]")


def search_book(books):
    """按书名关键词搜索"""
    keyword = input("请输入搜索关键词：").strip()
    results = [b for b in books if keyword in b["name"] or keyword in b["author"]]
    if not results:
        print("未找到匹配的图书。")
        return
    print(f"\n找到 {len(results)} 条结果：")
    for i, book in enumerate(results, 1):
        print(f"{i}. 《{book['name']}》 - {book['author']} [{book['category']}]")


def filter_by_category(books):
    """按分类筛选"""
    cate = input("请输入要筛选的分类：").strip()
    results = [b for b in books if b["category"] == cate]
    if not results:
        print(f"分类「{cate}」下暂无图书。")
        return
    print(f"\n分类「{cate}」下的图书：")
    for i, book in enumerate(results, 1):
        print(f"{i}. 《{book['name']}》 - {book['author']}")


def delete_book(books):
    """删除图书"""
    list_books(books)
    if not books:
        return
    try:
        idx = int(input("请输入要删除的图书序号：")) - 1
        if 0 <= idx < len(books):
            removed = books.pop(idx)
            save_books(books)
            print(f"《{removed['name']}》 已删除。")
        else:
            print("序号无效。")
    except ValueError:
        print("请输入有效数字。")


def show_menu():
    """显示主菜单"""
    print("\n===== book-cli 图书管理系统 =====")
    print("1. 查看全部图书")
    print("2. 添加图书")
    print("3. 关键词搜索")
    print("4. 按分类筛选")
    print("5. 删除图书")
    print("0. 退出")


def main():
    books = load_books()
    while True:
        show_menu()
        choice = input("请选择操作：").strip()
        if choice == "1":
            list_books(books)
        elif choice == "2":
            add_book(books)
        elif choice == "3":
            search_book(books)
        elif choice == "4":
            filter_by_category(books)
        elif choice == "5":
            delete_book(books)
        elif choice == "0":
            print("已退出系统，数据已保存。")
            break
        else:
            print("无效选项，请重新输入。")


if __name__ == "__main__":
    main()
