"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Part 2: Write queries


# Get the brand with the **id** of 8.
brand_with_id_8 = Brand.query.get(8)

# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
models_chevrolet_corvette = Model.query.filter_by(name="Corvette", brand_name="Chevrolet").all()

# Get all models that are older than 1960.
models_older_than_1960 = Model.query.filter(Model.year < 1960).all()

# Get all brands that were founded after 1920.
brands_after_1920 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
Models_with_cor = Model.query.filter(Model.name.like('Cor%')).all()

# Get all brands that were founded in 1903 and that are not yet discontinued.
Brands_founded_1903 = Brand.query.filter(Brand.founded == '1903', Brand.discontinued.is_(None)).all()

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
brands_disc_or_founded_before_1950 = Brand.query.filter((Brand.discontinued.isnot(None))|(Brand.founded < 1950)).all()

# Get all models whose brand_name is not Chevrolet.
models_chevrolet = Model.query.filter(Model.brand_name != 'Chevrolet').all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''

    model_info = db.session.query(Model.name, Model.brand_name,
                                  Brand.headquarters).join(Brand).filter(Model.year == year).all()

    for model_name, brand_name, brand_headquarters in model_info:
        print model_name, '-', brand_name, '-', brand_headquarters, "\n"

    return

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
     using only ONE database query.'''

    brands_summary = db.session.query(Model.brand_name,
                                      Model.name).order_by(Model.brand_name).all()
    for brand_name, model_name in brands_summary:
        print brand_name, model_name, '\t'

    return

# -------------------------------------------------------------------
# Part 2.5: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of
# ``Brand.query.filter_by(name='Ford')``?

# answer:
# Returned value is <flask_sqlalchemy.BaseQuery object at 0x7fb48c8e90d0>
# It's a query object, but we need to fetch data with .all(), .first(), .one()
# to get a Brand object with the name Ford

# 2. In your own words, what is an association table, and what *type* of
# relationship does an association table manage?

#answer:
#An association table is a table that connects/associates two other tables that
#have a many to many relationship. For example, from our exercises, Rating table
#was an assosiation table to the tables Movies and Users.

# -------------------------------------------------------------------
# Part 3

def search_brands_by_name(mystr):
    return Brand.query.filter(Brand.name.contains(mystr)).all()


def get_models_between(start_year, end_year):
    return Model.query.filter(Model.year >= start_year, Model.year <= end_year).all()
