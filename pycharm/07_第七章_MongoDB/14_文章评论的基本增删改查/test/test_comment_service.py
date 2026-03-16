# 解决模块导入问题：添加项目根目录到Python路径
import sys
import os
# 获取当前文件（test_comment_service.py）的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 获取项目根目录（tests的上一级）
project_root = os.path.dirname(current_dir)
# 把根目录加入搜索路径
sys.path.append(project_root)


import unittest 
from datetime import datetime
from models.comment import Comment
from services.comment_service import CommentService

class TestCommentService(unittest.TestCase):
    """评论服务单元测试类（对应Spring的@Test注解）"""   
    # 测试用例共享的变量
    test_comment_id = None  # 用于存储测试评论的ID，供后续测试用例使用
    test_user_id = '1003' # 用于存储测试用户ID，供后续测试用例使用


    def setUp(self):
        """初始化Service，确保每个测试方法独立"""
        self.comment_service = CommentService()
        # 清空测试数据（避免脏数据影响测试结果
        self._clean_test_data()

    # ========== 每个测试方法执行后清理（对应Spring的@AfterEach）==========
    def tearDown(self):
        """清理测试数据，保证环境干净"""
        self._clean_test_data()
        # pass

    # ========== 私有辅助方法（清理测试数据）==========
    def _clean_test_data(self):
        """删除测试用户的所有评论"""
        comments = self.comment_service.get_comments_by_user_id(self.test_user_id)
        for comment in comments:
            self.comment_service.delete_comment_by_id(str(comment.id))

    # ========== 具体测试用例（每个方法对应一个功能，可单独运行）==========
    def test_add_comment(self):
        """测试新增评论功能"""
        # 1. 准备测试数据
        test_comment = Comment(
            articleId="100000",
            content="单元测试新增评论3",
            userId=self.test_user_id,
            nickname="测试用户"
        )
        # 2. 调用被测试方法
        comment_id = self.comment_service.add_comment(test_comment)
        self.test_comment_id = comment_id # 存储测试评论ID供后续测试使用

        # 3. 断言结果   
        self.assertIsNotNone(comment_id)  # ID不为空
        self.assertEqual(len(comment_id), 24)  # MongoDB的ID长度为24位

    def test_get_comment_by_id(self):
         """测试根据ID查询评论功能"""
         # 1. 准备测试数据
         self.test_add_comment()  # 先新增一个评论，获取其ID
         #2.执行查询方法
         comment = self.comment_service.get_comment_by_id(self.test_comment_id)
         # 3. 断言结果
         print("查到的评论：", comment.to_dict())
         self.assertIsNotNone(comment)  # 评论不为空
         self.assertEqual(comment.userId, self.test_user_id)  # 用户ID正确
         self.assertEqual(comment.content, "单元测试新增评论")  # 评论内容正确


    def test_get_comments_by_user_id(self):
        """测试根据用户ID查询评论列表功能"""
        # 1. 新增两条测试评论
        comment1 = Comment(
            articleId="100000",
            content="测试评论1",
            userId=self.test_user_id,
            nickname="测试用户"
        )
        comment2 = Comment(
            articleId="100001",
            content="测试评论2",
            userId=self.test_user_id,
            nickname="测试用户"
        )
        self.comment_service.add_comment(comment1)
        self.comment_service.add_comment(comment2)
        # 2. 执行查询方法
        comments = self.comment_service.get_comments_by_user_id(self.test_user_id)
        # 3. 断言验证
        self.assertEqual(len(comments), 2)  # 列表长度为2
        self.assertEqual(comments[0].content, "测试评论1")  # 第一条内容匹配

    def test_update_comment_nickname(self):
        """测试更新评论昵称功能"""
        # 1. 先新增一条评论
        self.test_add_comment()
        # 2. 执行更新方法
        new_nickname = "更新后的测试昵称"
        update_success = self.comment_service.update_comment_nickname(
            self.test_comment_id, new_nickname
        )
        # 3. 断言验证更新结果
        self.assertEqual(update_success, True)  # 更新成功
        # 4. 查询验证昵称是否真的更新
        updated_comment = self.comment_service.get_comment_by_id(self.test_comment_id)
        self.assertEqual(updated_comment.nickname, new_nickname)  # 昵称匹配

    def test_delete_comment_by_id(self):
        """测试删除评论功能"""
        # 1. 先新增一条评论
        self.test_add_comment()
        # 2. 执行删除方法
        delete_success = self.comment_service.delete_comment_by_id(self.test_comment_id)
        # 3. 断言验证删除结果
        self.assertEqual(delete_success, True)  # 删除成功
        # 4. 查询验证评论是否真的删除
        deleted_comment = self.comment_service.get_comment_by_id(self.test_comment_id)
        self.assertIsNone(deleted_comment)  # 评论应为None

    def test_get_comments_by_user_id_page(self):
            for i in range(12):
                comment = Comment(
                    articleId=f"test_article_{i}",
                    content=f"分页测试内容 {i}",
                    userId=self.test_user_id,  # 固定测试用户ID
                    nickname="测试用户"
                )
                self.comment_service.add_comment(comment)
            
            # 2. 调用分页：第1页，每页5条
            page_1 = self.comment_service.get_comments_by_user_id_page(
                user_id=self.test_user_id,
                page=1,
                size=5
            )

            # 3. 断言
            self.assertEqual(len(page_1), 5)  # 第一页应该 5 条

            # 4. 测试第2页
            page_2 = self.comment_service.get_comments_by_user_id_page(
                user_id=self.test_user_id,
                page=2,
                size=5
            )
            self.assertEqual(len(page_2), 5)

            # 5. 测试第3页（只剩2条）
            page_3 = self.comment_service.get_comments_by_user_id_page(
                user_id=self.test_user_id,
                page=3,
                size=5
            )
            self.assertEqual(len(page_3), 2)

    def test_like_comment(self):
        # 1. 先插入一条测试评论
        comment = Comment(
            articleId="test_article_001",
            content="测试点赞",
            userId=self.test_user_id,
            nickname="测试用户",
            likeNum=0
        )
        comment_id = self.comment_service.add_comment(comment)
        original_comment = self.comment_service.get_comment_by_id(comment_id)
        print("原始评论：", original_comment.to_dict())

        # 2. 调用点赞（likeNum +1）
        success = self.comment_service.like_comment(comment_id)
        self.assertEqual(success, True)

        # 3. 查询回来，验证 likeNum 变成 1
        updated_comment = self.comment_service.get_comment_by_id(comment_id)
        print("点赞后的评论：", updated_comment.to_dict())
        self.assertEqual(updated_comment.likeNum, 1)

        # 4. 再点一次 → 变成 2
        self.comment_service.like_comment(comment_id)
        updated_comment = self.comment_service.get_comment_by_id(comment_id)
        print("点赞后的评论：", updated_comment.to_dict())
        self.assertEqual(updated_comment.likeNum, 2)

# ========== 测试运行入口（可指定单个/全部测试）==========
if __name__ == "__main__":
    # 缩进4个空格，紧跟执行代码
    suite = unittest.TestSuite()
    suite.addTest(TestCommentService("test_like_comment"))
    unittest.TextTestRunner(verbosity=2).run(suite)

