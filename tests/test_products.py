def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_category_init(category_1, category_2, category_3):
    assert category_1.name == "Смартфоны"
    assert (
        category_2.description
        == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )
    assert len(category_1.products) == 3

    assert category_1.category_count == 3
    assert category_2.category_count == 3
    assert category_3.category_count == 3
    assert len(category_3.products) == 0
