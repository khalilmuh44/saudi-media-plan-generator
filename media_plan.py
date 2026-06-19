def generate_media_plan(store_name, store_url, niche, budget, country):
    store_data = fetch_store_page(store_url)

    raw_primary_color = store_data["brand_assets"]["primary_color"]
    raw_secondary_color = store_data["brand_assets"]["secondary_color"]

    primary_color = protect_brand_color(raw_primary_color, "#2563eb")
    secondary_color = protect_brand_color(raw_secondary_color, "#111827")

    cover_text_color = get_text_color(primary_color)
    table_text_color = get_text_color(primary_color)

    logo_url = store_data["brand_assets"]["logo_url"]

    # (استدعاء OpenAI والحصول على report_markdown كما في كودك)
    system_prompt = """

    You are a senior Saudi e-commerce media buyer and growth consultant.

    You are writing for Saudi store owners, not marketers.

    Use professional, simple Saudi Arabic.

    Use soft, advisory, business-friendly language.

    Avoid technical jargon.

    If you mention a technical issue, explain its business impact on:

    - Sales

    - Conversion rate

    - Customer trust

    - ROAS



    Important:

    - Do not create a generic media plan.

    - First audit the store based on the extracted website data.

    - Then create the media plan based on the audit.

    - Choose platforms based on country, niche, audience behavior, product type, and customer journey.

    - Avoid recommending Facebook for Saudi e-commerce unless there is a strong reason.

    - Always mention the store name throughout the report.



    Very important Arabic wording rules:

    - Do not use the Arabic word "قضايا". Replace it with: "ملاحظات", "فرص تحسين", "نقاط تحتاج تطوير".

    - Do not use "مشاكل المتجر".

    - Do not use "الإبداعات" for creatives. Use "أفضل أشكال الإعلانات".

    - Do not say "البيع الإضافي والبيع المتقاطع"; use "فرص زيادة قيمة السلة" instead.



    Use these business-friendly section names:

    - الملخص التنفيذي

    - ملاحظاتنا على تجربة المتجر

    - فرص تحسين معدل التحويل

    - القنوات الإعلانية المناسبة

    - توزيع ميزانية أول شهر

    - خطة إعادة الاستهداف

    - فرص زيادة قيمة السلة

    - حملات واتساب

    - خطة المحتوى حسب مراحل الفانل

    - أفضل أشكال الإعلانات لكل منصة

    - الشرائح المستهدفة

    - فرص تحسين الظهور في Google

    - إجراءات سريعة التنفيذ

    - خطة نمو خلال 90 يوم

    

    Add a section called:

    - تقييم المتجر من 10



    Give the store an overall score out of 10.



    Also give separate scores out of 10 for:

    - تجربة العميل داخل المتجر

    - وضوح العروض

    - الثقة والمصداقية

    - صفحات المنتجات

    - فرص تحسين معدل التحويل

    - فرص الظهور في Google

    - جاهزية المتجر للإعلانات



    For each score, explain briefly:

    - Why this score was given

    - What can improve it



    Use a positive advisory tone.

    Do not make the client feel criticized.



    في نهاية قسم التقييم، اكتب السطر التالي بالظبط لتسهيل قراءته برمجياً:

    التقييم النهائي للمتجر هو: [اكتب الرقم هنا بدون أقواس مثل 8]



    Output in Markdown. Use tables whenever possible.

    """



    example_user = """

    Store Name: متجر العطور الفاخرة

    Niche: متجر عطور

    Monthly Budget: 15000 SAR

    Target Country: Saudi Arabia

    Generate a complete media plan.

    """



    example_assistant = """

    # الخطة التسويقية لمتجر العطور الفاخرة

    ## 1. الملخص التنفيذي

    بعد مراجعة متجر العطور الفاخرة...

    ## 2. القنوات الإعلانية المناسبة

    | القناة | مناسبة؟ | السبب |

    |---|---|---|

    | Instagram | نعم | مناسب لاكتشاف منتجات العطور |

               

    ## تقييم المتجر من 10

    | العنصر | التقييم | الملاحظة |

    |---|---|---|

    | تجربة العميل داخل المتجر | 7/10 | التجربة جيدة، لكن يمكن تحسين وضوح التنقل |

    | الثقة والمصداقية | 8/10 | وجود خبرة طويلة يعزز الثقة |

    | صفحات المنتجات | 6/10 | تحتاج إبراز التقييمات والعروض بشكل أوضح |

    | جاهزية المتجر للإعلانات | 7/10 | مناسب للإعلانات مع بعض التحسينات قبل التوسع |



    التقييم النهائي للمتجر هو: 7

    """



    user_prompt = f"""

    Store Name: {store_name}

    Store URL: {store_url}

    Niche: {niche}

    Monthly Budget: {budget}

    Target Country: {country}



    Extracted Website Data:

    Page Title: {store_data["title"]}

    Meta Description: {store_data["meta_description"]}

    Headings: {store_data["headings"]}

    Links / CTAs: {store_data["links_ctas"]}

    Page Text: {store_data["page_text"]}



    Detected Brand Assets:

    Primary Color: {primary_color}

    Secondary Color: {secondary_color}

    Logo URL: {logo_url}



    Create a complete customized audit and media plan based on this website data.

    """






    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": example_user},
            {"role": "assistant", "content": example_assistant},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.3,
    )
    report_markdown = response.choices[0].message.content
    report_html_body = markdown.markdown(report_markdown, extensions=["tables"])
    match = re.search(r"التقييم النهائي للمتجر هو:\s*(\d+)", report_markdown)
    final_score = match.group(1) if match else "7"
    logo_html = f'<img src="{logo_url}" class="logo" alt="Store Logo">' if logo_url else ""

    # لاحظ مضاعفة الأقواس {{ }} في الـ CSS أدناه
    html_template = f"""
    <!DOCTYPE html>
    <html lang="ar" dir="rtl">
    <head>
    <meta charset="UTF-8">
    <title>الخطة التسويقية - {store_name}</title>
    <style>
        :root {{
            --primary: {primary_color};
            --secondary: {secondary_color};
            --dark: #111827;
            --text: #1f2937;
            --muted: #6b7280;
            --bg: #f5f7fb;
            --border: #e5e7eb;
        }}
        body {{ font-family: Tahoma, Arial, sans-serif; direction: rtl; background: linear-gradient(135deg, var(--bg), #ffffff); color: var(--text); padding: 40px; margin: 0; }}
        .report {{ background: white; max-width: 1100px; margin: auto; border-radius: 22px; overflow: hidden; box-shadow: 0 18px 45px rgba(0,0,0,0.10); }}
        .cover {{ padding: 50px; background: linear-gradient(135deg, var(--primary), var(--secondary)); color: {cover_text_color}; }}
        .logo {{ max-height: 80px; max-width: 180px; background: white; padding: 10px; border-radius: 12px; margin-bottom: 25px; }}
        .cover h1, .cover p {{ color: {cover_text_color} !important; }}
        .content {{ padding: 45px; }}
        .score-box {{ background: #fdfaf4; padding: 25px; border-radius: 16px; text-align: center; margin: 10px auto 35px auto; max-width: 440px; border: 2px solid var(--primary); box-shadow: 0 4px 15px rgba(0,0,0,0.04); }}
        .score-number {{ font-size: 56px; font-weight: bold; color: var(--dark); }}
        h1 {{ color: var(--dark); font-size: 32px; padding-bottom: 18px; border-bottom: 4px solid var(--primary); }}
        h2 {{ color: var(--dark); margin-top: 38px; font-size: 25px; border-right: 6px solid var(--primary); padding-right: 12px; }}
        table {{ width: 100%; border-collapse: collapse; margin: 24px 0; }}
        th {{ background: var(--primary); color: {table_text_color}; padding: 13px; }}
        td {{ padding: 13px; border: 1px solid var(--border); }}
        .footer {{ margin-top: 50px; padding-top: 22px; border-top: 1px solid var(--border); text-align: center; color: var(--muted); font-size: 13px; }}
    </style>
    </head>
    <body>
    <div class="report">
        <div class="cover">
            {logo_html}
            <h1>الخطة التسويقية لمتجر {store_name}</h1>
            <p>تقرير مخصص مبني على تحليل بيانات المتجر، الهوية البصرية، والسوق السعودي.</p>
        </div>
        <div class="content">
            <div class="score-box">
                <div class="score-number">{final_score}/10</div>
                <div class="score-label">التقييم العام للمتجر</div>
            </div>
            {report_html_body}
            <div class="footer">
                تم إعداد هذا التقرير بواسطة شركة أمين للحلول التسويقية والنمو الرقمي
            </div>
        </div>
    </div>
    </body>
    </html>
    """

    with open("media_plan.html", "w", encoding="utf-8") as file:
        file.write(html_template)
    
    return html_template, report_markdown