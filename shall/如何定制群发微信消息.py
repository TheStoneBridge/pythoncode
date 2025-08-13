#  未找到合适的库  进行微信登录
# import pandas as pd
# import itchat_uos as itchat
# from itchat.content import TEXT

# def read_info():
#     # 读取Excel信息
#     df = pd.read_excel(r'C:\Users\yyk\Desktop\wechattest\test1.xls', sheet_name='Sheet1')
#     df = df.loc[:, ~df.columns.str.contains('Unnamed')] 
#     return [i for i in df.to_dict('records')]  


# def make_msg(raw_info):
#     # 生成消息内容
#     t = '{n}先生请于{t}时间在{ad}起飞'
#     return [t.format(n=i['姓名'],
#                      t=i['航班起飞时间'],
#                      ad=i['地点']) 
#                     for i in raw_info]
    
# def init_wechat_client():
#     try:
#         # 扫码登录，hotReload=True 保留登录状态
#         itchat.auto_login(hotReload=True, enableCmdQR=2)
#         print('登录成功')
#         return itchat
#     except Exception as e:
#         print('登录失败:', e)
#         return None

# def get_target_contacts(client, target_names=None):
#     '''获取目标联系人（可根据姓名筛选）'''
#     if not client:
#         return []
#     try:
#         # 获取所有联系人
#         contacts = client.get_friends(update=True)
#         # 如果指定了目标姓名，则筛选联系人（模糊匹配）
#         if target_names:
#             target_contacts = [
#                 contact for contact in contacts
#                 if any(name in contact['NickName'] for name in target_names)
#             ]
#             return target_contacts
#         # 否则返回所有联系人
#         return contacts
#     except Exception as e:
#         print('获取联系人失败:', e)
#         return []

# def send_messages(client, contacts, msg_list):
#     '''向指定联系人批量发送消息'''
#     if not client or not contacts or not msg_list:
#         print('参数错误')
#         return
#     # 确保消息数量与联系人数量匹配（取最小长度）
#     for i in range(min(len(contacts), len(msg_list))):
#         contact = contacts[i]
#         msg = msg_list[i]
#         try:
#             # 发送文本消息(使用联系人的UserName作为唯一标识)
#             client.send_msg(msg, toUserName=contact['UserName'])
#             print(f'已向{contact["NickName"]}发送消息:{msg}')
#         except Exception as e:
#             print(f'向{contact["NickName"]}发送消息失败:{e}')
            
# if __name__ == '__main__':
#     # 1.读取Excel信息并生成消息
#     raw_info = read_info()
#     msg_list = make_msg(raw_info)
    
#     # 2.初始化微信客户端（扫码登录）
#     wechat_client = init_wechat_client()
#     if not wechat_client:
#         exit(1)
    
#     # 3.获取目标联系人
#     target_names = [info['姓名'] for info in raw_info]
#     target_contacts = get_target_contacts(wechat_client, target_names)
    
#     # 4.发送消息
#     send_messages(wechat_client, target_contacts, msg_list)
#     print('发送完成')
    
#     # 5.退出登录
#     wechat_client.logout()
#     print('已退出登录')