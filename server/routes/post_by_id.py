from . import request, Resource
from models.post import Post
from schemas.post_schema import PostSchema
from models.user_community import UserCommunity
from schemas.user_schema import UserSchema  #!
from app_setup import db

# patch method to update an existing post within a community
# delete method to delete an existing post within a community

post_schema = PostSchema(session=db.session)
posts_schema = PostSchema(many=True, session=db.session)
user_schema = UserSchema(session=db.session)  #!


class PostById(Resource):
    def get(self, id):
        if post := db.session.get(Post, id):
            post_schema = PostSchema()
            return {
                "post": post_schema.dump(post),
                "user": user_schema.dump(post.user),
            }, 200
        return {"error": "Post not found"}, 404

    def patch(self, id):
        if post := db.session.get(Post, id):
            try:
                data = request.json
                # Validate data
                post_schema.validate(data)
                # Deserialize data and allow for partial updates
                updated_post = post_schema.load(data, instance=post, partial=True)
                db.session.commit()
                # Serialize the data and package your JSON response
                return post_schema.dump(updated_post), 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Could not find post"}, 404

    def delete(self, id):
        if post := db.session.get(Post, id):
            try:
                db.session.delete(post)
                db.session.commit()
                return {"message": f"Post {id} has been deleted"}, 200
            except Exception as e:
                db.session.rollback()
                return {"error": str(e)}, 400
        return {"error": "Could not find post"}, 404
