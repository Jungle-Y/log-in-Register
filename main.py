"""
注册登录功能
注册模块
    (1)操作文件 user.txt
    (2)录入用户的账号+密码   (账号不能重复)

登录模块
    (1)操作文件 user.txt
    (2)读取所有的用户信息,进行匹配
            如果存在一致的账号和密码, 提示登录成功
            如果不存在....         , 提示账号/密码错误
"""
choice = input("请输入注册/登录: ")
if choice == '注册':
    # 注册功能
    username = input("请输入账号: ")
    password = input("请输入密码: ")
    # 检测账号是否已存在于 user.txt
    f = open('user.txt', 'r', encoding='UTF-8')
    content = f.readlines()  # ['kk||1234\n', 'ff||4321\n', '亚鹏||3333\n']
    # for循环结束都没有找到和用户本次输入的一模一样的账号
    # for循环过程中, 发现了用户本次输入的账号已存在于user.txt中,强制结束循环
    has_no_exist = True  # 假设该账号不存在
    for info in content:  # ['kk||1234\n', 'ff||4321\n', 'xx||3333\n']
        tuple1 = info.partition("||")  # ('kk', '||', '1234\n')
        if username == tuple1[0]:  # 'kk' , 'ff'
            print("账号已存在")
            has_no_exist = False  # 此时,账号已存在
            break
    f.close()

    if has_no_exist:
        # 录入user.txt
        f = open('user.txt', 'a', encoding='UTF-8')
        # 账号密码无法区分
        u_p = username + '||' + password + '\n'
        f.write(u_p)
        f.close()
elif choice == "登录":
    # 登录功能
    username = input("请输入账号:  ")
    password = input("请输入密码:  ")
    f = open("user.txt", 'r', encoding='UTF-8')
    contens = f.readlines()
    for info in contens:  # 'kk||1234\n', 'ff||4321\n', 'xx||3333\n'
        # 去除 \n
        info1 = info.replace("\n", "")  # 'kk||1234'
        # 按照 || 分割
        info2 = info1.split("||")  # ['kk', '1234']
        if username == info2[0] and password == info2[1]:
            print("登录成功")
            break
    else:
        print("登录失败")
else:
    print("输入有误, 请输入注册/登录!!")