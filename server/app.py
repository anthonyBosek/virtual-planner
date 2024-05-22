#!/usr/bin/env python3

# Standard library imports

# Local imports
from app_setup import app, db, ma, api

# Model imports
# from models.user import User
# from schemas.user_schema import UserSchema
# from models.community import Community
# from schemas.community_schema import CommunitySchema
# from models.entry import Entry
# from schemas.entry_schema import EntrySchema
# from models.post import Post
# from schemas.post_schema import PostSchema
# from models.todo import Todo
#
# from models.user_community import UserCommunity
# from models.journal import Journal

# Route imports
from routes.check_session import CheckSession
from routes.communities import Communities
from routes.community_by_id import CommunityById
from routes.journal_by_id import JournalById
from routes.journal import Journals
from routes.login import Login
from routes.logout import Logout
from routes.post_by_id import PostById
from routes.posts import Posts
from routes.register import Register
from routes.todo_by_id import TodoById
from routes.todos import Todos
from routes.user_by_id import UserById
from routes.user_communities import UserCommunities
from routes.users import Users

# Schemas


# entry_schema = EntrySchema(session=db.session)
# entries_schema = EntrySchema(many=True, session=db.session)
# post_schema = PostSchema(session=db.session)
# posts_schema = PostSchema(many=True, session=db.session)
# todo_schema = TodoSchema(session=db.session)
# todos_schema = TodoSchema(many=True, session=db.session)

# Add resources
api.add_resource(CheckSession, '/checksession')
api.add_resource(Communities, '/communities')
api.add_resource(CommunityById, '/communities/<int:id>')
api.add_resource(JournalById, '/journals/<int:id>')
api.add_resource(Journals, "/journals")
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
api.add_resource(PostById, '/posts/<int:id>')
api.add_resource(Posts, '/communities/<int:id>/posts')
api.add_resource(Register, '/register')
api.add_resource(TodoById, '/todos/<int:id>')
api.add_resource(Todos, '/todos')
api.add_resource(UserById, '/users/<int:id>')
api.add_resource(UserCommunities, '/usercommunities')
api.add_resource(Users, '/users')
# api.add_resource(Entries, '/journal/<int:id>')


# Views go here!

@app.route('/')
def index():
    return '<h1>Project Server</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
