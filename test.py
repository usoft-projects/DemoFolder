import requests

# JSON verilerini yükleyin
data = {
  "Configurations": [
    "Breakfast",
    "Appetizers",
    "Salads",
    "Sandwiches",
    "Pasta",
    "Pizzas",
    "Burgers",
    "Desserts",
    "Beverages"
  ],
  "Breakfast": [
    {
      "details": "Full Breakfast",
      "image": "serpme-kahvalti.jpg",
      "name": "Serpme Kahvaltı",
      "price": 40
    },
    {
      "details": "Omelette",
      "image": "omlet.jpg",
      "name": "Omlet",
      "price": 20
    },
    {
      "details": "Pastry & Simit",
      "image": "acma-simit.jpg",
      "name": "Açma & Simit",
      "price": 15
    },
    {
      "details": "Menemen",
      "image": "menemen.jpg",
      "name": "Menemen",
      "price": 25
    }
  ],
  "Appetizers": [
    {
      "details": "Cigar Borek",
      "image": "sigara-boregi.jpg",
      "name": "Sigara Böreği",
      "price": 18
    },
    {
      "details": "Crispy Calamari",
      "image": "citr-kalamar.jpg",
      "name": "Çıtır Kalamar",
      "price": 22
    },
    {
      "details": "Mini Hamburger",
      "image": "mini-hamburger.jpg",
      "name": "Mini Hamburger",
      "price": 20
    }
  ],
  "Salads": [
    {
      "details": "Seasonal Salad",
      "image": "mevsim-salata.jpg",
      "name": "Mevsim Salata",
      "price": 18
    },
    {
      "details": "Caesar Salad",
      "image": "caesar-salata.jpg",
      "name": "Caesar Salata",
      "price": 22
    },
    {
      "details": "Mango Avocado Salad",
      "image": "mango-avokado-salata.jpg",
      "name": "Mango Avokado Salata",
      "price": 24
    }
  ],
  "Sandwiches": [
    {
      "details": "Chicken Sandwich",
      "image": "tavuklu-sandvic.jpg",
      "name": "Tavuklu Sandviç",
      "price": 20
    },
    {
      "details": "Vegetarian Sandwich",
      "image": "veggie-sandvic.jpg",
      "name": "Veggie Sandviç",
      "price": 18
    },
    {
      "details": "Fish Sandwich",
      "image": "balik-sandvic.jpg",
      "name": "Balık Sandviç",
      "price": 24
    }
  ],
  "Pasta": [
    {
      "details": "Fettuccine Alfredo",
      "image": "fettuccine-alfredo.jpg",
      "name": "Fettuccine Alfredo",
      "price": 28
    },
    {
      "details": "Penne Arrabbiata",
      "image": "penne-arrabbiata.jpg",
      "name": "Penne Arrabbiata",
      "price": 26
    }
  ],
  "Pizzas": [
    {
      "details": "Margherita Pizza",
      "image": "margherita-pizza.jpg",
      "name": "Margherita Pizza",
      "price": 30
    },
    {
      "details": "Vegetarian Pizza",
      "image": "vejeteryan-pizza.jpg",
      "name": "Vejeteryan Pizza",
      "price": 32
    },
    {
      "details": "Mixed Seafood Pizza",
      "image": "karisik-deniz-urunleri-pizza.jpg",
      "name": "Karışık Deniz Ürünleri Pizza",
      "price": 35
    }
  ],
  "Burgers": [
    {
      "details": "Classic Burger",
      "image": "klasik-burger.jpg",
      "name": "Klasik Burger",
      "price": 25
    },
    {
      "details": "Spicy Sauce Burger",
      "image": "aci-soslu-burger.jpg",
      "name": "Acı Soslu Burger",
      "price": 28
    },
    {
      "details": "Mushroom Burger",
      "image": "mantarli-burger.jpg",
      "name": "Mantarlı Burger",
      "price": 27
    }
  ],
  "Desserts": [
    {
      "details": "Cheesecake",
      "image": "cheesecake.jpg",
      "name": "Cheesecake",
      "price": 18
    },
    {
      "details": "Chocolate Brownie",
      "image": "cikolatali-brownie.jpg",
      "name": "Çikolatalı Brownie",
      "price": 20
    },
    {
      "details": "Fruit Plate",
      "image": "meyve-tabagi.jpg",
      "name": "Meyve Tabağı",
      "price": 16
    }
  ],
  "Beverages": [
    {
      "details": "Fruit Juice (350ml)",
      "image": "meyve-suyu.jpg",
      "name": "Meyve Suyu (350ml)",
      "price": 10
    },
    {
      "details": "Soda (250ml)",
      "image": "soda.jpg",
      "name": "Soda (250ml)",
      "price": 8
    },
    {
      "details": "Cappuccino",
      "image": "cappuccino.jpg",
      "name": "Cappuccino",
      "price": 15
    }
  ]
}

# Unsplash API anahtarınızı ve URL'sini buraya ekleyin
UNSPLASH_API_KEY = "111812491413a8045327ce7d8f9bdd0511c4aedfa3571b8b5133f65c79789703"
UNSPLASH_API_URL = "https://api.unsplash.com/search/photos"

# Her yemek öğesi için Unsplash API'den resimleri alın ve verilere ekleyin
for category, items in data.items():
    if category != "Configurations":
        for item in items:
            details = item["details"]
            query = f"{details} food"
            headers = {"Authorization": f"Client-ID {UNSPLASH_API_KEY}"}
            params = {"query": query, "per_page": 1}
            response = requests.get(UNSPLASH_API_URL, headers=headers, params=params)
            if response.status_code == 200:
                result = response.json()
                if result["results"]:
                    item["image"] = result["results"][0]["urls"]["regular"]
                else:
                    item["image"] = "Image not found"
            else:
                item["image"] = "Image not found"

# Sonuçları görüntüle
print(data)
