import json
import time

# 测试1：验证图片文章格式
print("=== 测试1：图片文章格式验证 ===")

# 模拟带图片的文章发布
new_article = {
    "id": int(time.time()),
    "title": "京都红叶摄影集",
    "date": "2025-12-23",
    "tags": ["旅行", "摄影"],
    "preview": "记录京都红叶季的绝美瞬间，岚山竹林与清水寺的红叶相映成趣。",
    "content": "<p>京都的秋天是一场视觉盛宴。每年11月，整座城市被层层叠叠的红叶覆盖，从深红到金黄，宛如印象派画家的调色盘。</p><p>岚山的竹林小径在红叶映衬下更显幽静，阳光透过枝叶洒下斑驳光影，漫步其中仿佛穿越时空。</p>",
    "images": [
        {
            "src": "../Picture/kyoto-red-leaves.jpg",  # 相对路径：从博客目录到Picture目录
            "alt": "岚山竹林红叶",
            "width": "100%",
            "height": "auto"
        },
        {
            "src": "../Picture/kinkaku-ji.jpg",
            "alt": "金阁寺秋景",
            "width": "100%",
            "height": "auto"
        }
    ]
}

# 输出格式化JSON
print(json.dumps(new_article, indent=2, ensure_ascii=False))
print("\n✅ JSON格式验证通过！")

# 测试2：验证图片路径格式
print("\n=== 测试2：图片路径格式验证 ===")

# 检查图片路径是否为相对路径
for i, img in enumerate(new_article["images"]):
    src = img["src"]
    if not src.startswith("../Picture/"):
        print(f"❌ 图片{i+1}路径格式不正确：{src}")
    else:
        print(f"✅ 图片{i+1}路径格式正确：{src}")

print("\n=== 测试完成 ===")