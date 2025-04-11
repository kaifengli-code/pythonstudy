# 初始化一个空的图书列表
books = []

# 定义添加图书的函数
def add_book():
    title = input("请输入图书的书名: ")
    author = input("请输入图书的作者: ")
    book = {"title": title, "author": author}
    books.append(book)
    print(f"图书《{title}》已成功添加。")

# 定义显示图书列表的函数
def display_books():
    if not books:
        print("当前没有图书记录。")
    else:
        print("图书列表如下：")
        for index, book in enumerate(books, start=1):
            print(f"{index}. 书名: {book['title']}, 作者: {book['author']}")

# 定义查找图书的函数
def find_book():
    title = input("请输入要查找的图书的书名: ")
    found = False
    for book in books:
        if book["title"] == title:
            print(f"找到图书：书名: {book['title']}, 作者: {book['author']}")
            found = True
            break
    if not found:
        print(f"未找到名为《{title}》的图书。")

# 定义删除图书的函数
def delete_book():
    title = input("请输入要删除的图书的书名: ")
    for book in books:
        if book["title"] == title:
            books.remove(book)
            print(f"图书《{title}》已成功删除。")
            return
    print(f"未找到名为《{title}》的图书，无法删除。")

# 主程序循环
while True:
    print("\n请选择操作：")
    print("1. 添加图书")
    print("2. 显示图书列表")
    print("3. 查找图书")
    print("4. 删除图书")
    print("5. 退出系统")
    choice = input("请输入你的选择 (1-5): ")

    if choice == "1":
        add_book()
    elif choice == "2":
        display_books()
    elif choice == "3":
        find_book()
    elif choice == "4":
        delete_book()
    elif choice == "5":
        print("感谢使用图书管理系统，再见！")
        break
    else:
        print("无效的选择，请输入 1-5 之间的数字。")