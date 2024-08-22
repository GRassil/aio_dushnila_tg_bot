from typing import Any, List

from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from .models import (
    Role,
    Profession,
    User,
    Subject,
    Theory,
    Exercise,
    Homework1part,
    UserHomework1part,
    Homework2part,
    UserHomework2part,
    Test,
    UserTestResult,
)


############### Работа с уроками ###############


async def orm_create_subjects(session: AsyncSession):
    query = select(Subject)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all(
        [
            Subject(name="Информатика", num_of_questions=27),
            Subject(name="Проф. Математика", num_of_questions=19),
            Subject(name="Обществознание", num_of_questions=25),
        ]
    )
    await session.commit()


async def orm_get_subjects(session: AsyncSession):
    query = select(Subject)
    result = await session.execute(query)
    return result.scalars().all()


############################ Роли ######################################


async def orm_create_roles(session: AsyncSession):
    query = select(Role)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all([Role("user"), Role("admin"), Role("student")])
    await session.commit()


async def orm_get_roles(session: AsyncSession):
    query = select(Role)
    result = await session.execute(query)
    return result.scalars().all()


############################ Профессии ######################################


async def orm_create_professions(session: AsyncSession):
    query = select(Profession)
    result = await session.execute(query)
    if result.first():
        return
    session.add_all(
        [Profession("Ученик"), Profession("Родитель"), Profession("Учитель")]
    )
    await session.commit()


async def orm_get_professions(session: AsyncSession):
    query = select(Profession)
    result = await session.execute(query)
    return result.scalars().all()


############ User #########
async def orm_add_user(
    session: AsyncSession,
    user_id: int,
    username: str,
    fullname: str,
    role_id: int,
    profession_id: int,
    subjects_ids: str,
):
    obj = User(user_id, username, fullname, role_id, profession_id, subjects_ids)
    print(obj, session)
    session.add(obj)
    await session.commit()


"""
############ Админка: добавить/изменить/удалить товар ########################


async def orm_add_product(session: AsyncSession, data: dict):
    obj = Product(
        name=data["name"],
        description=data["description"],
        price=float(data["price"]),
        image=data["image"],
        category_id=int(data["category"]),
    )
    session.add(obj)
    await session.commit()


async def orm_get_products(session: AsyncSession, category_id):
    query = select(Product).where(Product.category_id == int(category_id))
    result = await session.execute(query)
    return result.scalars().all()


async def orm_get_product(session: AsyncSession, product_id: int):
    query = select(Product).where(Product.id == product_id)
    result = await session.execute(query)
    return result.scalar()


async def orm_update_product(session: AsyncSession, product_id: int, data):
    query = (
        update(Product)
        .where(Product.id == product_id)
        .values(
            name=data["name"],
            description=data["description"],
            price=float(data["price"]),
            image=data["image"],
            category_id=int(data["category"]),
        )
    )
    await session.execute(query)
    await session.commit()


async def orm_delete_product(session: AsyncSession, product_id: int):
    query = delete(Product).where(Product.id == product_id)
    await session.execute(query)
    await session.commit()


##################### Добавляем юзера в БД #####################################


async def orm_add_user(
    session: AsyncSession,
    user_id: int,
    first_name: str | None = None,
    last_name: str | None = None,
    phone: str | None = None,
):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    if result.first() is None:
        session.add(
            User(
                user_id=user_id, first_name=first_name, last_name=last_name, phone=phone
            )
        )
        await session.commit()


######################## Работа с корзинами #######################################


async def orm_add_to_cart(session: AsyncSession, user_id: int, product_id: int):
    query = select(Cart).where(Cart.user_id == user_id, Cart.product_id == product_id)
    cart = await session.execute(query)
    cart = cart.scalar()
    if cart:
        cart.quantity += 1
        await session.commit()
        return cart
    else:
        session.add(Cart(user_id=user_id, product_id=product_id, quantity=1))
        await session.commit()


async def orm_get_user_carts(session: AsyncSession, user_id):
    query = (
        select(Cart).filter(Cart.user_id == user_id).options(joinedload(Cart.product))
    )
    result = await session.execute(query)
    return result.scalars().all()


async def orm_delete_from_cart(session: AsyncSession, user_id: int, product_id: int):
    query = delete(Cart).where(Cart.user_id == user_id, Cart.product_id == product_id)
    await session.execute(query)
    await session.commit()


async def orm_reduce_product_in_cart(
    session: AsyncSession, user_id: int, product_id: int
):
    query = select(Cart).where(Cart.user_id == user_id, Cart.product_id == product_id)
    cart = await session.execute(query)
    cart = cart.scalar()

    if not cart:
        return
    if cart.quantity > 1:
        cart.quantity -= 1
        await session.commit()
        return True
    else:
        await orm_delete_from_cart(session, user_id, product_id)
        await session.commit()
        return False
"""
