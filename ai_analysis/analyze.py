def explain_vulns(results):
    if not results:
        return "لم يتم اكتشاف أي ثغرات."
    
    summary = []
    for item in results:
        if 'vuln' in item:
            if item['vuln'] == "XSS":
                summary.append("ثغرة XSS تُمكن المهاجم من تنفيذ جافاسكربت ضار في المتصفح.")
            elif item['vuln'] == "SQL Injection":
                summary.append("ثغرة SQL Injection تتيح الوصول غير المصرح به لقاعدة البيانات.")
        else:
            summary.append("حدث خطأ أثناء الفحص: " + item.get("error", "غير معروف"))
    return " | ".join(summary)