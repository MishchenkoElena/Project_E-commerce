def test_product_init(product):
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
    assert len(category1.products) == 3

    assert category1.category_count == 3
    assert category2.category_count == 3
    assert category3.category_count == 3
    assert len(category3.products) == 0
