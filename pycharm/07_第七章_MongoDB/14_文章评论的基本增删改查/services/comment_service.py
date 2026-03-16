from bson.objectid import ObjectId
from config.mongo_config import MongoConfig
from models.comment import Comment

class CommentService:
    """评论服务类，负责评论的增删改查业务逻辑"""
    def __init__(self):
        """初始化集合（依赖注入风格），增加异常捕获"""
        try:
            # 确保获取集合成功，否则直接抛出异常并提示
            self.collection = MongoConfig.get_collection()
            print("✅ MongoDB集合获取成功，CommentService初始化完成")
        except Exception as e:
            raise Exception(f"❌ CommentService初始化失败：获取MongoDB集合出错，{str(e)}") from e
    # ==========新增Create==========
    def add_comment(self,comment:Comment) ->str:
        """新增评论
        :param comment: 评论实体
        :return: 新增评论的ID(字符串格式)
        """
        comment_dict = comment.to_dict()  # 实体转Document
        result = self.collection.insert_one(comment_dict)  # 插入文档
        return str(result.inserted_id)  # 返回新增评论的ID(字符串格式)
    
    # ==========查询Retrieve==========
    def  get_comment_by_id(self,comment_id:str) -> Comment | None:
        """根据评论ID查询评论
        :param comment_id: 评论ID
        :return: 评论实体，如果未找到则返回None
        """
        try:
            data = self.collection.find_one({'_id': ObjectId(comment_id)})  # 根据ID查询文档
            return Comment.from_dict(data) if data else None  # Document转实体
        except (ValueError, TypeError):
            raise None
        
    def  get_comments_by_user_id(self,user_id:str) -> list[Comment]:
        """
        根据用户ID查询评论列表
        :param user_id: 用户ID
        :return: 评论列表
        """
        data_list = self.collection.find({"userId": user_id})  # 根据用户ID查询文档列表
        return [Comment.from_dict(data) for data in data_list]  # Document转实体列表
    
    # ==========更新Update==========
    def update_comment_nickname(self,comment_id:str,new_nickname:str) ->bool:
        """
        更新评论昵称
        :param comment_id:评论ID
        :param new_nickname:新的昵称
        :return: 更新是否成功
        """
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(comment_id)},  # 根据ID查询文档
                {'$set': {'nickname': new_nickname}}  # 更新昵称字段
            )
            return result.modified_count > 0
        except (ValueError, TypeError):
            raise False
        
    # ==========删除Delete==========
    def delete_comment_by_id(self,comment_id:str) ->bool:
        """
        根据评论ID删除评论
        :param comment_id: 评论ID
        :return: 删除是否成功
        """
        try:
            result = self.collection.delete_one({'_id': ObjectId(comment_id)})  # 根据ID删除文档
            return result.deleted_count > 0
        except (ValueError, TypeError):
            raise False
        
    def get_comments_by_user_id_page(self,user_id:str,page:int =1,size:int =10) ->list[Comment]:    
        """
        根据用户ID分页查询评论列表
            :param user_id: 用户ID
            :param page: 页码
            :param size: 每页大小
            :return: 评论列表
        """
        skip = (page - 1) * size  # 计算跳过的文档数量
        data_list = self.collection.find({"userId": user_id}).skip(skip).limit(size)  # 分页查询文档列表
        return [Comment.from_dict(data) for data in data_list]  # Document转实体列表
    
    def like_comment(self,comment_id:str) ->bool:
        """
        点赞评论
        :param comment_id: 评论ID
        :return: 点赞是否成功
        """
        try:
            result = self.collection.update_one(
                {'_id': ObjectId(comment_id)},  # 根据ID查询文档
                {'$inc': {'likeNum': 1}}  # likeNum字段自增1
            )
            return result.modified_count > 0
        except (ValueError, TypeError):
            return False