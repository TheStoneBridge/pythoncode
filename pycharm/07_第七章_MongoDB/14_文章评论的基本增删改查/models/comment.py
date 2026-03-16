from dataclasses import dataclass
from datetime import datetime
from bson import ObjectId

@dataclass
class Comment:
    """评论实体类"""
    articleId :str
    content :str
    userId :str
    nickname :str
    state: str='1'
    likeNum :int=0
    replyNum :int=0
    createTime :datetime=datetime.now()
    id : ObjectId | None = None # ObjectId是MongoDB的默认主键类型

    def to_dict(self) -> dict:
        """转换为MongoDB可存储的字典(实体转Document)"""
        data = {
            'articleId': self.articleId,
            'content': self.content,
            'userId': self.userId,
            'nickname': self.nickname,
            'state': self.state,
            'likeNum': self.likeNum,
            'replyNum': self.replyNum,
            'createTime': self.createTime,
        }
        #新增时id为None，不存储到MongoDB；更新时id不为None，存储到MongoDB
        if self.id is not None:
            data['_id'] = self.id
        return data

    @staticmethod
    def from_dict(data: dict) -> 'Comment':
        """从MongoDB文档转换为实体( Document转实体)"""
        return Comment(
            articleId=data.get('articleId', ''),
            content=data.get('content', ''),
            userId=data.get('userId', ''),
            nickname=data.get('nickname', ''),
            state=data.get('state', '1'),
            likeNum=data.get('likeNum', 0),
            replyNum=data.get('replyNum', 0),
            createTime=data.get('createTime', datetime.now()),
            id=data.get('_id')  # MongoDB的主键字段是_id
        )    