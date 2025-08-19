import json

nft_data = {
    "address": "0:eb8fb7eca21af7e12913df13be860810c91711babb258551347760a5ecf91925",
    "next_item_index": 7,
    "owner": {
        "address": "0:cc75b17f9476c8008099c3e532bcfda61b02e575af9f48b6658755a22896b5a6",
        "is_scam": False,
        "is_wallet": True
    },
    "raw_collection_content": "b5ee9c7201010101004000007c0168747470733a2f2f732e67657467656d732e696f2f6e66742f632f3633666239363334633465633964353031303965393665382f6d6574612e6a736f6e",
    "metadata": {
        "cover_image": "https://s.getgems.io/nft/c/63fb9634c4ec9d50109e96e8/cover/63fb9593b0c782dc1aad55b4.jpg",
        "description": "One King\nOne Owner\nOne Durov",
        "marketplace": "getgems.io",
        "external_url": "https://getgems.io/collection/EQDrj7fsohr34SkT3xO-hggQyRcRurslhVE0d2Cl7PkZJQ7x",
        "social_links": [],
        "name": "CyberTon",
        "image": "https://s.getgems.io/nft/c/63fb9634c4ec9d50109e96e8/avatar/63fb959eb6d78bceec02ce6a.jpg"
    },
    "previews": [
        {"resolution": "5x5", "url": "https://cache.tonapi.io/imgproxy/c20aoMhsRJIu53kULrg7lQq75SH1O8OciHUD4fn1QnU/rs:fill:5:5:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjNmYjk2MzRjNGVjOWQ1MDEwOWU5NmU4L2F2YXRhci82M2ZiOTU5ZWI2ZDc4YmNlZWMwMmNlNmEuanBn.webp"},
        {"resolution": "100x100", "url": "https://cache.tonapi.io/imgproxy/y4i9Rrd4M4nNv1ruXKRujwE6O5ugrhnL2z9vLQctg0U/rs:fill:100:100:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjNmYjk2MzRjNGVjOWQ1MDEwOWU5NmU4L2F2YXRhci82M2ZiOTU5ZWI2ZDc4YmNlZWMwMmNlNmEuanBn.webp"},
        {"resolution": "500x500", "url": "https://cache.tonapi.io/imgproxy/NYrIAgdginnknKIHTxWMNKQdnzdzImfCgWzTqjHtLqQ/rs:fill:500:500:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjNmYjk2MzRjNGVjOWQ1MDEwOWU5NmU4L2F2YXRhci82M2ZiOTU5ZWI2ZDc4YmNlZWMwMmNlNmEuanBn.webp"},
        {"resolution": "1500x1500", "url": "https://cache.tonapi.io/imgproxy/fpyz0yfYVzwsxKuwcuoZ3PfuRgMY_e1m46rBMtzhYVI/rs:fill:1500:1500:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjNmYjk2MzRjNGVjOWQ1MDEwOWU5NmU4L2F2YXRhci82M2ZiOTU5ZWI2ZDc4YmNlZWMwMmNlNmEuanBn.webp"}
    ],
    "approved_by": []
}

print(json.dumps(nft_data, indent=4))
