import pickle

dicto = {'api_id':'xxx', 'api_hash':'xxx', 'username':'xxx', 'phone':'+xxx'}

with open('login_conf', 'wb') as f:
    pickle.dump(dicto, f)
    f.close
