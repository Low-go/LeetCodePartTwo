from dbmanager import DBManager
import json

json_data = '''
[
    {
        "id": 1234567890,
        "title": "A new data",
        "date_created": "2020-01-01",
        "updates": []
    },
    {
        "id": 9876543321,
        "title": "The data strikes back",
        "date_created": "2020-02-04",
        "updates": [
            {
                "date": "2020-02-04",
                "action": "item updated"
            }
        ]
    }
]
'''

if __name__ == '__main__':
    db_manager = DBManager()
    
    db_manager.open_connection()
    
    # Your code here to take json_data
    # and transform it into necessary format for storage
    

    data = json.loads(json_data)


    rows_to_save = []

    for i in data:
        if i["updates"]:

            for j in i["updates"]:

                row = {

                    "id": i["id"],
                    "title": i["title"],
                    "date_created": i["date_created"],
                    "date_updated": j["date"],
                    "update": j["action"]
                }

                rows_to_save.append(row)

            
        else:
            row = {
                "id": '',
                "title": '',
                "date_created": '',
                "date_updated": None,
                "update": None
            }

            rows_to_save.append(row)

            # I know have access to both on this hashmap
            # now to store them 

    db_manager.save_to_database(rows_to_save)

    db_manager.close_connection()