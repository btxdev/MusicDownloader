from youtubesearchpython import VideosSearch

def search_video(query):
    search = VideosSearch(query, limit = 1)
    if not search is None:
        return search['link']
    else:
        print('video {} not found'.format(query))
        return None
