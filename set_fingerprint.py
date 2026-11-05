"""python3 set_fingerprint.py <sha256>  -- writes the app's signing fingerprint into
.well-known/assetlinks.json. Accepts the value as printed by the build log
("APK certificate SHA-256: ab12..."), with or without colons."""
import json, re, sys

raw = (sys.argv[1] if len(sys.argv) > 1 else "").replace(":", "").strip().lower()
if not re.fullmatch(r"[0-9a-f]{64}", raw):
    sys.exit("اكتب البصمة كاملة: 64 حرفاً/رقماً (SHA-256).")
fp = ":".join(raw[i:i + 2] for i in range(0, 64, 2)).upper()
path = ".well-known/assetlinks.json"
data = json.load(open(path))
data[0]["target"]["sha256_cert_fingerprints"] = [fp]
json.dump(data, open(path, "w"), indent=2)
print("تم:", fp)
