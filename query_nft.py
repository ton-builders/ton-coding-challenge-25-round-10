import json

nft_data = {
    "address": "0:905d9072478187fea0a6e9a468bef77e183eaa29bfcc14300daf443417f7822c",
    "next_item_index": 3,
    "owner": {
        "address": "0:c57fcc0854a41e95eaf4b34a38ed80f30906620ade5fa1062b29f43b98f4e802",
        "name": "anonfireplace.ton",
        "is_scam": False,
        "is_wallet": True
    },
    "raw_collection_content": "b5ee9c7201010101004000007c0168747470733a2f2f732e67657467656d732e696f2f6e66742f632f3635653731656163396461393834646665643339643130352f6d6574612e6a736f6e",
    "metadata": {
        "description": "This collection is a series of 10 REAL paintings! All canvases are made with oil using potal. Feelings are something we can hardly control, but they encourage us to take the actions that make US! Some to a greater extent, some have their impact imperceptibly, like a summer wind. The series of paintings has been produced since 2019, at the moment 4/10 is ready. My works have already been presented at exhibitions of contemporary art. By purchasing any of these NFTs, you become the owner of a REAL picture that I will send you anywhere in the world (delivery is not included in the price). The release of the series at the physical exhibition is scheduled for 2025",
        "marketplace": "getgems.io",
        "external_url": "https://getgems.io/collection/EQCQXZByR4GH_qCm6aRovvd-GD6qKb_MFDANr0Q0F_eCLPq1",
        "social_links": ["https://t.me/illidaneageoffury"],
        "name": "FEELINGS",
        "image": "https://s.getgems.io/nft/c/65e71eac9da984dfed39d105/avatar/413067.png",
        "cover_image": "https://s.getgems.io/nft/c/65e71eac9da984dfed39d105/cover/413066.png"
    },
    "previews": [
        {"resolution": "5x5", "url": "https://cache.tonapi.io/imgproxy/UhUac5-KuX6n0W48_CLpLbttuyCPVhD5VYSx46ovJf4/rs:fill:5:5:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjVlNzFlYWM5ZGE5ODRkZmVkMzlkMTA1L2F2YXRhci80MTMwNjcucG5n.webp"},
        {"resolution": "100x100", "url": "https://cache.tonapi.io/imgproxy/I3k64woStt3BogjOP7__CovrTZdofsDi14afDFJKXbk/rs:fill:100:100:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjVlNzFlYWM5ZGE5ODRkZmVkMzlkMTA1L2F2YXRhci80MTMwNjcucG5n.webp"},
        {"resolution": "500x500", "url": "https://cache.tonapi.io/imgproxy/1L0744YhSkvvd999MpbaD6qrKZShETHGHBLTFclYSfs/rs:fill:500:500:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjVlNzFlYWM5ZGE5ODRkZmVkMzlkMTA1L2F2YXRhci80MTMwNjcucG5n.webp"},
        {"resolution": "1500x1500", "url": "https://cache.tonapi.io/imgproxy/la0bOQGvnabWJDvFRmEnHRJb760bHAs_fqbBBRO7r3Q/rs:fill:1500:1500:1/g:no/aHR0cHM6Ly9zLmdldGdlbXMuaW8vbmZ0L2MvNjVlNzFlYWM5ZGE5ODRkZmVkMzlkMTA1L2F2YXRhci80MTMwNjcucG5n.webp"}
    ],
    "approved_by": []
}

print(json.dumps(nft_data, indent=4))
