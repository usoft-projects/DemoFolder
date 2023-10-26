import json
import requests

# JSON verisi
data = {
  "1Configurations": [
    "Kahvaltı",
    "Ara Sıcaklar",
    "Salatalar",
    "Sandviçler",
    "Makarnalar",
    "Pizzalar",
    "Burgerler",
    "Tatlılar",
    "İçecekler"
  ],
  "Kahvaltı": [
    {
      "details": "Serpme Kahvaltı",
      "image": "serpme-kahvalti.jpg",
      "name": "Serpme Kahvaltı",
      "price": 40
    },
    {
      "details": "Omlet",
      "image": "omlet.jpg",
      "name": "Omlet",
      "price": 20
    },
    {
      "details": "Açma & Simit",
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
  "Ara Sıcaklar": [
    {
      "details": "Sigara Böreği",
      "image": "sigara-boregi.jpg",
      "name": "Sigara Böreği",
      "price": 18
    },
    {
      "details": "Çıtır Kalamar",
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
  "Salatalar": [
    {
      "details": "Mevsim Salata",
      "image": "mevsim-salata.jpg",
      "name": "Mevsim Salata",
      "price": 18
    },
    {
      "details": "Caesar Salata",
      "image": "caesar-salata.jpg",
      "name": "Caesar Salata",
      "price": 22
    },
    {
      "details": "Mango Avokado Salata",
      "image": "mango-avokado-salata.jpg",
      "name": "Mango Avokado Salata",
      "price": 24
    }
  ],
  "Sandviçler": [
    {
      "details": "Tavuklu Sandviç",
      "image": "tavuklu-sandvic.jpg",
      "name": "Tavuklu Sandviç",
      "price": 20
    },
    {
      "details": "Veggie Sandviç",
      "image": "veggie-sandvic.jpg",
      "name": "Veggie Sandviç",
      "price": 18
    },
    {
      "details": "Balık Sandviç",
      "image": "balik-sandvic.jpg",
      "name": "Balık Sandviç",
      "price": 24
    }
  ],
  "Makarnalar": [
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
  "Pizzalar": [
    {
      "details": "Margherita Pizza",
      "image": "margherita-pizza.jpg",
      "name": "Margherita Pizza",
      "price": 30
    },
    {
      "details": "Vejeteryan Pizza",
      "image": "vejeteryan-pizza.jpg",
      "name": "Vejeteryan Pizza",
      "price": 32
    },
    {
      "details": "Karışık Deniz Ürünleri Pizza",
      "image": "karisik-deniz-urunleri-pizza.jpg",
      "name": "Karışık Deniz Ürünleri Pizza",
      "price": 35
    }
  ],
  "Burgerler": [
    {
      "details": "Klasik Burger",
      "image": "klasik-burger.jpg",
      "name": "Klasik Burger",
      "price": 25
    },
    {
      "details": "Acı Soslu Burger",
      "image": "aci-soslu-burger.jpg",
      "name": "Acı Soslu Burger",
      "price": 28
    },
    {
      "details": "Mantarlı Burger",
      "image": "mantarli-burger.jpg",
      "name": "Mantarlı Burger",
      "price": 27
    }
  ],
  "Tatlılar": [
    {
      "details": "Cheesecake",
      "image": "cheesecake.jpg",
      "name": "Cheesecake",
      "price": 18
    },
    {
      "details": "Çikolatalı Brownie",
      "image": "cikolatali-brownie.jpg",
      "name": "Çikolatalı Brownie",
      "price": 20
    },
    {
      "details": "Meyve Tabağı",
      "image": "meyve-tabagi.jpg",
      "name": "Meyve Tabağı",
      "price": 16
    }
  ],
  "İçecekler": [
    {
      "details": "Meyve Suyu (350ml)",
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


# Unsplash API anahtarınızı buraya ekleyin
UNSPLASH_API_KEY = "111812491413a8045327ce7d8f9bdd0511c4aedfa3571b8b5133f65c79789703"

# JSON verisini dolaşarak görsel URL'leri ekleyin
for category in data:
    if category != "1Configurations":
        for dish in data[category]:
            # Yemek adını al
            dish_name = dish["name"]
            # Unsplash API'sini kullanarak görsel URL'si al
            unsplash_url = f"https://api.unsplash.com/search/photos/?query={dish_name} food&client_id={UNSPLASH_API_KEY}"
            response = requests.get(unsplash_url)
            if response.status_code == 200:
                unsplash_data = response.json()
                if len(unsplash_data["results"]) > 0:
                    image_url = unsplash_data["results"][0]["urls"]["regular"]
                    # JSON verisine görsel URL'sini ekle
                    dish["image"] = image_url

# Sonuçları yazdır
print(json.dumps(data, indent=2))

# JSON verisini başka bir dosyaya kaydetmek için kullanabilirsiniz
# with open("updated_menu.json", "w") as file:
#     json.dump(data, file, indent=2)
