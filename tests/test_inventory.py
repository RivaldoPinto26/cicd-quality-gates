# tests will be added in PR #2 when functions are implemented
import pytest
from src.inventory import Inventory

def test_add_product():
    inv = Inventory()
    inv.add_product("laptop", 10, 1000)
    assert "laptop" in inv.products

def test_duplicate_product():
    inv = Inventory()
    inv.add_product("mouse", 5, 20)
    with pytest.raises(Exception):
        inv.add_product("mouse", 5, 20)


def test_remove_more_than_stock():
    inv = Inventory()
    inv.add_product("monitor", 2, 200)
    with pytest.raises(Exception):
        inv.remove_stock("monitor", 5)
def test_update_stock():
    inv = Inventory()
    inv.add_product("phone", 5, 500)
    inv.update_stock("phone", 5)
    assert inv.products["phone"]["quantity"] == 10


def test_get_low_stock():
    inv = Inventory()
    inv.add_product("usb", 2, 10)
    result = inv.get_low_stock(5)
    assert "usb" in result

def test_total_value():
    inv = Inventory()
    inv.add_product("a", 2, 10)
    inv.add_product("b", 3, 20)
    assert inv.get_total_value() == 80

def test_add_detailed_tech_product():
    inv = Inventory()
    
    # Passamos os 8 parametros exigidos para testar a adicao da Mesa Gaming
    result = inv.add_detailed_tech_product(
        "Mesa Gaming RGB", 5, 250, "Setup Tech", 25, "1.5x0.8", "TechSupplier PT", "SKU-GAMING-001"
    )
    
    assert result is True
    assert "Mesa Gaming RGB" in inv.products
    assert inv.products["Mesa Gaming RGB"]["category"] == "Setup Tech"

def test_apply_discount():
    inv = Inventory()

    inv.add_product("Headset Bluetooth", 10, 100)

    result = inv.apply_discount("Headset Bluetooth", 10)

    # Teste valida o comportamento errado
    assert result == 110