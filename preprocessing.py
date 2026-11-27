import json
import geopandas as gpd

gdf = gpd.read_file("data/20260907_S1C_X1X4v2.shp")

# 1. Keep only geometry (drops heavy attribute columns)
gdf = gdf[["geometry"]].copy()
gdf["geometry"] = gdf.geometry.make_valid()
gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()]

# 2. Drop tiny flood polygons (e.g., smaller than 50,000 m² ≈ 5 hectares)
# EPSG:32651 works well for Central Visayas / eastern PH; use EPSG:32650 for western PH
gdf_proj = gdf.to_crs(epsg=32651)
gdf = gdf[gdf_proj.geometry.area >= 1_000_000].copy()

# 3. Simplify geometry more aggressively (in degrees; ~0.002–0.005 is ~200m–500m)
gdf = gdf.to_crs(epsg=4326)
gdf["geometry"] = gdf["geometry"].simplify(tolerance=0.005, preserve_topology=True)
gdf = gdf[~gdf.geometry.is_empty & gdf.geometry.notna()]

# 4. Round coordinate decimals (5 decimals ≈ 1.1m precision, trims JSON size)
geojson_obj = json.loads(gdf.to_json())

def round_coords(coords, precision=4):
    if isinstance(coords[0], (int, float)):
        return [round(coords[0], precision), round(coords[1], precision)]
    return [round_coords(c, precision) for c in coords]

for feature in geojson_obj.get("features", []):
    geom = feature.get("geometry")
    if geom and "coordinates" in geom:
        geom["coordinates"] = round_coords(geom["coordinates"], precision=5)

with open("data/philsa_flood_web.geojson", "w", encoding="utf-8") as f:
    json.dump(geojson_obj, f, separators=(",", ":"))  # compact JSON, no whitespace