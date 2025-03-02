def get_coffee_recommendation(q1, q2, q3, q4):
    recommendations = {
        ("すぐ行動する", "フルーティー", "朝食と一緒に", "いいえ"): ("エチオピア 浅煎り ☕", "フルーティーな香りが特徴で、朝のすっきりした時間に最適。"),
        ("ゆっくりコーヒーを飲む", "バランスが良い", "リラックスタイム", "はい"): ("コロンビア 中煎り ☕", "バランスの取れたコクと甘み。スイーツと相性抜群。"),
        ("読書から始める", "しっかり苦味", "仕事中", "いいえ"): ("グアテマラ 深煎り ☕", "豊かな香りとしっかりしたボディ。集中したいときに最適。"),
        ("ゆっくりコーヒーを飲む", "フルーティー", "朝食と一緒に", "はい"): ("ケニア 浅煎り ☕", "ベリーのような酸味が特徴で、さっぱりとした味わい。"),
        ("すぐ行動する", "バランスが良い", "仕事中", "はい"): ("ブラジル 中煎り ☕", "ナッツのような甘みがあり、飲みやすい。"),
    }
    return recommendations.get((q1, q2, q3, q4), ("マンデリン 深煎り ☕", "濃厚でスモーキーな苦味が特徴。しっかりした味わい。"))
