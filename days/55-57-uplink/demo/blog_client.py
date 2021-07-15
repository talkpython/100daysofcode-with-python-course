import datetime

import requests
import uplink

from uplink_helpers import raise_for_status


@uplink.json
@raise_for_status
class BlogClient(uplink.Consumer):

    def __init__(self):
        # Updating this to the latest SSL based version
        # Should have redirected in code but not in many browsers oddly
        # Hopefully it's just clearer having it here like this.
        super().__init__(base_url='https://consumerservicesapi.talkpython.fm/')

    @uplink.get('/api/blog')
    def all_entries(self) -> requests.models.Response:
        """ Gets all blog entries from the server. """

    @uplink.get('/api/blog/{post_id}')
    def entry_by_id(self, post_id) -> requests.models.Response:
        """ Get single blog post details. """

    def create_new_entry(self, title: str, content: str,
                         views: int = 0, published: str = None) -> requests.models.Response:
        if published is None:
            published = datetime.datetime.now().isoformat()

        # noinspection PyTypeChecker
        resp = self.internal_create_new_entry(title=title, content=content, view_count=views, published=published)
        return resp

    # Note: For some reason, the name of this method was freaking out the latest version of
    # uplink. So we just named it internal_. That's why it's different from the video.
    @uplink.post('/api/blog')
    def internal_create_new_entry(self, **kwargs: uplink.Body) -> requests.models.Response:
        """ Creates a new post. """
