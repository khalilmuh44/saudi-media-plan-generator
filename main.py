
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()



client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
###################################            ask anything          #############################
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content":"من هي شركة ربحان" }
#     ]
# )


# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

# print("Answer saved successfully! Open answer.txt to read it.")

#######################################   Update     ########################################

# prompt = """
# Update name to Maarten, pronouns to he/him, and job title to Senior Content Developer
# in the following text:
# Joanne is a Content Developer at DataCamp. Her favorite programming language is R,
# which she uses for her statistical analyses.
# """


# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ]
# )


# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

# print("The model successfully updated the name, pronouns, and job title in the biography")


###################################    Text summarization        ########################################

# text= """
# عندهم حسابات علي سوشيال ميديا ليهم شركة في جده للعقارات و عاوزين يظهرو و مش عارف أيه الأفضل أنه ينشأ موقع ولا يستكفي بالحملات - عميل مسؤل التسويق في الشركه مصرى 
# شركه المتولي للتطوير العقارى 
# شركه للتمليك فقط عايزين عملاء القوه الشرائيه بتاعتهم كبيره 
# مقر الشركه في جده 
# معملش حملات 
# اشناء ورد بريس + سيو + حملات 
# 3 شهور 11000 
# اسم العقد هيكون ب اسم محمد ابراهيم المتولي
# بقاله سنتين بس في السوق 
# منافس مباشر  معارج للتطوير العقارى 
# هبعتله العقد وهكلمه الساعه 4 ونص قبل ممشى
# برن عليه مش بيرد 
# هرن عليه قبل ممشى  
# رنيت عليه مش بيرد 
# هرن عليه الساعه 12
# مش بيرد عليا 
# بعتله رساله 

# """

# prompt= F"""Summarize the the customer conversation in the following text in Arabic in three concise key points:
# {text}"""    


# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ] , 
#     # max_completion_tokens=5   # controls the maximum length of the model's response [output only]
#         #The actual number of output tokens is often lower than the max_completion_tokens value.
#     # Total Cost = Input Tokens + Output Tokens
#     #Cost depends on the model and the number of tokens used. More tokens = higher cost. Increasing max_completion_tokens can increase the cost because the model may generate longer responses.
     
# )

# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

# print("The model successfully summarized the customer conversation in the biography")


###############################  Calculating The Cost of the API Call  ########################################
# text= """
# عندهم حسابات علي سوشيال ميديا ليهم شركة في جده للعقارات و عاوزين يظهرو و مش عارف أيه الأفضل أنه ينشأ موقع ولا يستكفي بالحملات - عميل مسؤل التسويق في الشركه مصرى 
# شركه المتولي للتطوير العقارى 
# شركه للتمليك فقط عايزين عملاء القوه الشرائيه بتاعتهم كبيره 
# مقر الشركه في جده 
# معملش حملات 
# اشناء ورد بريس + سيو + حملات 
# 3 شهور 11000 
# اسم العقد هيكون ب اسم محمد ابراهيم المتولي
# بقاله سنتين بس في السوق 
# منافس مباشر  معارج للتطوير العقارى 
# هبعتله العقد وهكلمه الساعه 4 ونص قبل ممشى
# برن عليه مش بيرد 
# هرن عليه قبل ممشى  
# رنيت عليه مش بيرد 
# هرن عليه الساعه 12
# مش بيرد عليا 
# بعتله رساله 

# """

# prompt= F"""Summarize the the customer conversation in the following text in Arabic in three concise key points:
# {text}"""    

# max_completion_tokens = 500   # OUTPUT ONLY
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ] , 
#     max_completion_tokens=max_completion_tokens
     
# )

# input_token_price = 0.15 / 1_000_000    # The cost per input token for the gpt-4o-mini model is $0.15 per million tokens.    
# output_token_price = 0.6 / 1_000_000    # The cost per output token for the gpt-4o-mini model is $0.6 per million tokens.

# input_tokens = response.usage.prompt_tokens
# output_tokens = max_completion_tokens  

# cost = (input_tokens * input_token_price + output_tokens * output_token_price)

# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

# print("The model successfully summarized the customer conversation in the biography")
# print(f"Cost of the API call: ${cost:.6f}")

##########################   Controlling response randomness    ################################

# text= """
# عندهم حسابات علي سوشيال ميديا ليهم شركة في جده للعقارات و عاوزين يظهرو و مش عارف أيه الأفضل أنه ينشأ موقع ولا يستكفي بالحملات - عميل مسؤل التسويق في الشركه مصرى 
# شركه المتولي للتطوير العقارى 
# شركه للتمليك فقط عايزين عملاء القوه الشرائيه بتاعتهم كبيره 
# مقر الشركه في جده 
# معملش حملات 
# اشناء ورد بريس + سيو + حملات 
# 3 شهور 11000 
# اسم العقد هيكون ب اسم محمد ابراهيم المتولي
# بقاله سنتين بس في السوق 
# منافس مباشر  معارج للتطوير العقارى 
# هبعتله العقد وهكلمه الساعه 4 ونص قبل ممشى
# برن عليه مش بيرد 
# هرن عليه قبل ممشى  
# رنيت عليه مش بيرد 
# هرن عليه الساعه 12
# مش بيرد عليا 
# بعتله رساله 

# """


# prompt= F"""Summarize the the customer conversation in the following text in Arabic in three concise key points:
# {text}"""    

# max_completion_tokens = 500   # OUTPUT ONLY
# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ] , 
#     max_completion_tokens=max_completion_tokens , 
#     temperature=1  # The temperature parameter controls the randomness of the model's output. A higher value (e.g., 0.8) makes the output more random, while a lower value (e.g., 0.2) makes it more deterministic.
     
# )

# input_token_price = 0.15 / 1_000_000    # The cost per input token for the gpt-4o-mini model is $0.15 per million tokens.    
# output_token_price = 0.6 / 1_000_000    # The cost per output token for the gpt-4o-mini model is $0.6 per million tokens.

# input_tokens = response.usage.prompt_tokens
# output_tokens = max_completion_tokens  

# cost = (input_tokens * input_token_price + output_tokens * output_token_price)

# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

# print("The model successfully summarized the customer conversation in the biography")
# print(f"Cost of the API call: ${cost:.6f}")

######################################   Text Generation Marketing #############################

# prompt = """Generate 5 taglines similar to:

# We Fund. We Operate. We Scale.

# Company funds, operates, and scales businesses.
# Responsible for growth and results.
# Short, premium, bold."""

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "user", "content": prompt}
#     ] , 
    
# )

# with open("answer.txt", "w", encoding="utf-8") as file:
#     file.write(response.choices[0].message.content)

########################################   PDF ###########################
import re
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import markdown




def is_valid_hex(color):
    return bool(re.match(r"^#[0-9A-Fa-f]{6}$", color))


def extract_brand_assets(soup, base_url):
    theme_color = None

    meta_theme = soup.find("meta", attrs={"name": "theme-color"})
    if meta_theme and meta_theme.get("content"):
        color = meta_theme.get("content").strip()
        if is_valid_hex(color):
            theme_color = color

    html_text = str(soup)

    hex_colors = re.findall(r"#[0-9A-Fa-f]{6}", html_text)

    ignored_colors = {
        "#ffffff", "#000000", "#f5f5f5", "#eeeeee", "#e5e5e5",
        "#cccccc", "#dddddd", "#f9f9f9", "#111111", "#222222"
    }

    filtered_colors = [
        c for c in hex_colors
        if c.lower() not in ignored_colors
    ]

    primary_color = theme_color or (filtered_colors[0] if filtered_colors else "#4f46e5")
    secondary_color = filtered_colors[1] if len(filtered_colors) > 1 else "#111827"

    logo_url = None

    og_image = soup.find("meta", property="og:image")
    if og_image and og_image.get("content"):
        logo_url = og_image.get("content")

    if not logo_url:
        logo_img = soup.find("img", attrs={"alt": re.compile("logo|شعار", re.I)})
        if logo_img and logo_img.get("src"):
            logo_url = logo_img.get("src")

    if logo_url and logo_url.startswith("/"):
        logo_url = base_url.rstrip("/") + logo_url

    return {
        "primary_color": primary_color,
        "secondary_color": secondary_color,
        "logo_url": logo_url
    }


def fetch_store_page(url):
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers, timeout=20)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    brand_assets = extract_brand_assets(soup, url)

    for tag in soup(["script", "style", "noscript"]):
        tag.decompose()

    title = soup.title.get_text(strip=True) if soup.title else ""

    meta_description = ""
    meta = soup.find("meta", attrs={"name": "description"})
    if meta:
        meta_description = meta.get("content", "")

    headings = [
        h.get_text(" ", strip=True)
        for h in soup.find_all(["h1", "h2", "h3"])
        if h.get_text(strip=True)
    ]

    links_ctas = [
        a.get_text(" ", strip=True)
        for a in soup.find_all(["a", "button"])
        if a.get_text(strip=True)
    ]

    page_text = soup.get_text(" ", strip=True)

    return {
        "title": title,
        "meta_description": meta_description,
        "headings": headings[:50],
        "links_ctas": links_ctas[:80],
        "page_text": page_text[:12000],
        "brand_assets": brand_assets
    }


store_name = "سليمان أكاديمي"
store_url = "https://solimanacademy.com/"
niche = "تعليم وتطوير مهارات"
budget = "10000 SAR"
country = "Saudi Arabia"

store_data = fetch_store_page(store_url)

primary_color = store_data["brand_assets"]["primary_color"]
secondary_color = store_data["brand_assets"]["secondary_color"]
logo_url = store_data["brand_assets"]["logo_url"]

#####################################
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
- Do not assume all platforms are suitable.
- Choose platforms based on country, niche, audience behavior, product type, and customer journey.
- Avoid recommending Facebook for Saudi e-commerce unless there is a strong reason.
- For Saudi e-commerce, consider Instagram, Snapchat, TikTok, Google Search, Google Shopping, and WhatsApp where suitable.
- Always explain why each platform is recommended or excluded.
- Always mention the store name throughout the report.

Very important Arabic wording rules:
- Do not use the Arabic word "قضايا".
- Replace it with softer terms like:
  "ملاحظات", "فرص تحسين", "نقاط تحتاج تطوير", "فرص تعزيز", "ملاحظاتنا على تجربة المتجر".
- Do not use heavy or negative wording.
- Avoid saying "مشاكل المتجر".
- Use advisory wording that feels respectful and consultative.
- Do not use direct translations like "الإبداعات" for creatives.
- Use "أفضل أشكال الإعلانات" or "أنواع المحتوى المقترحة".
- Do not say "البيع الإضافي والبيع المتقاطع" as a main section title.
- Use "فرص زيادة قيمة السلة" instead.
- Explain upsell and cross-sell as:
  "اقتراح منتجات أعلى قيمة أو منتجات مكملة تساعد على رفع متوسط قيمة الطلب".

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

The report must include:
1. Store audit:
   - Conversion improvement opportunities
   - Customer experience observations
   - Trust-building opportunities
   - Content improvement opportunities
   - SEO improvement opportunities
   - Offer improvement opportunities
2. Suitable marketing channels analysis.
3. First-month platform budget allocation.
4. Retargeting funnel:
   - View Content
   - Add To Cart
   - Initiate Checkout
   - Purchase
5. Increasing average order value.
6. WhatsApp retargeting campaigns.
7. Content plan mapped to funnel stages.
8. Recommended ad formats for each platform:
   - Image
   - Video
   - Carousel
   - UGC
   - Product demo
9. Target audiences:
   - Direct audiences
   - Indirect audiences
10. SEO recommendations.
11. Quick wins.
12. 90-day growth roadmap.

Output in Markdown.
Use tables whenever possible.
Include estimated KPIs.
Include expected ROAS benchmarks.
Include budget percentages and SAR amounts.
Include implementation priorities: High / Medium / Low.
Prioritize actionable recommendations over theory.
"""

#######################################################
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
بعد مراجعة متجر العطور الفاخرة، تظهر فرصة قوية لرفع المبيعات من خلال تحسين صفحات المنتجات، بناء ثقة أكبر داخل المتجر، وتفعيل حملات إعادة الاستهداف حسب مراحل رحلة العميل.

## 2. القنوات الإعلانية المناسبة

| القناة | مناسبة؟ | السبب |
|---|---|---|
| Instagram | نعم | مناسب لاكتشاف منتجات العطور وبناء الرغبة الشرائية |
| Snapchat | نعم | قوي في السوق السعودي خصوصًا للمنتجات الاستهلاكية |
| TikTok | نعم | مناسب للفيديوهات القصيرة وتجارب الاستخدام |
| Google Search | نعم | يستهدف العملاء أصحاب نية الشراء العالية |
| Facebook | لا | ليس القناة الأقوى لهذا النوع من العملاء في السعودية |

## 3. فرص تحسين معدل التحويل

| التوصية | التأثير المتوقع | الأولوية |
|---|---|---|
| إضافة تقييمات العملاء داخل صفحات المنتجات | زيادة الثقة قبل الشراء | High |
| توضيح سياسة الشحن والاسترجاع | تقليل تردد العميل | High |
| إنشاء عروض مجمعة للمنتجات الأكثر مبيعًا | رفع متوسط قيمة الطلب | Medium |
"""


user_prompt = f"""
Store Name: {store_name}
Store URL: {store_url}
Niche: {niche}
Monthly Budget: {budget}
Target Country: {country}

Extracted Website Data:

Page Title:
{store_data["title"]}

Meta Description:
{store_data["meta_description"]}

Headings:
{store_data["headings"]}

Links / CTAs:
{store_data["links_ctas"]}

Page Text:
{store_data["page_text"]}

Detected Brand Assets:
Primary Color: {primary_color}
Secondary Color: {secondary_color}
Logo URL: {logo_url}

Create a complete customized audit and media plan based on this website data.
Mention actual issues and opportunities you notice from the extracted data.
Do not use technical terms unless you explain their business impact.
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

logo_html = ""
if logo_url:
    logo_html = f'<img src="{logo_url}" class="logo" alt="Store Logo">'

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

body {{
    font-family: Tahoma, Arial, sans-serif;
    direction: rtl;
    background: linear-gradient(135deg, var(--bg), #ffffff);
    color: var(--text);
    padding: 40px;
    margin: 0;
}}

.report {{
    background: white;
    max-width: 1100px;
    margin: auto;
    padding: 0;
    border-radius: 22px;
    overflow: hidden;
    box-shadow: 0 18px 45px rgba(0,0,0,0.10);
}}

.cover {{
    padding: 50px;
    background: linear-gradient(135deg, var(--primary), var(--secondary));
    color: white;
}}

.logo {{
    max-height: 80px;
    max-width: 180px;
    background: white;
    padding: 10px;
    border-radius: 12px;
    margin-bottom: 25px;
}}

.cover h1 {{
    margin: 0;
    font-size: 34px;
    line-height: 1.5;
}}

.cover p {{
    margin-top: 12px;
    font-size: 17px;
    opacity: 0.95;
}}

.content {{
    padding: 45px;
}}

h1 {{
    color: var(--dark);
    font-size: 32px;
    padding-bottom: 18px;
    border-bottom: 4px solid var(--primary);
}}

h2 {{
    color: var(--primary);
    margin-top: 38px;
    font-size: 25px;
    border-right: 6px solid var(--primary);
    padding-right: 12px;
}}

h3 {{
    color: var(--secondary);
    margin-top: 28px;
}}

p, li {{
    font-size: 16px;
    line-height: 1.95;
}}

ul {{
    padding-right: 25px;
}}

table {{
    width: 100%;
    border-collapse: collapse;
    margin: 24px 0;
    font-size: 15px;
    overflow: hidden;
    border-radius: 12px;
}}

th {{
    background: var(--primary);
    color: white;
    padding: 13px;
    border: 1px solid var(--primary);
}}

td {{
    padding: 13px;
    border: 1px solid var(--border);
    background: #ffffff;
}}

tr:nth-child(even) td {{
    background: #fafafa;
}}

strong {{
    color: var(--secondary);
}}

.footer {{
    margin-top: 50px;
    padding-top: 22px;
    border-top: 1px solid var(--border);
    text-align: center;
    color: var(--muted);
    font-size: 13px;
}}

@media print {{
    body {{
        background: white;
        padding: 0;
    }}

    .report {{
        box-shadow: none;
        border-radius: 0;
        max-width: 100%;
    }}

    .cover {{
        -webkit-print-color-adjust: exact;
        print-color-adjust: exact;
    }}
}}
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
        {report_html_body}

        <div class="footer">
            تم إعداد هذا التقرير بواسطة شركة ربحان
        </div>
    </div>

</div>
</body>
</html>
"""

with open("media_plan.html", "w", encoding="utf-8") as file:
    file.write(html_template)

print("HTML Report Created Successfully: media_plan.html")
print("Primary Color:", primary_color)
print("Secondary Color:", secondary_color)
print("Logo URL:", logo_url)