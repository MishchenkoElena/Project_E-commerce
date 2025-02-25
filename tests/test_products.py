from unittest.mock import patch

from src.products import Product


def test_product_init(product: Product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(category1, category2, category3):
    assert category1.name == "Смартфоны"
    assert (
        category2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category1.products_in_list) == 3
    assert category1.category_count == 3
    assert category2.category_count == 3
    assert category3.category_count == 3
    assert len(category3.products) == 0


def test_add_new_product():
    products_list = []
    new_product_data = {
        "name": "Samsung Galaxy S24 Ultra",
        "description": "512GB, Серый цвет, 200MP камера",
        "price": 250000.0,
        "quantity": 10,
    }
    product = Product.new_product(new_product_data, products_list)
    assert product.name == "Samsung Galaxy S24 Ultra"
    assert product.description == "512GB, Серый цвет, 200MP камера"
    assert product.price == 250000.0
    assert product.quantity == 10


def test_product_price_incorrect(capsys, product: Product):
    product.price = -500
    captured = capsys.readouterr()
    with patch("builtins.print"):
        assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
        assert product.price
    product.price = 0
    with patch("builtins.print"):
        assert captured.out == "Цена не должна быть нулевая или отрицательная\n"
        assert product.price


def test_product_price_setter_yes(capsys, product: Product):
    new_price = 100000.0
    with patch("builtins.input", side_effect=["y"]):
        product.price = new_price
        captured = capsys.readouterr()
        assert captured.out == ""
        assert product.price == 100000.0
