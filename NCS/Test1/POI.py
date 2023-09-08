class POI:
    def __init__(self):
        self.poi_list = {
            1: "테스트용",
        }

    def login(self, username, password):
        if username == "admin" and password == "admin":
            return "admin"
        elif username == "user01" and password == "password":
            return "user"
        else:
            return None

    def get_poi(self, poi_id):
        return self.poi_list.get(poi_id)

    def add_poi(self, name):
        if name is not None:
            new_id = 2
            return new_id
        else:
            return None

    def edit_poi(self, poi_id, name):
        if poi_id == 1 and name is not None:
            return True
        else:
            return False

    def delete_poi(self, poi_id):
        if poi_id == 1:
            return True
        else:
            return False
