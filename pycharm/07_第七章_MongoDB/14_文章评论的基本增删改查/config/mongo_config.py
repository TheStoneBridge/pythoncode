from pymongo import MongoClient
from pymongo.errors import PyMongoError

class MongoConfig:
    """MongoDB的连接配置类
    """
    MONGO_HOST = "localhost"
    MONGO_PORT = 27017
    MONGO_DB = "article"
    MONGO_COLLECTION = "comment"

    @classmethod
    def get_mongo_client(cls):
        """获取MongoDB客户端"""
        try:
            client = MongoClient(
                host=cls.MONGO_HOST,
                port=cls.MONGO_PORT,
                connectTimeoutMS=3000,  # 连接超时3秒
                serverSelectionTimeoutMS=3000)
            #验证连接
            client.admin.command('ping')
            print(f"✅ MongoDB连接成功：{cls.MONGO_HOST}:{cls.MONGO_PORT}")
            return client
        except PyMongoError as e:
            raise PyMongoError(f"❌ MongoDB连接失败：请检查服务是否启动/配置是否正确，{str(e)}") from e
    @classmethod
    def get_collection(cls):
        """获取Comment集合，保证数据库/集合自动创建"""
        try:
            client = cls.get_mongo_client()
            db = client[cls.MONGO_DB]  # 数据库不存在自动创建
            coll = db[cls.MONGO_COLLECTION]  # 集合不存在自动创建
            return coll
        except Exception as e:
            raise Exception(f"❌ 获取集合失败：{str(e)}") from e