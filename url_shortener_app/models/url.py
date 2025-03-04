from bson.objectid import ObjectId

# Lazy import to prevent circular import issues
def get_mongo():
    from app import mongo
    return mongo

class URL:
    @staticmethod
    def create_url(user_id, long_url, short_url):
        get_mongo().db.urls.insert_one({"user_id": user_id, "long_url": long_url, "short_url": short_url, "favorite": False})

    @staticmethod
    def get_user_urls(user_id):
        return get_mongo().db.urls.find({"user_id": user_id})
    
    @staticmethod
    def get_user_favs(user_id):
        return get_mongo().db.urls.find({"user_id": user_id, "favorite": True}).sort({"long_url":1})
    
    @staticmethod
    def get_fav_status(user_id, short_url):
        result = get_mongo().db.urls.find_one({"user_id": user_id, "short_url": short_url}, {"favorite": 1})
        if result:
            return result["favorite"]
        return None
    
    @staticmethod
    def toggle_favorite(user_id, short_url):
        fav = URL.get_fav_status(user_id, short_url)
        if fav is not None:
            return get_mongo().db.urls.update_one(
                {"user_id": user_id, "short_url": short_url},
                {"$set": {"favorite": not fav}}
            )

    @staticmethod
    def query(query):
        return get_mongo().db.urls.find(query)

    @staticmethod
    def delete_url(short_url):
        get_mongo().db.urls.delete_one({"short_url": short_url})

    @staticmethod
    def update_url(short_url, new_long_url):
        return get_mongo().db.urls.update_one({"short_url": short_url}, {"$set": {"long_url": new_long_url}})

    @staticmethod
    def short_to_long(short_url):
        document = get_mongo().db.urls.find_one({"short_url": short_url})
        if document:
            return (document.get("long_url"))
        return None
