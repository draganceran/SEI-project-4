from pony.orm import db_session
from app import db
from models.Farm import Farm, Comment
from models.Product import Product
from models.User import User, UserSchema


db.drop_all_tables(with_all_data=True)
db.create_tables()

with db_session():
    schema = UserSchema()
    dragan = User(
        username='DRAGAN',
        email='dragan@dragan.com',
        password_hash=schema.generate_hash('pass')
    )
    fruit = Product(name='Fruit')
    vine = Product(name='Vine')
    honey = Product(name='Honey')
    meat = Product(name='Meat')
    fish = Product(name='Fish')
    dairy = Product(name='Dairy')
    vegetables = Product(name='Vegetables')
    eggs = Product(name='Eggs')
    destilery = Product(name='Destilery')
    brewery = Product(name='Brewery')



    my_farm = Farm(
        name='Happy Farm',
        country='UK',
        region='Kent',
        address='Maidstone Rd, Paddock Wood, Tonbridge TN12 6PY',
        products=[brewery, fish],
        image='https://thehopfarm.co.uk/uploads/_contentImage/childshetland.jpg',
        accommodation=True,
        dissable_acces=False,
        user=dragan,
        description='The Hop Farm Family Park is a 400-acre Country Park in Beltring, near East Peckham in Kent, England, is over 450 years old, and has the largest collection of oast houses in the world.',
        long=0.39528,
        lat=51.19721,






    )
    Comment(content='nice farm for detox ', user=dragan, farm=my_farm)

    db.commit()
