موقع روابط Sentry (GitHub Pages) — خطوات لمرة واحدة

1) أنشئ مستودعاً عاماً (Public) على GitHub باسم بالضبط:  nt18s-max.github.io
2) ارفع محتويات هذا المجلد كلها إلى جذر المستودع (بما فيها المجلد المخفي .well-known والملف .nojekyll).
3) خذ بصمة توقيع التطبيق: من سجل بناء GitHub Actions (سطر "APK certificate SHA-256: ...") ثم:
      python3 set_fingerprint.py <البصمة>
   وارفع ملف .well-known/assetlinks.json المحدّث.
4) فعّل Pages: Settings > Pages > Deploy from a branch > main / (root).
5) تحقق من فتح الرابط في المتصفح:  https://nt18s-max.github.io/.well-known/assetlinks.json
6) ثبّت نسخة التطبيق الجديدة (التحقق من الرابط يتم عند التثبيت وبوجود إنترنت).
شكل الرابط:  https://nt18s-max.github.io/l/v/<الرمز>
