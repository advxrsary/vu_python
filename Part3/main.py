from sqlalchemy import create_engine, func, select, Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import declarative_base, relationship, Session

# For colored output
CGREEN = '\33[32m'
CEND = '\33[0m'

# ------------------------------------------------------ Task 1 --------------------------------------------------------

# Construct a new base class for declarative class definitions
Base = declarative_base()


# Declare new mapped classes as subclasses of the base
class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    address = Column(String(100))

    # Establish a collection of Item objects on Shop called Shop.items
    # Establish a .shop attribute on Item which will refer to the parent Shop object
    items = relationship('Item', backref='shop')

    def __repr__(self):
        return f'<Shop(name="{self.name}", address="{self.address}")>'


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer, primary_key=True)
    barcode = Column(String(32), unique=True)
    name = Column(String(40), nullable=False)
    description = Column(String(200), default='')
    unit_price = Column(Numeric(10, 2), nullable=False, default=1.00)
    created_at = Column(DateTime, server_default=func.now())

    shop_id = Column(Integer, ForeignKey('shops.id'))

    # Establish a collection of Component objects on Item called Item.components
    # Establish a .item attribute on Component which will refer to the parent Item object
    components = relationship('Component', backref='item')

    def __repr__(self):
        return (
            f'<Item(barcode="{self.barcode}", name="{self.name}", description="{self.description}", '
            f'unit_price="{self.unit_price}", created_at="{self.created_at}")>'
        )


class Component(Base):
    __tablename__ = 'components'

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    quantity = Column(Numeric(10, 2), default=1.00)

    item_id = Column(Integer, ForeignKey('items.id'))

    def __repr__(self):
        return f'<Component(name="{self.name}", quantity="{self.quantity}")>'


# Create a new Engine instance for working with an in-memory SQLite database
# The sqlite :memory: identifier is the default if no filepath is present
# Specify echo=True so that the Engine will log all statements
# future=True is to ensure we are using the latest SQLAlchemy 2.0-style APIs
engine = create_engine('sqlite://', echo=True, future=True)

# Generate our schema in our target SQLite database
Base.metadata.create_all(engine)

# ------------------------------------------------------ Task 2 --------------------------------------------------------

# Create session and add objects
# Use the session in a Python context manager so that it is automatically closed at the end of the block
with Session(engine) as session:

    # noinspection PyTypeChecker
    # Needed to add this comment to suppress the false 'Incorrect type' IDE warning
    session.add_all([
        Shop(
            name='IKI',
            address='Kaunas, Iki street 1',
            items=[
                Item(
                    barcode='112233112233',
                    name='Žemaičių bread',
                    unit_price=1.55,
                    components=[
                        Component(
                            name='Flour',
                            quantity=1.50,
                        ),
                        Component(
                            name='Water',
                            quantity=1.00,
                        ),
                    ],
                ),
                Item(
                    barcode='33333222111',
                    name='Klaipeda milk',
                    description='Milk from Klaipeda',
                    unit_price=2.69,
                    components=[
                        Component(
                            name='Milk',
                            quantity=1.00,
                        ),
                    ],
                ),
            ],
        ),
        Shop(
            name='MAXIMA',
            address='Kaunas, Maksima street 2',
            items=[
                Item(
                    barcode='99898989898',
                    name='Aukštaičių bread',
                    unit_price=1.65,
                    components=[
                        Component(
                            name='Flour',
                            quantity=1.60,
                        ),
                        Component(
                            name='Water',
                            quantity=1.10,
                        ),
                    ],
                ),
                Item(
                    barcode='99919191991',
                    description='Milk from Vilnius',
                    name='Vilnius milk',
                    unit_price=2.99,
                    components=[
                        Component(
                            name='Milk',
                            quantity=1.10,
                        ),
                    ],
                ),
            ],
        ),
    ])

    session.commit()

# ------------------------------------------------------ Task 3 --------------------------------------------------------

# Create a clean session
with Session(engine) as session:

    stmt = (
        select(Component)
        .join(Component.item)
        .join(Item.shop)
        .where(Shop.name == 'IKI')
        .where(Item.name == 'Žemaičių bread')
        .where(Component.name == 'Water')
    )
    iki_bread_water = session.scalar(stmt)
    iki_bread_water.quantity = 1.45

    stmt = (
        select(Component)
        .join(Component.item)
        .join(Item.shop)
        .where(Shop.name == 'MAXIMA')
        .where(Item.name == 'Vilnius milk')
        .where(Component.name == 'Milk')
    )
    maxima_milk_milk = session.scalar(stmt)
    session.delete(maxima_milk_milk)

    session.commit()

# ------------------------------------------------------ Task 4 --------------------------------------------------------

with Session(engine) as session:

    stmt1 = select(Shop)
    for shop in session.scalars(stmt1):
        print(f'{CGREEN}{shop}{CEND}')
        stmt2 = (
            select(Item)
            .join(Item.shop)
            .where(Shop.name == shop.name)
        )
        for item in session.scalars(stmt2):
            print(f'    {CGREEN}{item}{CEND}')
            stmt3 = (
                select(Component)
                .join(Component.item)
                .join(Item.shop)
                .where(Shop.name == shop.name)
                .where(Item.name == item.name)
            )
            for component in session.scalars(stmt3):
                print(f'        {CGREEN}{component}{CEND}')

# ------------------------------------------------------ Task 5 --------------------------------------------------------

with Session(engine) as session:

    # Select items that have related components
    stmt = (
        select(Item)
        .where(Item.components.any())
    )
    for item in session.scalars(stmt):
        print(f'{CGREEN}{item}{CEND}')

    # Select items, which name contains 'ien'
    stmt = (
        select(Item)
        .where(Item.name.contains('ien'))
    )
    for item in session.scalars(stmt):
        print(f'{CGREEN}{item}{CEND}')

    # Count how many components each item consists of
    stmt = select(Item)
    for item in session.scalars(stmt):
        stmt = (
            select(func.count())
            .select_from(Component)
            .where(Component.item_id == item.id)
        )
        count = session.scalar(stmt)
        print(f'{CGREEN}{item}: {count}{CEND}')

    # Calculate the quantity of components for each item
    stmt = select(Item)
    for item in session.scalars(stmt):
        stmt = (
            select(func.sum(Component.quantity))
            .select_from(Component)
            .where(Component.item_id == item.id)
        )
        count = session.scalar(stmt)
        print(f'{CGREEN}{item}: {count}{CEND}')

    # Calculate the total cost of all items presented in each shop
    stmt = select(Shop)
    for shop in session.scalars(stmt):
        stmt = (
            select(func.sum(Item.unit_price))
            .select_from(Item)
            .where(Item.shop_id == shop.id)
        )
        count = session.scalar(stmt)
        print(f'{CGREEN}{shop}: {count}{CEND}')

    # Select the lowest price among all items of all shops
    stmt = select(func.min(Item.unit_price))
    min_price = session.scalar(stmt)
    print(f'{CGREEN}{min_price}{CEND}')
