from sqlalchemy import create_engine, text

connection_string = "sqlite:///db.sqlite3"

engine = create_engine(connection_string)


def select_all():
    with engine.connect() as connection:
        query = "SELECT * FROM mainapp_accommodation WHERE is_active = true"
        cursor = connection.execute(text(query))
        data = cursor.fetchall()
        result = [row._asdict() for row in data]
        return result


# print(select_all())


def select_by_id(**kwargs):
    with engine.connect() as connection:
        query = "SELECT * FROM mainapp_accommodation WHERE id = :id"
        cursor = connection.execute(text(query), parameters=kwargs)
        data = cursor.fetchone()
        if data is not None:
            data = data._asdict()
            return data


# print(select_by_id(id=1))

def create_new(**kwargs):
    with engine.connect() as connection:
        query = "INSERT INTO mainapp_accommodation (" \
                "id, name, image, short_desc, " \
                "description, availability, price, " \
                "room_desc, is_active, country_id, region_id) VALUES " \
                "(:id, :name, :image, :short_desc," \
                ":description, :availability, :price," \
                ":room_desc, :is_active, :country_id, :region_id)"

        connection.execute(text(query), parameters=kwargs)
        connection.commit()


# create_new(id=11, name='санаторий парус 2', image='accommodation_img/parus_80MrPZw.jpg',
#            short_desc='анапский санаторий с романтичным названием «Парус', description='большое описание',
#            availability=20, price=2000, room_desc='описание номера', is_active=1, country_id=1, region_id=1)


def update_by_id(**kwargs):
    with engine.connect() as connection:
        query = "UPDATE mainapp_accommodation SET name = :name WHERE id = :id"

        connection.execute(text(query), parameters=kwargs)
        connection.commit()


# update_by_id(name='санаторий парус 3', id=11)


def delete_by_id(**kwargs):
    with engine.connect() as connection:
        query = "DELETE FROM mainapp_accommodation WHERE id = :id"

        connection.execute(text(query), parameters=kwargs)
        connection.commit()

# delete_by_id(name='санаторий парус 3', id=11)
