from dataclasses import dataclass

@dataclass
class ProductItem():
    title: str
    price: str
    currency: str
    images: list[str]
    properties: dict[str, any]
    source: str
    source_id: str
