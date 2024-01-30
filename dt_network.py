import numpy as np
class NetworkDigitalTwin:
    def __init__(s, n=6, rate=20):
        s.n = n; s.rate = rate
    def simulate(s, periods=365, seed=42):
        rng = np.random.default_rng(seed)
        demand = np.maximum(rng.normal(800, 160, periods), 0)
        results = []; inv = 800*2; cost = 0
        for t in range(periods):
            d = demand[t]
            order = max(0, d*1.1 - inv + 800)
            inv = max(0, inv + order - d)
            holding = inv * 0.03
            shortage = max(0, d - inv) * 40
            cost += holding + shortage
            results.append({{"period": t, "demand": round(d,1), "inventory": round(inv,1), "cost": round(holding+shortage,1)}})
        return {{"total_cost": round(cost,0), "avg_inventory": round(np.mean([r["inventory"] for r in results]),1),
                "service_level": round(np.mean([1 for r in results if r["inventory"]>0])*100,1),
                "periods": len(results)}}
if __name__=="__main__": print(NetworkDigitalTwin().simulate())
