from handlers.base import BaseHandler
from google.appengine.api import mail


class EmailNewCommentWorker(BaseHandler):
    def post(self):
        topic_author_email = self.request.get("topic_author_email")
        topic_title = self.request.get("topic_title")
        topic_id = self.request.get("topic_id")
        comment_author_email = self.request.get("comment_author_email")

        mail.send_mail(sender="turnsek.lucija@gmail.com",
                        to=topic_author_email,
                        subject="New comment on your topic in %s!" % topic_title,
                        body="""Your topic {0} received a new comment.

                       Click <a href="http://your-domain.org/topic/{1}">on this link</a> to see it""".format(topic_title,
                                                                                                             topic_id))
