import requests as r
class Trello:
    Key = '29aace4902c9e1898428eea32bd05973'
    Secret = 'ae9bedb5c85157f9f3e76563b23653e1032ab3d59aa3327ad010862afa73d54d'
    BoardID = '5a3cdf21c93f6243ad714464'
    Home = "https://api.trello.com/1/"

    def __init__(self):
        raise NotImplementedError("Trello requires Token")

    def __init__(self, Token):
        self.Token = Token
        self.Auth = Auth = ",url&key={}&token={}".format(self.Key, Token)

    def get_cards(self, listID = '5ace0a300abdbb6e38672237'):
        query = 'lists/{}/cards?fields=id,name,badges,labels'.format(listID)
        return self.get_response(query).json()

    def get_response(self, query):
        return r.get(self.Home + query + self.Auth)